from unittest import TestCase

from jena_models.base_solution import BaseSolution
from jena_models.set_of_differences import SetOfDifferences
from jena_models.update_rules import dynamic_backpropagation_rule_I, dynamic_backpropagation_rule_II

class TestPlanning(TestCase):

    def test_model_network(self):
        b_s = BaseSolution()
        self.assertTrue(False)

    def test_relax_network(self):
        b_s = BaseSolution()
        self.assertTrue(False)

    def test_transform_dispatchable_graph(self):
        b_s = BaseSolution()
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
