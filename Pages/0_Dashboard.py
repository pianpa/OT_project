import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import get_connection

import streamlit as st

st.set_page_config(page_title="Dashboard OT", layout="wide")
st.title("Dashboard de Órdenes de Trabajo")
st.markdown("Bienvenido al panel principal. Desde aquí podés navegar a las distintas secciones de la app.")
