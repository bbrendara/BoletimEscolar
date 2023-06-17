import streamlit as st;
import Controllers.AlunoController as AlunoController
from unittest import main

import Pages.Aluno.Create as PageCreateAluno


def List():
    paramID = st.experimental_get_query_params()
    if paramID == {}:
        
        colms= st.columns((2,2,2,3,3,3,3,3,3,3, 3, 3))
        campos = ['Matricula', 'Nome', 'Serie', 'Artes', 'Ciencias', 'Fisica', 'Geografia', 'Historia', 'Portugues', 'Matematica', '', '']
    
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)
    
        for x, item in enumerate(AlunoController.SelecionarTodos()):
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns((2,2,2,3,3,3,3,3,3,3, 3, 3))
            col1.write(item.matricula)
            col2.write(item.nome)
            col3.write(item.serie)
            col4.write(item.artes)
            col5.write(item.ciencias)
            col6.write(item.fisica)
            col7.write(item.geografia)
            col8.write(item.historia)
            col9.write(item.portugues)
            col10.write(item.matematica)
            button_space_excluir = col11.empty()
            on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.matricula))
            button_space_alterar = col12.empty()
            on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.matricula))
        
            if on_click_excluir:
                AlunoController.Excluir(item.matricula)
                button_space_excluir.button('Excluído')
           
            if on_click_alterar:
                st.experimental_set_query_params(
                    matricula= [item.matricula]
            )
                st.experimental_rerun()
            

            
    else:
        PageCreateAluno.Create()
        