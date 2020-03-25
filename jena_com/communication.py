from SPARQLWrapper import SPARQLWrapper, JSON, POST, TURTLE, XML
from more_itertools import grouper

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

    @staticmethod
    def concatenate_prefix(query):
        return """
            PREFIX cogrob: <http://onto-server-tuni.herokuapp.com/Panda#>
            PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl:  <http://www.w3.org/2002/07/owl#>
            PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>
        """ + query


    def generate_instance_uri(self, class_name):
        query = """
            SELECT ?s
            WHERE {
                ?s rdf:type cogrob:"""+class_name+""" .
            }
        """
        instances = self.select_operation(query)
        index = max([inst['s']['value'][-1] for inst in instances]) if instances else -1
        index = str(int(index)+1)
        return "cogrob:"+ class_name[0].lower() + class_name[1:]+"Ind"+index

    def create_instance(self, class_name):
        subject = self.generate_instance_uri(class_name)
        predicate = "rdf:type"
        object = "cogrob:" + class_name
        query = """
            INSERT DATA {
                """ + subject + """ """ + predicate + """ """ + object + """
            }"""
        return self.update_operation(query)

    def select_operation(self, query):
        ''' Returns variables bound in a query pattern match '''
        try:
            self.query_sparql_store.setReturnFormat(JSON)
            self.query_sparql_store.setQuery(self.concatenate_prefix(query))
            dict_result = self.query_sparql_store.query().convert()
            return [x for x in dict_result["results"]["bindings"]]
        except:
            print("Could not complete {}".format(query))

    def update_operation(self, query):
        ''' DELETE or INSERT operations '''
        try:
            self.update_sparql_store.setMethod(POST)
            self.update_sparql_store.setQuery(self.concatenate_prefix(query))
            results = self.update_sparql_store.query()
            #return results.response.read()
            return True
        except:
            print("Could not complete UPDATE operation")

    def ask_operation(self, query):
        ''' Returns a boolean indicating whether a query pattern matches or not. '''
        try:
            self.query_sparql_store.setReturnFormat(JSON)
            self.query_sparql_store.setQuery(self.concatenate_prefix(query))
            dict_result = self.query_sparql_store.query().convert()
            return dict_result['boolean']
        except Exception as e:
            print("Could not complete ASK operation")

    def describe_operation(self, query):
        '''  Returns an RDF graph that describes the resources found. '''
        try:
            self.query_sparql_store.setReturnFormat(XML)
            self.query_sparql_store.setQuery(self.concatenate_prefix(query))
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
