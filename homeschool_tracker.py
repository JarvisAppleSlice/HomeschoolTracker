import pandas as pd
# import numpy as np
import plotly.express as px
import streamlit as st


if 'sessions' not in st.session_state:
     
     st.session_state.sessions = []

with st.sidebar:
    
    st.title('Report Session')    
   
    with st.form('session_form'):
        
          student = st.selectbox(
            'Student:',
            ('Allen', 'Rafael', 'Chance'))
        
          subject = st.selectbox(
            'Subject:',
            ('Math', 'Reading', 'Writing', 'Science', 'History', 'Typing', 'Geography'))

          time = st.slider(
            'Time Spent:',
            min_value=15,
            max_value=480,
            step=15
            )
          
          submitted = st.form_submit_button('Record Session')


if submitted:
    
    if time < 60:
     time_display = f'{time} min'
    else:
     hrs = time // 60
     mins = time % 60

     if mins == 0 and hrs == 1:
          time_display = f'{hrs} hr'
     elif mins == 0:
          time_display = f'{hrs} hrs'    
     elif hrs > 1:
          time_display = f'{hrs} hrs {mins} mins'
     else:
          time_display = f'{hrs} hr {mins} mins'    

    st.session_state.sessions.append({
         'Student': student,
         'Subject': subject,
         'Time': time,
    })
    st.write(f'Student: {student}')
    st.write(f'Subject: {subject}')
    st.write(f'Time Spent: {time_display}')

if len(st.session_state.sessions) > 0:
    df = pd.DataFrame(st.session_state.sessions)
    st.dataframe(df)

    subject_totals = df.groupby('Subject')['Time'].sum()

    session_count = df.groupby('Student').sum()

    st.write(session_count)

    st.write(subject_totals)

    fig = px.pie(
        subject_totals,
        values=subject_totals.values,
        names=subject_totals.index
    )
    st.plotly_chart(fig)