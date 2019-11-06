"""
Wrap around the rdflib libraries. Introduce the concepts around agents to offer
perpective taking skills and other higher level reasoning abilities.
"""
import rdflib

class Reasoner(object):

    _robot_ctx = Namespace("http://cognitive.robotics.tut/franka#")

    def __init__(self, knowledge_store, planning_policy):
        pass

    def create_skill(self, skill_name, action, target, dictionary):
        pass

    def find_skills(self):
        pass

    def fetch_skill(self, name):
        pass

    def process(self, query):
        pass

    def answer(self, message):
        pass

    def answer_command(self, msg):
        pass

    def does_understand(self, action, target):
        pass

    #############
    def add_triple(self, triple):
        pass

    def remove_triple(self, triple):
        pass
