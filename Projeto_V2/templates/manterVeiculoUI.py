import streamlit as st
import pandas as pd
from Views import View
import matplotlib.pyplot as plt
import json
import time

class ManterVeiculoUI:
    def main():
        st.header("Cadastro de Veiculos")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Gráfico", "Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterVeiculoUI.grafico()
        with tab2: ManterVeiculoUI.listar()
        with tab3: ManterVeiculoUI.inserir()
        with tab4: ManterVeiculoUI.atualizar()
        with tab5: ManterVeiculoUI.excluir()

    def grafico():
        with open('versões.json', mode='r', encoding='utf-8') as arquivo:
            versoes = json.load(arquivo)
        
        b = (
            
            Bar(versoes)
            .add_xaxis(json.nome)
            .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="Veículos por Fabricantes"
            )
            )
        )

    
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
        fabricantes = View.fabricante_listar()
        if len(fabricantes) == 0: 
            st.write("Nenhuma fabricante cadastrada")
        else:    
            dic = []
            for obj in fabricantes: dic.append(obj.__dict__)

        
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


            fabricantes = View.fabricante_listar()
            if len(fabricantes) == 0: 
                st.write("Nenhuma fabricante cadastrada")
            else:    
                dic = []
                for obj in fabricantes: dic.append(obj.__dict__)


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
