from unittest import TestCase
from jena_com.communication import FusekiServer

class TestCommunication(TestCase):

    def test_select(self):
        ontology_server = FusekiServer()
        results = ontology_server.select_operation("""
            PREFIX ns: <http://www.example.org/ns#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT *
            WHERE {
                ?s rdf:type ns:Person .
            }
        """)
        result = True
        persons = [
            "http://www.example.org/ns#Don_Quijote",
            "http://www.example.org/ns#Rocinante",
            "http://www.example.org/ns#Sancho",
            "http://www.example.org/ns#Dulcinea"
        ]
        for triple in results:
            if not triple["s"]["value"] in persons:
                result=False
        self.assertTrue(result)

    def test_ask(self):
        ontology_server = FusekiServer()
        results = ontology_server.ask_operation("""
            PREFIX ns: <http://www.example.org/ns#>
            ASK {
              ns:Don_Quijote ns:knows ?o
            }
        """)
        self.assertTrue(results)

    def test_describe(self):
        ontology_server = FusekiServer()
        results = ontology_server.describe_operation("""
            PREFIX ns: <http://www.example.org/ns#>
            DESCRIBE ?x
            WHERE {
                ?x ns:knows ?o .
            }
        """)
        self.assertTrue(len(results)==12 or len(results)==19)

    def test_update(self):
        ontology_server = FusekiServer()
        ontology_server.update_operation("""
            PREFIX ns: <http://www.example.org/ns#>
            INSERT DATA {
                ns:Don_Quijote ns:knows ns:Rocinante .
            }
        """)
        result = ontology_server.ask_operation("""
            PREFIX ns: <http://www.example.org/ns#>
            ASK {
              ns:Don_Quijote ns:knows ns:Rocinante .
            }
        """)
        self.assertTrue(result)
