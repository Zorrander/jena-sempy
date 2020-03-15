
from rdflib import Namespace
from unittest import TestCase
from ..jena_com.communication import Server
from rdflib import RDF, RDFS, OWL

cogtuni = Namespace("http://cognitive.robotics.tut#")

class TestCommunication(TestCase):

    def test_find_namespace(self):
        reasoner = Server()
        test = reasoner.find_namespace("FrankaDictionary")
        self.assertTrue(test == "http://cognitive.robotics.tut")

    def test_find_subject(self):
        reasoner = Server()
        test = True if (cogtuni.Skill in reasoner.g.subjects()) else False
        self.assertTrue(test == True)

    def test_find_predicate(self):
        reasoner = Server()
        test = True if (RDF.type in reasoner.g.predicates()) else False
        self.assertTrue(test == True)

    def test_find_object(self):
        reasoner = Server()
        test = True if (cogtuni.Sensor in reasoner.g.objects()) else False
        self.assertTrue(test == True)

    def test_read_subject(self):
        reasoner = Server()
        p_o = reasoner.read("FrankaDictionary")
        self.assertTrue(('type', 'NamedIndividual') in p_o)
