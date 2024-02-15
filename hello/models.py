from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)

class AssessmentAreas(models.Model):
    name = models.CharField(max_length=200)

class Awards(models.Model):
    name = models.CharField(max_length=200)

class Class(models.Model):
    class_name = models.CharField(max_length=200)

class Student(models.Model):
    fullname = models.CharField(max_length=200)

class Subject(models.Model):
    subject = models.CharField(max_length=200)
    score = models.IntegerField()

class Answers(models.Model):
    answers = models.CharField(max_length=200)

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='summaries')
    sydney_participant = models.IntegerField()
    sydney_percentile = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE, related_name='summaries')
    award = models.ForeignKey(Awards, on_delete=models.CASCADE, related_name='summaries')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='summaries')
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=2)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='summaries')
    participant = models.IntegerField()
    student_score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='summaries')
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=200)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='summaries')
    correct_answer_id = models.IntegerField()
