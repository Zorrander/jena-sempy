from jena_models.base_solution import BaseSolution
from jena_models.set_of_differences import SetOfDifferences

class Planner(object):
    """Compile a plan.

    Converts the information retrieved from the knowledge base into a
    Multi-agent Disjunctive Temporal Constraint Network With Uncertainty
    """

    def __init__(self, policy=None):
        self.base_solution = BaseSolution()
        #self.set_of_differences = SetOfDifferences()
        self.planning_policy = policy

    def create_plan(self, task):
        """ Model a temporal plan .

        Model a plan and instantiate a dispatcher to perform the plan
        """
        self.base_solution.model_temporal_problem(task)
        self.base_solution.relax_network()
        self.base_solution.transform_dispatchable_graph()


    def apply_timestamp(self):
        # Propagate it to its immediate neighbors
        pass

    def find_next_action(self):
        ''' Pick an event TP in the graph such that current_time is in TP's time bound '''
        return self.base_solution.find_available_step(current_time)

    def perform_action(self):
        ''' Set TP's execution time to current_timeand add TP to S '''
        ''' Propagate the time of executionto its IMMEDIATE NEIGHBORS in the distancegraph '''
        ''' Put in A all events TPx such that allnegative edges starting from TPx have adestination that is already in S; '''
        pass

    def export_data(self):
        with open(os.path.join("./", self.planning_policy.name + '.csv'), mode='w') as working_times:
            data_csv = csv.writer(working_times, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for full_assignment in self.planning_policy.data:
                data_csv.writerow(full_assignment)
