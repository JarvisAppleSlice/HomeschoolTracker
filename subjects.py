import streamlit as st

def add_subject(name):

    st.session_state.subjects.append(name)