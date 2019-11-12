from unittest import TestCase
from jena_reasoning.owl import Knowledge

class TestFetchAll(TestCase):

    def test_is_communicating(self):
        reasoner = Knowledge()
        test = reasoner.fetch_all()
        self.assertTrue(len(test) == 25)
