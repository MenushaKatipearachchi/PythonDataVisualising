from django.test import TestCase
from django.urls import reverse
from hello.models import School, Student, Subject, AssessmentAreas, Awards, Class, Answers, Summary

class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up objects used by all test methods
        School.objects.create(name='Test School')
        Student.objects.create(fullname='Test Student')
        Subject.objects.create(subject='Test Subject', score=100)
        AssessmentAreas.objects.create(name='Test Assessment Area')
        Awards.objects.create(name='Test Award')
        Class.objects.create(class_name='Test Class')
        Answers.objects.create(answers='Test Answer')

        Summary.objects.create(
            school=School.objects.get(name='Test School'),
            sydney_participant=1,
            sydney_percentile=99.9,
            assessment_area=AssessmentAreas.objects.get(name='Test Assessment Area'),
            award=Awards.objects.get(name='Test Award'),
            class_id=Class.objects.get(class_name='Test Class'),
            correct_answer_percentage_per_class=100.0,
            correct_answer='A',
            student=Student.objects.get(fullname='Test Student'),
            participant=1,
            student_score=100,
            subject=Subject.objects.get(subject='Test Subject', score=100),
            category_id=1,
            year_level_name='Year 1',
            answer=Answers.objects.get(answers='Test Answer'),
            correct_answer_id=1
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_context_data(self):
        response = self.client.get(reverse('index'))
        self.assertTrue('schools' in response.context)
        self.assertTrue('students' in response.context)
        self.assertTrue('subjects' in response.context)
        self.assertTrue('assessment_areas' in response.context)
        self.assertTrue('awards' in response.context)
        self.assertTrue('classes' in response.context)
        self.assertTrue('answers' in response.context)
        self.assertTrue('summaries' in response.context)
