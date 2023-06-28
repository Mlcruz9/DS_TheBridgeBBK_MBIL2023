import streamlit as st
import pandas as pd
from PIL import Image
# from functions import home, datos, cargar_datos, menu_filtros

# Este es mi script

st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')

path_csv = 'data/red_recarga_acceso_publico_2021.csv'
df = pd.read_csv(path_csv, sep=';')

st.dataframe(df)

st.balloons()