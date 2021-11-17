from django.test import TestCase

# Create your tests here.
from modelstudy.models import School, Student


class TestModels(TestCase):

    def test_test01(self):
        school = School.objects.get(id=1)
        print(school.name)



