from SPARQLWrapper import SPARQLWrapper, JSON, POST, TURTLE
from more_itertools import grouper
from . import queries as qry

'''
modifiers= [
    'order',       # put the solutions in order
    'projection',  # choose certain variables
    'distinct',    # ensure solutions in the sequence are unique
    'reduced',     # permit elimination of some non-unique solutions
    'offset',      # control where the solutions start from in the overall sequence of solutions
    'limit'        # restrict the number of solutions
]
'''

class FusekiServer:
    def __init__(self, host="onto-server-tuni.herokuapp.com", dataset="Panda"):
        self.query_sparql_store = SPARQLWrapper("http://"+host+"/"+ dataset +"/sparql")  # serviceQuery
        self.update_sparql_store = SPARQLWrapper("http://"+host+"/"+ dataset +"/update")  # updateQuery


    def select_operation(self, query):
        ''' Returns variables bound in a query pattern match '''
        try:
            self.query_sparql_store.setReturnFormat(JSON)
            self.query_sparql_store.setQuery(query)
            dict_result = self.query_sparql_store.query().convert()
            return [x for x in dict_result["results"]["bindings"]]
        except:
            print("Could not complete SELECT operation")

    def update_operation(self, query):
        ''' DELETE or INSERT operations '''
        try:
            self.update_sparql_store.setMethod(POST)
            self.update_sparql_store.setQuery(query)
            self.update_sparql_store.query()
            # return results.response.read()
        except:
            print("Could not complete UPDATE operation")

    def ask_operation(self, query):
        ''' Returns a boolean indicating whether a query pattern matches or not. '''
        try:
            self.query_sparql_store.setReturnFormat(JSON)
            self.query_sparql_store.setQuery(query)
            dict_result = self.query_sparql_store.query().convert()
            return dict_result['boolean']
        except Exception as e:
            print("Could not complete ASK operation")

    def describe_operation(self, query):
        '''  Returns an RDF graph that describes the resources found. '''
        try:
            self.query_sparql_store.setQuery(query)
            results = self.query_sparql_store.query().convert()
            str_result = results.serialize(format='nt')
            uris = str_result.split(' ')
            clean_uris = [x if not x[0]=='.' else x[2:] for x in uris]
            return list(grouper(3, clean_uris))[:-1]
        except Exception as e:
            print("Could not complete DESCRIBE operation")

    def construct_operation(self, query):
        ''' Returns an RDF graph constructed by substituting variables in a set of triple templates. '''
        pass
