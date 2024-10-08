import streamlit as st

from reviewer.webapp.session import add_user_to_session
from reviewer.webapp.auth import login, logged_in


add_user_to_session(st.session_state)


print("state", st.session_state.user)
if st.session_state.user is not None:
    st.title(f"Hello, {st.session_state.user.email}")
    logged_in()

else:
    st.write("# Bem vido ao Vlibras reviewer")
    login()