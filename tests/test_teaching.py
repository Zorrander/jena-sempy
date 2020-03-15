from unittest import TestCase
from jena_reasoning.owl import Knowledge
from ..jena_com import queries as qry
from rdflib import Literal, RDF

'''
filename = raw_input("Enter a file name to save the plan: ")
d = json_graph.node_link_data(self._graph)  # node-link format to serialize
# write json
file = open(filename, "w+")
json.dump(d, file)
'''

json_data = '''{
    "parts": [
        {
          "name": "Pendulum",
          "type": "Peg",
          "hasShape": "circle",
          "hasSize": "",
          "isLinkedTo": "PendulumHead"
        },
        {
          "name": "PendulumHead",
          "type": "Hole",
          "hasShape": "circle",
          "hasSize": "",
          "isLinkedTo": "Pendulum"
        }]
}'''


class TestTeaching(TestCase):

    def test_add_object(self):
        ''' Translate JSON data in terms of rdf triples as an assembly part '''
        reasoner = Knowledge()

        uri_peg           = reasoner.cogtuni_ns["Peg"]
        uri_hole          = reasoner.cogtuni_ns["Hole"]
        uri_pendulum      = reasoner.cogtuni_ns["Pendulum"]
        uri_pendulum_head = reasoner.cogtuni_ns["PendulumHead"]

        pendulum_triples      = [ (uri_pendulum, RDF.type , uri_peg), (uri_pendulum, reasoner.shape_property, reasoner.shape_values[0]), (uri_pendulum, reasoner.size_property , reasoner.cogtuni_ns[""]), (uri_pendulum, reasoner.link_property , uri_pendulum_head) ]
        pendulum_head_triples = [ (uri_pendulum_head, RDF.type, uri_hole), (uri_pendulum_head, reasoner.shape_property, reasoner.shape_values[0]), (uri_pendulum_head, reasoner.size_property, reasoner.cogtuni_ns[""]), (uri_pendulum_head, reasoner.link_property , uri_pendulum) ]
        list_triples = reasoner.add_object(json_data)
        test = True if sorted(pendulum_triples + pendulum_head_triples) == sorted(list_triples) else False
        self.assertTrue(test == True)
