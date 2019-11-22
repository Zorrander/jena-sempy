from unittest import TestCase
from jena_reasoning.owl import Knowledge
import jena_com.queries as qry
from rdflib import URIRef, BNode, Literal, Namespace, RDF

cogtuni = Namespace("http://cognitive.robotics.tut#")

json_data = {
    "parts": [
        {
          "name": "Pendulum",
          "type": "Peg",
          "hasShape": "Circle",
          "hasSize": "",
          "isLinkedTo": "PendulumHead"
        },
        {
          "name": "PendulumHead",
          "type": "Hole",
          "hasShape": "Circle",
          "hasSize": "",
          "isLinkedTo": "Pendulum"
        }]
}

uri_peg           = cogtuni["Peg"]
uri_hole          = cogtuni["Hole"]
uri_pendulum      = cogtuni["Pendulum"]
uri_pendulum_head = cogtuni["PendulumHead"]

shape_property = cogtuni["hasShape"]
size_property  = cogtuni["hasSize"]
link_property  = cogtuni["isLinkedTo"]

size_values  = [cogtuni["big"], cogtuni["small"]]
shape_values = [cogtuni["circle"], cogtuni["square"]]

pendulum_triples      = [ (uri_pendulum, RDF.type , uri_peg), (uri_pendulum, shape_property, shape_values[0]), (uri_pendulum, size_property , Literal()), (uri_pendulum, link_property , uri_pendulum_head) ]
pendulum_head_triples = [ (uri_pendulum_head, RDF.type, uri_hole), (uri_pendulum_head, shape_property, shape_values[1]), (uri_pendulum_head, size_property, Literal()), (uri_pendulum_head, link_property , uri_pendulum) ]

class TestTeaching(TestCase):

    def test_add_object(self):
        ''' Receives JSON data from the webapp and translate in terms of rdf triples as an assembly part. '''
        reasoner = Knowledge()
        list_triples = reasoner.add_object(json_data)
        test = True if pendulum_triples + pendulum_head_triples == list_triples else False
        self.assertTrue(test == True)
