from unittest import TestCase
from jena_com.communication import Server

select_persons = """
    PREFIX ns: <http://www.example.org/ns#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT *
    WHERE {
        ?s rdf:type ns:Person .
    }
"""
select_someone_who_knows = """
    PREFIX ns: <http://www.example.org/ns#>
    SELECT *
    WHERE {
        ?s ns:knows ?o .
    }
"""

class TestCommunication(TestCase):

    def test_select(self):
        ontology_server = Server()
        results = ontology_server.select_operation(select_persons)
        self.assertTrue(results[0]["s"]["value"] == "http://www.example.org/ns#Don_Quijote")

    def test_update(self):
        ontology_server = Server()
        results = ontology_server.update_operation("""
            PREFIX ns: <http://www.example.org/ns#>
            INSERT DATA {
                ns:Don_Quijote ns:knows ns:Rocinante .
            }
        """)
        result = True if not results==None else False
        self.assertTrue(result)
