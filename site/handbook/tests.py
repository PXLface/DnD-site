import datetime

from django.test import TestCase
from django.utils import timezone

from .models import *

class QuestionModelTest(TestCase):
    def test_was_published_recently_was_future_question(self):
        time = timezone.now()+datetime.timedelta(days=3)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)