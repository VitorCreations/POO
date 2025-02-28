from templates.manterUsuarioUI import ManterUsuarioUI
from templates.manterFabricanteUI import ManterFabricanteUI
from templates.manterVeiculoUI import ManterVeiculoUI
from templates.manterVersaoUI import ManterVersaoUI
from templates.manterProfissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.LoginUI import LoginUI
from templates.meusdadosUsuarioUI import MeusDadosUsuarioUI
from templates.meusdadosProfissional import MeusDadosProfissionalUI
from templates.ListarFabricantes import ListarFabricanteUI
from templates.ListarVeiculos import ListarVeiculoUI
from templates.ListarVersoes import ListarVersãoUI

from Views import View

import streamlit as st
import pandas as pd

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
               
    def menu_usuario():            
        op = st.sidebar.selectbox("Menu", ["Usuarios", "Fabricantes", "Veiculos", "Profissionais", "Versões", "Meus Dados"])
        if op == "Usuarios": ManterUsuarioUI.main()
        if op == "Fabricantes": ManterFabricanteUI.main()
        if op == "Veiculos": ManterVeiculoUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Versões": ManterVersaoUI.main()
        if op == "Meus Dados": MeusDadosUsuarioUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Fabricantes", "Veículos", "Versões", "Meus Dados"])
        if op == "Fabricantes": ListarFabricanteUI.main()
        if op == "Veículos": ListarVeiculoUI.main()
        if op == "Versões": ListarVersãoUI.main()
        if op == "Meus Dados": MeusDadosUsuarioUI.main()


    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    
    def sidebar():
        if "usuario_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["usuario_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            # menu do usuário
            if st.session_state["tipo"] == "usuario":
                if admin: IndexUI.menu_usuario()
                else: IndexUI.menu_profissional()
            else:
                IndexUI.menu_profissional()    
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.usuario_admin()
        # monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()
