import streamlit as st
from src.core.df_handler import DfHandler

class HomeView:
    def __init__(self):
        self.title = "Home - Amazon Sales"
        self.df_handler = DfHandler()  # Alterei para deixar claro que é um manipulador, não o DataFrame direto.

    def render(self):
        st.title(self.title)

        # Obtém o DataFrame tratado
        df = self.df_handler.get_df()

        # Exibe o DataFrame na tela
        st.write("Dados processados:")
        st.dataframe(df)
