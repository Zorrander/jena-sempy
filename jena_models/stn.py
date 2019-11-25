import copy
import networkx as nx

class SimpleTemporalNetwork(object):
    def __init__(self):
        self._graph = nx.DiGraph()
        self.synch_table = {}

    def model_temporal_problem(self, skill):
        """ Converts the problem into an STNU

        Translate the lists of steps and their constraints into timepoints and links between them.
        """
        print("Steps >>>")
        for step in steps:
            print("{} >>> {} >>> {}".format(step[0], step[1], step[2]))
        print("Constraints >>>")
        for constraint in constraints:
            print("{} -------- {}".format(constraint[0], constraint[1]))
        stn = SimpleTemporalNetwork()
        for step in steps:
            self.base_solution.synch_table.update( { step[0] : [] } )
            previous = ""
            for task in step[2]:
                node = stn.add_event(task, step[1], step[0])
                if previous and previous != node:
                    stn.set_relation(previous, node, 'temporal_constraint', (DEFAULT_HUMAN_EXECUTION_TIME, DEFAULT_ROBOT_EXECUTION_TIME))
                previous = node

        for constraint in constraints:
            if constraint[0]:
                node_b = stn._find_first_task(constraint[1])
                if isinstance(constraint[0], list):
                    for step in constraint[0]:
                        node_a = stn._find_last_task(step)
                        stn.set_relation(node_a, node_b, 'temporal_constraint', (DEFAULT_HUMAN_EXECUTION_TIME, DEFAULT_ROBOT_EXECUTION_TIME))
                        self.base_solution.synch_table[constraint[1]].append(step)
                else:
                    node_a = stn._find_last_task(constraint[0])
                    stn.set_relation(node_a, node_b, 'temporal_constraint', (DEFAULT_HUMAN_EXECUTION_TIME, DEFAULT_ROBOT_EXECUTION_TIME))
                    self.base_solution.synch_table[constraint[1]].append(constraint[0])
            else:
                node = stn._find_first_task(constraint[1])
                stn.set_relation("Start", node, 'temporal_constraint', (-10000, 0))
        return stn, steps

    @property
    def timepoints(self):
        """Get the timepoints of the network."""
        return [task for task in self._graph.nodes(data=True) if not task[0] == "Start"]

    def update_after_completion(self, event, time):
        print ("Before {}".format(self.synch_table))
        del self.synch_table[event]
        for step, synch in self.synch_table.items():
            if event in synch:
                self.synch_table[step].remove(event)
        print ("After {}".format(self.synch_table))

    def available_steps(self):
        """Get the available events in the network."""
        return [(step, self.retrieve_subgraph(step)) for step, synch in self.synch_table.items() if not synch]

    def retrieve_subgraph(self, step):
        return self._graph.subgraph( [n for n,attrdict in self._graph.node.items() if not n == "Start" and attrdict['step'] == step ] )

    def _are_available(self, events):
        return False if False in map(self._is_available, events) else True

    def get_event(self, event, data=False):
        """Return the value for an attribute of the node 'event' if data. All the attributes otherwise."""
        return self._graph.nodes(data=data)[event] if data else self._graph.nodes(data=True)[event]

    def add_event(self, name, task=None, step=None, is_done=False):
        """Create a new node in the graph."""
        id = nx.number_of_nodes(self._graph)+1
        self._graph.add_node(id, value=name, task=task, step=step, is_done=is_done, is_claimed=False)
        return id

    def set_event(self, name, data, value):
        """ Set the attribute 'data' of the node 'name' to 'value'"""
        nx.set_node_attributes(self._graph, value, data)

    def has_relation(self, u, v):
        """ Return the value of an edge. False if it does not exist."""
        return self._graph.edges[u, v]['temporal_constraint'] if self._graph.has_edge(u, v) else False

    def set_relation(self, u, v, data, value):
        """Set the value of an edge. Create if it does not exist yet."""
        if not self.has_relation(u, v):
            self._graph.add_edge(u, v)
        self._graph.edges[u, v][data] = value

    def adjacent_nodes(self, node=False):
        """Return the list of events related to the argument"""
        return list(self._graph.adj[node[0]]) if type(node) is tuple else list(self._graph.adj[node])

    def construct_distance_graph(self):
        """ Translate the constraint form representation into its associated distance graph.

        The distance graph indicates the same interval as the constraint but yields two equivalent inequalities.
        """
        new_edges = []
        for u, v, weight in tqdm(self._graph.edges(data='temporal_constraint')):
            lower_bound = weight[0] if not isinstance(weight, int) else weight
            upper_bound = weight[1] if not isinstance(weight, int) else weight
            self.set_relation(u, v, 'temporal_constraint', upper_bound)
            self.set_relation(v, u, 'temporal_constraint', -lower_bound)
            new_edges.append((v, u, -lower_bound))

    def all_pairs_shortest_paths(self):
        """ Compute all pairs shortest paths with Floyd-Warshall algorithm

        Computes a fully-connected network, with binary constraints relating each pair of events.
        """
        distance = nx.floyd_warshall(self._graph, weight='temporal_constraint')
        for node_a in tqdm(distance):
            for node_b in distance[node_a]:
                if not(node_a==node_b or (node_a, node_b) in list(self._graph.edges)):
                    self.set_relation(node_a, node_b, 'temporal_constraint', distance[node_a][node_b])

    def prune_redundant_constraints(self):
        """ Remove dominated edges.

        Remove dominated edges to make STN dispatchable.
        """
        graph = copy.deepcopy(self._graph)
        for A, B, weight in tqdm(self._graph.edges(data='temporal_constraint')):
            for C in set(self._graph.successors(A)).intersection(self._graph.successors(B)):
                a_c = self.has_relation(A, C)
                b_c = self.has_relation(B, C)
                if self.is_dominated(a_c, b_c, weight):
                    try:
                        graph.remove_edge(A, C)
                    except:
                        pass
                    break
        self._graph = graph

    def is_dominated(self, edge_ac, edge_bc, edge_ab):
        if (edge_ac > 0 and edge_bc > 0) or (edge_ac < 0 and edge_ab < 0):
            return True if edge_ac == edge_ab + edge_bc else False
        else:
            return False


    def print_graph(self):
        print(list(self._graph.nodes(data=True)))
        print(list(self._graph.edges(data=True)))

    def find_first_task(self, step):
        """ Identify the first task within a step """
        for u, v in self._graph.edges():
            if (not (u == "Start")) and self._graph.nodes(data='step')[u] == step:
                has_predecessor = False
                for u_dot, v_dot in self._graph.edges():
                    if v_dot == u and self._graph.nodes(data='step')[u_dot] == step and not (u_dot == "Start"):
                        has_predecessor = True
                if not has_predecessor:
                    return u

    def find_last_task(self, step):
        """ Identify the last task within a step """
        for u, v in self._graph.edges():
            if (not (u == "Start")) and self._graph.nodes(data='step')[v] == step:
                has_successor = False
                for u_dot, v_dot in self._graph.edges():
                    if u_dot == v and self._graph.nodes(data='step')[v_dot] == step:
                        has_successor = True
                if not has_successor:
                    return v
