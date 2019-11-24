from jena_models.stn import SimpleTemporalNetwork

class BaseSolution(SimpleTemporalNetwork):
    def __init__(self):
        super(BaseSolution, self).__init__()

    def _relax_network(self, stn):
        """ Relax the temporal constraints.

        The disjunctive constraints can be combined by taking only the lower and upper bounds.
        """
        self._graph = copy.deepcopy(stn._graph)
        for u, v, weight in tqdm(self._graph.edges(data='temporal_constraint')):
            if not u=="Start":
                human_expectations = weight[0]
                robot_expectations = weight[1]
                self.set_relation(u, v, 'temporal_constraint', (min(human_expectations[0], robot_expectations[0]), max(human_expectations[1], robot_expectations[1])))

    def _transform_dispatchable_graph(self, method="apsp"):
        """ Compute the Base Solution.

        The Base Solution consists in a dispatchable graph.
        One-step propagation makes explicit all constraints on neighboring events.
        """
        if method == "apsp":
            print("Construct distance graph:")
            self.construct_distance_graph()
            print("Writing resulting graph into dist.graphml")
            self.print_graph()
            nx.write_graphml(self._graph, "dist.graphml")
            print("Calculating the APSP form of the graph:")
            self._all_pairs_shortest_paths()
            print("Writing resulting graph into apsp.graphml")
            nx.write_graphml(self._graph, "apsp.graphml")
            print("Removing dominated edges:")
            self._prune_redundant_constraints()
        elif method == "chordal":
            pass
