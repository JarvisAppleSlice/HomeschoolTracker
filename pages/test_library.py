# Testing purposes. Generating Lessons library. #

import streamlit as st
from test_lessons import generate_test_lessons
from state import initialize_session_state

initialize_session_state()


if st.button('Load Test Data'):
    test_lessons = generate_test_lessons(st.session_state.students, st.session_state.subjects)

    st.session_state.sessions.extend(test_lessons)