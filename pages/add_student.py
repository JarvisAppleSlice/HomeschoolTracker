import streamlit as st
from students import add_student
from state import initialize_session_state

initialize_session_state()

with st.form('student_form'):

    st.title('Add Student')

    student = st.text_input('Student:')

    submitted = st.form_submit_button('Add')

    if submitted:

        add_student(student)