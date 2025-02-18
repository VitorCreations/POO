import streamlit as st
import pandas as pd
from Views import View
import time

class MeusDadosUsuarioUI:
    def main():
        st.header("Meus Dados")
        MeusDadosUsuarioUI.atualizar()

    def atualizar():
        op = View.usuario_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.nome)
        email = st.text_input("Informe o novo e-mail", op.email)
        senha = st.text_input("Informe a nova senha", op.senha, type="password")
        if st.button("Atualizar"):
            View.cliente_atualizar(op.id, nome, email, senha)
            st.success("Dados atualizados com sucesso")
            time.sleep(2)
            st.rerun()
