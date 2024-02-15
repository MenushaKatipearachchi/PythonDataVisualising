import pandas as pd
from hello.models import School, Student, Subject, AssessmentAreas, Awards, Class, Answers, Summary

def populate_db():
    # Read the CSV files
    df1 = pd.read_csv('Ganison_dataset/Ganison_dataset_1.csv', nrows=1000)
    df2 = pd.read_csv('Ganison_dataset/Ganison_dataset_2.csv', nrows=1000)
    df3 = pd.read_csv('Ganison_dataset/Ganison_dataset_3.csv', nrows=1000)
    df4 = pd.read_csv('Ganison_dataset/Ganison_dataset_4.csv', nrows=1000)
    df5 = pd.read_csv('Ganison_dataset/Ganison_dataset_5.csv', nrows=1000)
    df6 = pd.read_csv('Ganison_dataset/Ganison_dataset_6.csv', nrows=1000)

    # Concatenate all dataframes into one
    df = pd.concat([df1, df2, df3, df4, df5, df6])

    # Create dictionaries to store the unique objects
    schools = {}
    assessment_areas = {}
    awards = {}
    classes = {}
    students = {}
    subjects = {}
    answers = {}

    # Create a list to store the Summary objects
    summaries = []

    # Define the batch size
    batch_size = 1000

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Create objects only if they don't exist yet
        school_name = row['school_name']
        if school_name not in schools:
            schools[school_name] = School.objects.create(name=school_name)

        area_name = row['Assessment Areas']
        if area_name not in assessment_areas:
            assessment_areas[area_name] = AssessmentAreas.objects.create(name=area_name)

        award_name = row['award']
        if award_name not in awards:
            awards[award_name] = Awards.objects.create(name=award_name)

        class_name = row['Class']
        if class_name not in classes:
            classes[class_name] = Class.objects.create(class_name=class_name)

        student_name = row['First Name'] + ' ' + row['Last Name']
        if student_name not in students:
            students[student_name] = Student.objects.create(fullname=student_name)

        subject_name = row['Subject']
        subject_score = row['student_score']
        if (subject_name, subject_score) not in subjects:
            subjects[(subject_name, subject_score)] = Subject.objects.create(subject=subject_name, score=subject_score)

        answer_text = row['Answers']
        if answer_text not in answers:
            answers[answer_text] = Answers.objects.create(answers=answer_text)

        # Create the Summary object
        summaries.append(Summary(
            school=schools[school_name],
            sydney_participant=row['sydney_participants'],
            sydney_percentile=row['sydney_percentile'],
            assessment_area=assessment_areas[area_name],
            award=awards[award_name],
            class_id=classes[class_name],
            correct_answer_percentage_per_class=row['correct_answer_percentage_per_class'],
            correct_answer=row['Correct Answers'],
            student=students[student_name],
            participant=row['participant'],
            student_score=row['student_score'],
            subject=subjects[(subject_name, subject_score)],
            category_id=1,
            year_level_name=row['Year Level'],
            answer=answers[answer_text],
            correct_answer_id=1
        ))

        # If batch size is full, save the objects to the database
        if (index + 1) % batch_size == 0:
            Summary.objects.bulk_create(summaries)

            # Clear the lists for the next batch
            summaries.clear()

    # Save any remaining objects that didn't make up a full batch
    Summary.objects.bulk_create(summaries)
