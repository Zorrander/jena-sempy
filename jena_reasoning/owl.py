import jena_com.queries as qry
from jena_com.communication import Server

class Knowledge:

    def __init__(self):
        self.store = Server()

    def fetch_all(self):
        query = qry.select_all()
        return self.store.send(query)['results']['bindings']
