from unittest import TestCase
from jena_reasoning.owl import Knowledge
from rdflib import RDF, RDFS, OWL
cogtuni = "http://cognitive.robotics.tut#"

class TestCommunication(TestCase):

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

    def test_read_subject(self):
        reasoner = Knowledge()
        p_o = reasoner.read("FrankaDictionary")
        print p_o
        self.assertTrue(('type', 'NamedIndividual') in p_o)
