from unittest import TestCase
from jena_reasoning.owl import Knowledge

class TestReasoning(TestCase):

    def test_is_communicating(self):
        reasoner = Knowledge()
        test = reasoner.fetch_all()
        self.assertTrue(len(test) == 25)

    def test_find_subject(self):
        pass

    def test_find_predicate(self):
        pass

    def test_find_object(self):
        pass

    def test_understand_request(self):
        pass
