# Dashboard page. Showing diagrams and information for the graphs. #

import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date
from state import initialize_session_state
from utilities import format_time
from analytics import data_analytics

initialize_session_state()

if len(st.session_state.sessions) > 0:
    df = pd.DataFrame(st.session_state.sessions)

    analytics = data_analytics(df)

    st.write(analytics['time_total_student'])

    st.write(analytics['subject_totals'])

    st.write(f"Total Lessons: {analytics['lesson_total']}")

    st.write(f"The total Time spent across all subjects is {format_time(analytics['time_total_subjects'])}")

    st.write(f"An average lesson takes "
             f"{format_time(analytics['average_time_per_lesson'])}"
             )

# Pie chart showing % of total time per subject in overall lessons recorded.

    fig = px.pie(
        analytics['subject_totals'],
        values=analytics['subject_totals'].values,
        names=analytics['subject_totals'].index
    )

    st.plotly_chart(fig)

# Bar chart showing # of lessons and time spent total.

    bar_df = pd.DataFrame({
        'Subject': analytics['lesson_total_per_subject'].index,
        'Lessons': analytics['lesson_total_per_subject'].values,
        'Time in Hours': analytics['time_totals'].values,        
    })

    fig = px.bar(
        bar_df,
        x='Subject',
        y=['Lessons', 'Time in Hours'],
        barmode='group',
        title='Lessons vs. Time by Subject'
    )

    st.plotly_chart(fig)

#bar chart showing the average time per lesson organized by subject

    bar_df = pd.DataFrame({
        'Subject': analytics['average_lesson_time_per_subject'].index,
        'Average Minutes': analytics['average_lesson_time_per_subject'].values,      
    })

    fig = px.bar(
        bar_df,
        x='Subject',
        y='Average Minutes',
        title='Average Lesson Time by Subject'
    )

    st.plotly_chart(fig)

    #bar chart showing time per student for each student

    bar_df = analytics['time_student_subject_hours'].reset_index()

    fig = px.bar(
        bar_df,
        x='Time', 
        y= 'Student',
        color='Subject',
        barmode='group',
        title='Total time for each student in Hours'
    )

    st.plotly_chart(fig)

    #pie chart showing time per student for each student

    bar_df = analytics['time_student_subject_hours'].reset_index()

    fig = px.pie(
        bar_df,
        values='Time',
        names='Subject',
        facet_col='Student',
        facet_col_spacing=.05,
        facet_col_wrap=2,
        facet_row_spacing=.3
    )

    st.plotly_chart(fig)