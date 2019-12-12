from unittest import TestCase
import os
from jena_models.base_solution import BaseSolution
from jena_models.set_of_differences import SetOfDifferences
from jena_models.update_rules import dynamic_backpropagation_rule_I, dynamic_backpropagation_rule_II


class TestPlanning(TestCase):

    def test_model_network(self):
        b_s = BaseSolution()
        b_s.model_temporal_problem("Cranfield_Assembly")
        b_s.display_graph("test_model_network")
        self.assertTrue(False)

    def test_relax_network(self):
        b_s = BaseSolution()
        b_s.model_temporal_problem("Cranfield_Assembly")
        b_s.relax_network()
        b_s.display_graph("test_relax_network")
        self.assertTrue(False)

    def test_construct_distance_graph(self):
        b_s = BaseSolution()
        b_s.model_temporal_problem("Cranfield_Assembly")
        b_s.relax_network()
        b_s.construct_distance_graph()
        b_s.display_graph("test_construct_distance_graph")
        self.assertTrue(False)

    def test_all_pairs_shortest_paths(self):
        b_s = BaseSolution()
        b_s.model_temporal_problem("Cranfield_Assembly")
        b_s.relax_network()
        b_s.construct_distance_graph()
        b_s.all_pairs_shortest_paths()
        b_s.display_graph("test_all_pairs_shortest_paths")
        self.assertTrue(False)

    def test_prune_redundant_constraints(self):
        b_s = BaseSolution()
        b_s.model_temporal_problem("Cranfield_Assembly")
        b_s.relax_network()
        b_s.construct_distance_graph()
        b_s.all_pairs_shortest_paths()
        b_s.prune_redundant_constraints()
        b_s.display_graph("test_prune_redundant_constraints")
        self.assertTrue(False)

    def test_create_component_solution(self):
        set_dif = SetOfDifferences()
        self.assertTrue(False)

    def test_backpropagate_task_assign(self):
        set_dif = SetOfDifferences()
        self.assertTrue(False)

    def test_dbp_rule_I(self):
        temporal_constraint = False
        base_solution = False
        dbp = dynamic_backpropagation_rule_I(temporal_constraint, base_solution)
        case_1 = ""
        case_2 = ""
        case_3 = ""
        self.assertTrue(case_1 and case_2 and case_3)

    def test_dbp_rule_II(self):
        temporal_constraint = False
        base_solution = False
        dbp = dynamic_backpropagation_rule_II(temporal_constraint, base_solution)
        case_1 = ""
        case_2 = ""
        case_3 = ""
        self.assertTrue(case_1 and case_2 and case_3)


    def test_create_plan(self):
        # Make a plan.
        # Export it to a file.
        # Read the file and compare to expected output.
        b_s = BaseSolution()
        s_o_d = SetOfDifferences()
        planinng_policy = None

        b_s.model_temporal_problem("Cranfield_Assembly")
        print("Step 1 : Relax the plan")
        b_s.relax_network()
        print ("Step 2 : Compile the plan to a dispatchable form to get the Base Solution")
        b_s.transform_dispatchable_graph()
        print ("Step 3 : Compute the constraint changes for each feasible task assignments")
        s_o_d.initialize_set_of_differences(b_s, planinng_policy)
        for full_assignment in s_o_d.valid_assignments:
            constraints = [asg[0] for asg in full_assignment.task_assignments]
            temporally_consistent = s_o_d.backpropagate_task_assign(constraints, b_s, full_assignment)
            if not temporally_consistent:
                full_assignment.feasible = False

        self.assertTrue(False)
        pass
