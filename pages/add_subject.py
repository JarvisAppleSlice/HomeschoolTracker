import streamlit as st
from subjects import add_subject
from state import initialize_session_state

initialize_session_state()

with st.form('subject_form'):

    st.title('Add Subject')

    subject = st.text_input('Subject:')

    submitted = st.form_submit_button('Add')

    if submitted:

        add_subject(subject)