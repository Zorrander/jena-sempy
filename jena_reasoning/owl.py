import json
from rdflib import URIRef, BNode, Literal, Namespace, RDF
from jena_com.communication import Server

class Knowledge:

    def __init__(self):
        self.cogtuni_ns = Namespace("http://cognitive.robotics.tut#")
        self.server = Server()
        self.shape_property = self.cogtuni_ns["hasShape"]
        self.size_property  = self.cogtuni_ns["hasSize"]
        self.link_property  = self.cogtuni_ns["isLinkedTo"]

        self.size_values  = [self.cogtuni_ns["big"], self.cogtuni_ns["small"]]
        self.shape_values = [self.cogtuni_ns["circle"], self.cogtuni_ns["square"]]

    def add_object(self, json_data):
        ''' Receives JSON data from the webapp and translate in terms of rdf triples as an assembly part. '''
        list_triples = []
        parsed_json = (json.loads(json_data))
        for object in parsed_json["parts"]:
            object_name = object["name"]
            for key, value in object.items():
                if key != "name":
                        key_ns = self.server.find_namespace(key)
                        value_ns = self.server.find_namespace(value)
                        key_ns = Namespace(key_ns+"#") if key_ns else self.cogtuni_ns
                        value_ns = Namespace(value_ns+"#") if value_ns else self.cogtuni_ns
                        list_triples.append( (self.cogtuni_ns[object_name], key_ns[key], value_ns[value]) )
        return list_triples

    def deduce_step(self):
        ''' Given a list of parts and links, isolate independant groups of tasks. '''
        pass

    def deduce_constraints(self):
        '''  Given a list of parts and links, identifies a sequence order. '''
        pass

    def deduce_task(self):
        ''' Given a list of parts and links, identifies within step the different phases of the assembly '''
        pass

    def assembly_by_disassembly(self):
        ''' Given a list of parts and links, generates a complete XML file enabling planning later on. '''
        pass
