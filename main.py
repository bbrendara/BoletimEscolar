from os import write
import streamlit as st;
from numpy.core.fromnumeric import size
import Controllers.AlunoController as AlunoController
import models.Aluno as aluno
import streamlit.components.v1 as components
import pandas as pd
import Pages.Aluno.Create as PageCreateCliente
import Pages.Aluno.List as PageListCliente



st.sidebar.title('Opções')
Page_cliente = st.sidebar.selectbox ('Aluno', ['Incluir aluno', 'Consultar' ])

if Page_cliente == 'Consultar':
    PageListCliente.List()

    
    
if Page_cliente == 'Incluir aluno':
    
    PageCreateCliente.Create()

        


   
