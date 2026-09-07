import random
from datetime import date, timedelta

students = ['Allen', 'Rafael', 'Chance']

subjects = ['Math', 'Reading', 'Writing', 'Science', 'History', 'Typing', 'Geography', 'Art',]

def generate_test_lessons(count = 100):

    lessons = []

    for _ in range(count):
        lesson = {
            'Student': random.choice(students),
            'Subject': random.choice(subjects),
            'Time': random.choice(range(15, 241, 15)),
            'Date': date.today() - timedelta(days=random.choice(range(0, 61))),
        } 
        lessons.append(lesson)

    return lessons   