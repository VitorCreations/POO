import streamlit as st
import pandas as pd
from Views import View
import time

class MeusDadosProfissionalUI:
    def main():
        st.header("Meus Dados")
        MeusDadosProfissionalUI.atualizar()

    def atualizar():
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.nome)
        email = st.text_input("Informe o novo e-mail", op.email)
        senha = st.text_input("Informe a nova senha", op.senha, type="password")
        if st.button("Atualizar"):
            View.profissional_atualizar(op.id, nome, email, senha)
            st.success("Dados atualizados com sucesso")
            time.sleep(2)
            st.rerun()
