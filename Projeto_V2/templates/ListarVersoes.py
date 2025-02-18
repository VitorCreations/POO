import streamlit as st
import pandas as pd
from Views import View

class ListarVersãoUI:
    def main():
        st.header("Versões")
        ListarVersãoUI.listar()

    def listar():
        versao = View.versao_listar()
        if len(versao) == 0: 
            st.write("Nenhuma versão cadastrado")
        else:    
            dic = []
            for obj in versao: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)