import streamlit as st
from test_lessons import generate_test_lessons

if 'sessions' not in st.session_state:
     
     st.session_state.sessions = []

if st.button('Load Test Data'):
    test_lessons = generate_test_lessons()

    st.session_state.sessions.extend(test_lessons)