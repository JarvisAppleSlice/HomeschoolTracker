# Session state.

import streamlit as st


def initialize_session_state():
     
   if 'sessions' not in st.session_state:
     
      st.session_state.sessions = []

   if 'students' not in st.session_state:

      st.session_state.students = []
