from unittest import TestCase
from jena_reasoning.owl import Knowledge
import jena_com.queries as qry
from rdflib import URIRef, BNode, Literal, Namespace, RDF

cogtuni = Namespace("http://cognitive.robotics.tut#")

class TestReasoning(TestCase):

    def test_reason(self):
        pass
