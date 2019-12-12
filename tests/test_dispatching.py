from unittest import TestCase
from jena_models.planner import Planner
from jena_models.policies import Policy
from jena_models.dispatcher import Dispatcher

class TestDispatching(TestCase):

    def test_run_dispatch(self):
        policy = Policy()
        planner = Planner(policy)
        dispatcher = Dispatcher(planner)

        msg = {'data':"Cranfield_Assembly"}
        planner.create_plan(msg)
        # Create plan
        print(planner.set_of_differences.valid_assignments)
        print("RUN DISPATCHER")
        dispatcher.run()
        # Run dispatching
        self.assertTrue(False)
