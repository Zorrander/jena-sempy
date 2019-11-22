class Knowledge:

    def __init__(self):
        pass

    def add_object(self, json):
        ''' Receives JSON data from the webapp and translate in terms of rdf triples as an assembly part. '''
        list_triples = []

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
