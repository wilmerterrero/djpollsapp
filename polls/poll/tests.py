from django.test import TestCase
from .models import Question


class QuestionTestCase(TestCase):
    fixtures = ['questions', 'choices']

    def test_retrieve_question(self):
        question = Question.objects.first()

        response = self.client.get(f'/polls/api/{question.id}')

        self.assertEqual(response.status_code, 200)

        response_json = response.json()

        self.assertIsInstance(response_json, dict)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('question_text'), str)
