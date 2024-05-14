import random
from typing import Dict, List, Tuple
from experta import *

from fact_data import get_maintainance_questions, get_starting_question
from chat import Chat
from model import Bicycle, BicycleMaintainance

starting_question = get_starting_question()
maintainance_questions = get_maintainance_questions()


chat = Chat("Bicycle service chat")


class BicycleEngine(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="start")

    @Rule(Fact(action="start"))
    def initialize_conversation(self):
        bike_works: Fact = chat.ask_question_dict(
            starting_question[0], starting_question[1]
        )
        self.declare(bike_works)

    @Rule(Bicycle(works=False))
    def ask_basic_problem(self):
        pass

    @Rule(Bicycle(works=True))
    def ask_maintainance_tip(self):
        maintainanace: Fact = chat.ask_question_dict(
            maintainance_questions[0], maintainance_questions[1]
        )
        self.declare(maintainanace)

    @Rule(BicycleMaintainance(when=MATCH.w, what=MATCH.t))
    def show_maintainance_tip(self, w, t):
        print(f'Tips for "{w}" bike maintainanace')
        for tip in t:
            print(f"- {tip}")


engine = BicycleEngine()

while True:
    print("\nStarting experta engine")
    engine.reset()
    engine.run()
    input("Press enter to start new conversation")
    print("\n" * 10)
