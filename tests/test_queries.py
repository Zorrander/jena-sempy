from unittest import TestCase
from jena_reasoning.owl import Knowledge
import jena_com.queries as qry
from rdflib import URIRef, BNode, Literal, Namespace, RDF

cogtuni = Namespace("http://cognitive.robotics.tut#")

class TestReasoning(TestCase):

    def test_is_communicating(self):
        reasoner = Knowledge()
        test = reasoner.fetch_all()
        self.assertTrue(len(test) == 25)

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

    def test_understand_request(self):
        reasoner = Knowledge()
        test = reasoner.query(qry.select_skill("Make", "cranfield"))
        self.assertTrue(test == "Cranfield_Assembly")
