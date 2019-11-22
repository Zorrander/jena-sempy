from unittest import TestCase
from jena_reasoning.owl import Knowledge
import jena_com.queries as qry
from rdflib import URIRef, BNode, Literal, Namespace, RDF

cogtuni = Namespace("http://cognitive.robotics.tut#")

class TestReasoning(TestCase):

    def test_deduce_step(self):
        ''' Given a list of parts and links, isolate independant groups of tasks. '''
        pass

    def test_deduce_constraints(self):
        '''  Given a list of parts and links, identifies a sequence order. '''

    def test_deduce_task(self):
        ''' Given a list of parts and links, identifies within step the different phases of the assembly '''
        pass

    def test_assembly_by_disassembly(self):
        ''' Given a list of parts and links, generates a complete XML file enabling planning later on. '''
        pass
