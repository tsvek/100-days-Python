import html
import requests

from key import deepl

class QuizBrain:

    def __init__(self) -> None:
        self.current = None
        self.score = 0
        self.question_number = 0

    def get_new_question(self):
        """Get new question with answer"""
        url = "https://opentdb.com/api.php"

        params = {
            'amount': 1,
            'category':9,
            'type':'boolean'
        }

        respons = requests.get(url=url, params=params)
        respons.raise_for_status()
        question = html.unescape(respons.json()['results'][0]['question'])
        answer = respons.json()['results'][0]['correct_answer']
        self.current = [question, answer]

    def check_answer(self, user) -> bool:
        correct = False
        if user == self.current[1]:
            self.score += 1
            correct = True
        self.question_number += 1
        return correct

    def get_translate(self) -> str:
        """Translates fact into Ukrainian(special for my wife=))."""
        url = "http://api-free.deepl.com/v2/translate"
        headers = {
            'Authorization': f'DeepL-Auth-Key {deepl}', 
            'Content-Type': 'application/json'
        }
        params = {
            'text': self.current[0],
            'target_lang': "UK"
        }
        response = requests.get(url=url, headers=headers, params=params)
        new = response.json()['translations'][0]['text']
        self.current.append(new)