from unittest import TestCase
from jena_reasoning.owl import Knowledge
import jena_com.queries as qry
from rdflib import URIRef, BNode, Literal, Namespace, RDF

cogtuni = Namespace("http://cognitive.robotics.tut#")

class TestReasoning(TestCase):

    def test_find_subject(self):
        reasoner = Knowledge()
        test = True if (cogtuni.Skill in reasoner.g.subjects()) else False
        self.assertTrue(test == True)

    def test_find_predicate(self):
        reasoner = Knowledge()
        test = True if (RDF.type in reasoner.g.predicates()) else False
        self.assertTrue(test == True)

    def test_find_object(self):
        reasoner = Knowledge()
        test = True if (cogtuni.Sensor in reasoner.g.objects()) else False
        self.assertTrue(test == True)
