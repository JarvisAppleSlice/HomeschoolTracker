import streamlit as st
from datetime import date
from state import initialize_session_state
from utilities import format_time

initialize_session_state()

with st.sidebar:
    
    st.title('Report Session')    
   
    with st.form('session_form'):
        
          student = st.selectbox(
            'Student:',
            st.session_state.students
            )
        
          subject = st.selectbox(
            'Subject:',
            st.session_state.subjects
            )

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
    
    time_display = format_time(time)

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