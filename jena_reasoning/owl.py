from rdflib import Namespace
from rdflib.graph import Graph
import jena_com.queries as qry

cogtuni = Namespace("http://cognitive.robotics.tut#")
rdfs    = Namespace("http://www.w3.org/2000/01/rdf-schema#")
namespaces = dict(cogtuni=cogtuni, rdfs=rdfs)

class Knowledge:

    def __init__(self, ip="127.0.0.1", port="3030", format="n3"):
        self.g = Graph()
        self.g.parse("http://"+ip+":"+port+"/Panda/get", format=format)

    def query(self, query):
        SPARQLResult = self.g.query(query, initNs=namespaces)
        rows = [x for x in SPARQLResult]
        if len(rows)==1:
            return rows[0][0].toPython().split("#")[1]
        else:
            return rows

    def fetch_all(self):
        query = qry.select_all()
        #for row in self.g.query(query):
        #    print(row)
        return self.query(query)
