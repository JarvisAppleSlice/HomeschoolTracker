import random
from datetime import date, timedelta
from uuid import uuid4

def generate_test_lessons(students, subjects, count = 100):

    lessons = []

    for _ in range(count):
        lesson = {
            'Id': uuid4(),
            'Student': random.choice(students),
            'Subject': random.choice(subjects),
            'Time': random.choice(range(15, 241, 15)),
            'Date': date.today() - timedelta(days=random.choice(range(0, 61))),
        } 
        lessons.append(lesson)

    return lessons   