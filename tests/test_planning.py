from unittest import TestCase
import os
from jena_models.base_solution import BaseSolution
from jena_models.set_of_differences import SetOfDifferences
from jena_models.policies import Policy
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

    def test_policy_evaluate(self):
        b_s = BaseSolution()
        policy = Policy()
        # Create plan
        b_s.model_temporal_problem("Cranfield_Assembly")
        b_s.relax_network()
        b_s.construct_distance_graph()
        b_s.all_pairs_shortest_paths()
        b_s.prune_redundant_constraints()
        #
        print("Evaluating: {}".format(b_s._graph.nodes.data()))
        policy.evaluate(b_s)
        print("Policy results")
        print(policy.valid_assignments)
        print(policy.data)
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
