import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date


if 'sessions' not in st.session_state:
     
     st.session_state.sessions = []

if len(st.session_state.sessions) > 0:
    df = pd.DataFrame(st.session_state.sessions)
    st.dataframe(df)

    subject_totals = df.groupby('Subject')['Time'].sum()

    session_count = df.groupby('Student')['Time'].sum()

    lesson_count = df.groupby('Subject').size()

    time_totals = df.groupby('Subject')['Time'].sum() / 60

    st.write(session_count)

    st.write(subject_totals)

    fig = px.pie(
        subject_totals,
        values=subject_totals.values,
        names=subject_totals.index
    )
    st.plotly_chart(fig)

    bar_df = pd.DataFrame({
        'Subject': lesson_count.index,
        'Lessons': lesson_count.values,
        'Hours': time_totals.values,        
    })

    fig = px.bar(
        bar_df,
        x='Subject',
        y=['Lessons', 'Hours'],
        barmode='group',
        title='Lessons vs. Time by Subject'
    )

    st.plotly_chart(fig)