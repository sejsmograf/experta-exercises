from typing import List, Dict, Any
from fuzzywuzzy import fuzz, process


class Chat:
    def __init__(self, name: str):
        self.name = name
        self.say_hello()

    def say_hello(self):
        print(f"Hello, my name is {self.name} and i can help you with you bicycle")

    def ask_question(self, question: str, expected_answers: List[str]) -> str:
        print(f"\n\n\n\n\n\n\n{question}: ")
        for ans in expected_answers:
            print(f"- {ans}")
        answer = input("\n$ ")

        max_similiarity = 0
        matched_answer = expected_answers[0]

        for expected_answer in expected_answers:
            similarity = fuzz.token_sort_ratio(answer.lower(), expected_answer)

            if similarity > max_similiarity:
                max_similiarity = similarity
                matched_answer = expected_answer

        return matched_answer

    def ask_question_dict(self, question: str, answers_dict: Dict[str, Any]) -> Any:
        user_answer: str = self.ask_question(
            question, [ans for ans in answers_dict.keys()]
        )

        return answers_dict[user_answer]
