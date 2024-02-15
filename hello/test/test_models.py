from django.test import TestCase
from hello.models import School, Student, Subject, AssessmentAreas, Awards, Class, Answers, Summary

class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(fullname='Test Student')

    def test_fullname_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('fullname').verbose_name
        self.assertEqual(field_label, 'fullname')

    def test_fullname_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('fullname').max_length
        self.assertEqual(max_length, 200)

class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Subject.objects.create(subject='Test Subject', score=100)

    def test_subject_label(self):
        subject = Subject.objects.get(id=1)
        field_label = subject._meta.get_field('subject').verbose_name
        self.assertEqual(field_label, 'subject')

    def test_subject_max_length(self):
        subject = Subject.objects.get(id=1)
        max_length = subject._meta.get_field('subject').max_length
        self.assertEqual(max_length, 200)

    def test_score_label(self):
        subject = Subject.objects.get(id=1)
        field_label = subject._meta.get_field('score').verbose_name
        self.assertEqual(field_label, 'score')

class AssessmentAreasModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        AssessmentAreas.objects.create(name='Test Assessment Area')

    def test_name_label(self):
        assessment_area = AssessmentAreas.objects.get(id=1)
        field_label = assessment_area._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        assessment_area = AssessmentAreas.objects.get(id=1)
        max_length = assessment_area._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

class AwardsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Awards.objects.create(name='Test Award')

    def test_name_label(self):
        award = Awards.objects.get(id=1)
        field_label = award._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        award = Awards.objects.get(id=1)
        max_length = award._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)
        
class ClassModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Class.objects.create(class_name='Test Class')

    def test_class_name_label(self):
        class_obj = Class.objects.get(id=1)
        field_label = class_obj._meta.get_field('class_name').verbose_name
        self.assertEqual(field_label, 'class name')

    def test_class_name_max_length(self):
        class_obj = Class.objects.get(id=1)
        max_length = class_obj._meta.get_field('class_name').max_length
        self.assertEqual(max_length, 200)

class AnswersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Answers.objects.create(answers='Test Answer')

    def test_answers_label(self):
        answer = Answers.objects.get(id=1)
        field_label = answer._meta.get_field('answers').verbose_name
        self.assertEqual(field_label, 'answers')

    def test_answers_max_length(self):
        answer = Answers.objects.get(id=1)
        max_length = answer._meta.get_field('answers').max_length
        self.assertEqual(max_length, 200)

class SummaryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        school = School.objects.create(name='Test School')
        student = Student.objects.create(fullname='Test Student')
        subject = Subject.objects.create(subject='Test Subject', score=100)
        assessment_area = AssessmentAreas.objects.create(name='Test Assessment Area')
        award = Awards.objects.create(name='Test Award')
        class_obj = Class.objects.create(class_name='Test Class')
        answer = Answers.objects.create(answers='Test Answer')

        Summary.objects.create(
            school=school,
            sydney_participant=1,
            sydney_percentile=99.9,
            assessment_area=assessment_area,
            award=award,
            class_id=class_obj,
            correct_answer_percentage_per_class=100.0,
            correct_answer='A',
            student=student,
            participant=1,
            student_score=100,
            subject=subject,
            category_id=1,
            year_level_name='Year 1',
            answer=answer,
            correct_answer_id=1
        )