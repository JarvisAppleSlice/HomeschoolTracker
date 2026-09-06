import streamlit as st
from datetime import date


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
            max_value=240,
            step=15
            )
          lesson_date = st.date_input(
              'Date:',
              value=date.today()
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
         'Date': lesson_date,
    })
    st.write(f'Student: {student}')
    st.write(f'Subject: {subject}')
    st.write(f'Time Spent: {time_display}')
    st.write(f'Date: {lesson_date}')