import streamlit as st
import pandas as pd
from Views import View
import time

class ManterFabricanteUI:
    def main():
        st.header("Cadastro de Fabricantes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterFabricanteUI.listar()
        with tab2: ManterFabricanteUI.inserir()
        with tab3: ManterFabricanteUI.atualizar()
        with tab4: ManterFabricanteUI.excluir()

    def listar():
        fabricantes = View.fabricante_listar()
        if len(fabricantes) == 0: 
            st.write("Nenhuma fabricante cadastrada")
        else:    
            dic = []
            for obj in fabricantes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome da fabricante")
        email = st.text_input("Informe o email")
        fone = st.text_input("Informe o telefone para contato")
        if st.button("Inserir"):
            View.fabricante_inserir(nome, email, fone)
            st.success("Fabricante inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        fabricantes = View.fabricante_listar()
        if len(fabricantes) == 0: 
            st.write("Nenhuma fabricante cadastrada")
        else:
            op = st.selectbox("Atualização de fabricante", fabricantes)
            nome = st.text_input("Informe o novo nome da fabricante", op.nome)
            email = st.text_input("Informe o novo email", op.email)
            fone = st.text_input("Informe o novo telefone para contato", str(op.fone))
            if st.button("Atualizar"):
                View.fabricante_atualizar(op.id, nome, email, fone)
                st.success("Fabricante atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        fabricantes = View.fabricante_listar()
        if len(fabricantes) == 0: 
            st.write("Nenhuma fabricante cadastrada")
        else:
            op = st.selectbox("Exclusão de fabricante", fabricantes)
            if st.button("Excluir"):
                View.fabricante_excluir(op.id)
                st.success("Fabricante excluída com sucesso")
                time.sleep(2)
                st.rerun()
