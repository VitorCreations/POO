import streamlit as st
import pandas as pd
from Views import View

class ListarVeiculoUI:
    def main():
        st.header("Veiculos")
        ListarVeiculoUI.listar()

    def listar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0: 
            st.write("Nenhum veiculo cadastrada")
        else:    
            dic = []
            for obj in veiculos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)