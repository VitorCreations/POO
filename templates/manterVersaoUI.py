import streamlit as st
import pandas as pd
from Views import View
import time

class ManterVersaoUI:
    def main():
        st.header("Cadastro de Versões")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterVersaoUI.listar()
        with tab2: ManterVersaoUI.inserir()
        with tab3: ManterVersaoUI.atualizar()
        with tab4: ManterVersaoUI.excluir()

    def listar():
        versao = View.versao_listar()
        if len(versao) == 0: 
            st.write("Nenhuma versão cadastrado")
        else:    
            dic = []
            for obj in versao: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        veiculos = View.veiculo_listar
        veiculo = st.selectbox("Informe o veiculo dessa versão", veiculos, index = None)
        nome = st.text_input("Informe o nome da versão")
        ano = st.text_input("Informe o ano da versão")
        preco = st.text_input("Informe o preço da versão")
        ipva = st.text_input("Informe o valor do IPVA")
        seguro = st.text_input("Informe o valor do seguro")
        garantia = st.text_input("Informe o tempo de garantia")
        porte = st.text_input("Informe o porte")
        lugares = st.text_input("Informe a quantidade de lugares")

        if st.button("Inserir"):
            View.versao_inserir(veiculo.id, nome, ano, preco, ipva, seguro, garantia, porte, lugares)
            st.success("Versão inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        versao = View.versao_listar()
        if len(versao) == 0: 
            st.write("Nenhuma versão cadastrado")
        else:
            op = st.selectbox("Atualização de versão", versao)
            veiculos = View.veiculo_listar
            veiculo = st.selectbox("Informe o novo veiculo dessa versão", veiculos, index = None)
            nome = st.text_input("Informe o novo nome da versão")
            ano = st.text_input("Informe o novo ano da versão")
            preco = st.text_input("Informe o novo preço da versão")
            ipva = st.text_input("Informe o novo valor do IPVA")
            seguro = st.text_input("Informe o novo valor do seguro")
            garantia = st.text_input("Informe o novo tempo de garantia")
            porte = st.text_input("Informe o novo porte")
            lugares = st.text_input("Informe a novo quantidade de lugares")

            if st.button("Atualizar"):
                View.versao_atualizar(veiculo.id, nome, ano, preco, ipva, seguro, garantia, porte, lugares)
                st.success("Versão atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        versao = View.versao_listar()
        if len(versao) == 0: 
            st.write("Nenhuma versão cadastrada")
        else:
            op = st.selectbox("Exclusão de versão", versao)
            if st.button("Excluir"):
                View.versao_excluir(op.id)
                st.success("Versão excluída com sucesso")
                time.sleep(2)
                st.rerun()
