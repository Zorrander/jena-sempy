import rdflib
from rdflib import Namespace, URIRef
from rdflib.graph import Graph
import jena_com.queries as qry

cogtuni = Namespace("http://cognitive.robotics.tut#")
rdfs    = Namespace("http://www.w3.org/2000/01/rdf-schema#")
namespaces = dict(cogtuni=cogtuni, rdfs=rdfs)

class Server:

    def __init__(self, ip="127.0.0.1", port="3030", format="n3"):
        self.g = Graph()
        self.g.parse("http://"+ip+":"+port+"/Panda/get", format=format)

    def process_uri(self, uri):
        uri_py = uri
        if isinstance(uri_py, rdflib.term.URIRef):
            uri_py = uri.toPython()
        if "#" in uri_py:
            uri_py = uri_py.split("#")[1]
        return uri_py.encode('ascii', 'ignore')

    def process_result(self, result):
        rows = [x for x in result]
        if len(rows)==1:
            return rows[0][0].toPython().split("#")[1]
        else:
            return rows

    def query(self, query):
        SPARQLResult = self.g.query(query, initNs=namespaces)
        return self.process_result(SPARQLResult)

    def fetch_all(self):
        query = qry.select_all()
        return self.query(query)

    def create(self, subject, predicate, object):
        self.g.add( (URIRef(subject), URIRef(predicate), URIRef()) )

    def read(self, subject):
        if not "#" in subject:
            subject = cogtuni[subject]
        gen = self.g.predicate_objects(subject)
        return [ (self.process_uri(pred), self.process_uri(obj)) for pred, obj in gen ]

    def find_namespace(self, entity):
        found = False
        for triple in self.fetch_all():
            for uri_ref in triple:
                if isinstance(uri_ref, rdflib.term.URIRef) and "#" in uri_ref:
                    uri_py = uri_ref.toPython()
                    if uri_py.split("#")[1] == entity:
                        found = uri_py.split("#")[0]
                        break
                if found:
                    break
        return found
