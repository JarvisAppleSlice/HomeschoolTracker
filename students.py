import streamlit as st

def add_student(name):
   
    st.session_state.students.append(name)