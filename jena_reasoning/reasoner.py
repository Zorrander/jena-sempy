"""
Wrap around the rdflib libraries. Introduce the concepts around agents to offer
perpective taking skills and other higher level reasoning abilities.
"""
#from rdflib import Namespace
from .nlp import _SpeechEngine
from .queries import _QueryEngine
from .planner import _Planner
from .dispatcher import _Dispatcher
from .owl import Command, StepCompleted


class _Reasoner(object):

    _robot_ctx = Namespace("http://cognitive.robotics.tut/franka#")

    def __init__(self, knowledge_store, planning_policy):
        self.query_engine = _QueryEngine(knowledge_store, self._robot_ctx)
        self.speech_engine = _SpeechEngine()
        self.planner = _Planner(planning_policy)
        self.dispatcher = _Dispatcher(self.planner)
        self.last_agent = None
        self.other_agents = {}
        self.active = True
        self.state = "Listening"
        self.id_loc= 0

    def create_skill(self, skill_name, action, target, dictionary):
        self.query_engine.serialize(skill_name, (action, target), dictionary, self._robot_ctx)

    def find_skills(self):
        skills = self.query_engine.select_skills(self._robot_ctx)
        skills.remove("Skill")
        return skills

    def fetch_skill(self, name):
        return self.query_engine.select_all_pred_obj(self._robot_ctx, name)

    def process(self, query):
        return self.query_engine.query(self._robot_ctx, query)

    def answer(self, message):
        msg = self.speech_engine.parse(message)
        if isinstance(msg, Command):
            return self.answer_command(msg)
        elif isinstance(msg, StepCompleted):
            return self.acknowledge_step_completion(msg)

    def answer_command(self, msg):
        steps, constraints = self.does_understand(msg.action, msg.target)
        if self.planner.create_plan(steps, constraints):
            self.dispatcher.start()
            return self.speech_engine.generate("Confirm")
        return self.speech_engine.generate("Error")

    def does_understand(self, action, target):
        list_steps = []
        list_constraints = []
        skill = self.query_engine.select_skill_from_coa(self._robot_ctx, action, target)
        if skill and len(skill)==1:
            steps = self.query_engine.select_steps_from_skill(self._robot_ctx, skill[0])
            for s in steps:
                task, actions, previous_step = self.query_engine.compute_step_info(self._robot_ctx, s)
                list_steps.append((s, task, actions))
                list_constraints.append((previous_step, s))
        return (list_steps,list_constraints)

    def acknowledge_step_completion(self, msg):
        self.dispatcher.update(msg.step_number)
        return self.speech_engine.generate("Acknowledge")

    #############
    def add_triple(self, triple):
        for ctx, status in self.other_agents.items():
            if status=="active":
                self.kb.get_context(ctx).add(triple)
        self.kb.get_context(self.robot_ctx).add(triple)

    def remove_triple(self, triple):
        for ctx, status in self.other_agents.items():
            if status=="active":
                self.kb.get_context(ctx).remove(triple)
        self.kb.get_context(self.robot_ctx).remove(triple)
