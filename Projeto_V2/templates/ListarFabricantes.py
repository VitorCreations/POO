import streamlit as st
import pandas as pd
from Views import View

class ListarFabricanteUI:
    def main():
        st.header("Fabricantes")
        ListarFabricanteUI.listar()

    def listar():
        fabricantes = View.fabricante_listar()
        if len(fabricantes) == 0: 
            st.write("Nenhuma fabricante cadastrada")
        else:    
            dic = []
            for obj in fabricantes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)