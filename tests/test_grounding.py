from unittest import TestCase
from ..jena_com.communication import Server
from ..jena_com import queries as qry

class TestGrounding(TestCase):

    def test_understand_request(self):
        reasoner = Server()
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
