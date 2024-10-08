import streamlit as st


def login():
    e_mail = st.text_input("e-mail")
    senha = st.text_input("senha", type="password")
    result = st.button("entrar", key="login")
    if e_mail and senha and result:
        user = st.session_state.user_manager.login(e_mail, senha)
        st.session_state.user = user
        st.rerun()


def logout():
    st.session_state.user = None
    st.rerun()

def change_password():
    st.title(f"Change password")
    senha1 = st.text_input("nova senha", type="password")
    senha2 = st.text_input("repita a senha", type="password")
    if senha1 and senha2 and senha1 == senha2:
        st.session_state.user.password = st.session_state.user_manager.get_hash(senha1)
        st.session_state.user_manager.update_user(st.session_state.user)
        st.session_state.user = st.session_state.user_manager.get_user(st.session_state.user.email)

def logged_in():
    if st.session_state.user is not None:
        if st.session_state.user_manager.verify_password(st.session_state.user, "123456"):
            change_password()
        if st.button("sair"):
            logout()
        if st.button("mudar senha"):
            change_password()
