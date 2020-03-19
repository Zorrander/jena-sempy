from SPARQLWrapper import SPARQLWrapper, JSON, POST, DIGEST
from . import queries as qry

class Server:
    def __init__(self, host="onto-server-tuni.herokuapp.com", dataset="Panda"):
        self.query_sparql_store = SPARQLWrapper("http://"+host+"/"+ dataset +"/sparql")  # serviceQuery
        self.update_sparql_store = SPARQLWrapper("http://"+host+"/"+ dataset +"/update")  # updateQuery

    def select_operation(self, query):
        ''' SELECT query. a SPARQL Results Document in XML, JSON, or CSV/TSV format. '''
        try:
            self.query_sparql_store.setReturnFormat(JSON)
            self.query_sparql_store.setQuery(query)
            raw_result = self.query_sparql_store.query().convert()
            return [x for x in raw_result["results"]["bindings"]]
        except:
            print("Could not complete SELECT operation")

    def update_operation(self, query):
        try:
            self.update_sparql_store.setMethod(POST)
            self.update_sparql_store.setQuery(query)
            results = self.update_sparql_store.query()
            return results.response.read()
        except:
            print("Could not complete UPDATE operation")

    def ask_operation(self, sparql):
        ''' ASK query. a SPARQL Results Document in XML, JSON, or CSV/TSV format.'''
        pass

    def construct_operation(self, triples):
        ''' an RDF graph serialized, for example, in the RDF/XML syntax '''
        pass

    def describe_operation(self, data):
        '''  an RDF graph serialized, for example, in the RDF/XML syntax '''
        pass
