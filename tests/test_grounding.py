from unittest import TestCase
from jena_reasoning.owl import Knowledge
import jena_com.queries as qry

class TestGrounding(TestCase):

    def test_understand_request(self):
        reasoner = Knowledge()
        test = reasoner.query(qry.select_skill("Make", "cranfield"))
        self.assertTrue(test == "Cranfield_Assembly")

    def test_misunderstand_action(self):
        pass

    def test_misunderstand_target(self):
        pass

    def test_grouding_action(self):
        pass

    def test_grouding_target(self):
        pass
