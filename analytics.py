def data_analytics(df):

    lesson_total = len(df)

    time_total_subjects = df['Time'].sum()

    lesson_total_per_subject = df.groupby('Subject').size()

    subject_totals = df.groupby('Subject')['Time'].sum()
    time_totals = subject_totals / 60

    time_total_student = df.groupby('Student')['Time'].sum()

    time_student_subject = df.groupby(['Student', 'Subject'])['Time'].sum()   
    time_student_subject_hours = time_student_subject / 60

    average_time_per_lesson = round(df['Time'].sum() / lesson_total)

    average_lesson_time_per_subject = round(df.groupby('Subject')['Time'].mean())

    return {
        'lesson_total': lesson_total,
        'time_total_subjects': time_total_subjects,
        'lesson_total_per_subject': lesson_total_per_subject,
        'subject_totals': subject_totals,
        'time_totals': time_totals,
        'time_total_student': time_total_student,
        'time_student_subject': time_student_subject,
        'time_student_subject_hours': time_student_subject_hours,
        'average_time_per_lesson': average_time_per_lesson,
        'average_lesson_time_per_subject': average_lesson_time_per_subject,
    }