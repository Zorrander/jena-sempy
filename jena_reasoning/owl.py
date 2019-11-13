from rdflib.graph import Graph
import jena_com.queries as qry

class Knowledge:

    def __init__(self, ip="127.0.0.1", port="3030", format="n3"):
        self.g = Graph()
        self.g.parse("http://"+ip+":"+port+"/Panda/get", format=format)

    def fetch_all(self):
        query = qry.select_all()
        #for row in self.g.query(query):
        #    print(row)
        return self.g.query(query)
