import streamlit as st
import pandas as pd
from Views import View
import time

class ManterVeiculoUI:
    def main():
        st.header("Cadastro de Veiculos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterVeiculoUI.listar()
        with tab2: ManterVeiculoUI.inserir()
        with tab3: ManterVeiculoUI.atualizar()
        with tab4: ManterVeiculoUI.excluir()

    def listar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0: 
            st.write("Nenhum veiculo cadastrada")
        else:    
            dic = []
            for obj in veiculos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        fabricantes = View.fabricante_listar
        nome = st.text_input("Informe o nome do veiculo")
        fabricante = st.selectbox("Informe o fabricante do veiculo", fabricantes, index = None)
        if st.button("Inserir"):
            View.veiculo_inserir(nome, fabricante.id)
            st.success("Veiculo inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0: 
            st.write("Nenhum veiculo cadastrado")
        else:
            fabricantes = View.fabricante_listar()
            op = st.selectbox("Atualização de veiculo", veiculos)
            nome = st.text_input("Informe o novo nome do veiculo", op.nome)
            id_fabricante = None if op.id_fabricante in [0, None] else op.id_fabricante
            fabricante = st.selectbox("Informe o novo fabricante", fabricantes, next((i for i, c in enumerate(fabricantes) if c.id == id_fabricante), None))
            if st.button("Atualizar"):
                View.veiculo_atualizar(op.id, nome, fabricante.id)
                st.success("Veiculo atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0: 
            st.write("Nenhum veiculo cadastrada")
        else:
            op = st.selectbox("Exclusão de veiculo", veiculos)
            if st.button("Excluir"):
                View.veiculo_excluir(op.id)
                st.success("Veiculo excluído com sucesso")
                time.sleep(2)
                st.rerun()
