import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Gestión OT - Dashboard",
    layout="wide",
    page_icon="📊"
)

# -----------------------------
# BARRA SUPERIOR / APPBAR
# -----------------------------
logo_url = "assets/keen-logo.png"  # Asegurate de la ruta
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1 style='text-align: center;'>Bienvenido al Sistema de Gestión de OT</h1>", unsafe_allow_html=True)
with col2:
    st.image(logo_url, width=150)

st.markdown("---")

# -----------------------------
# KPIs de ejemplo
# -----------------------------
st.subheader("Indicadores Clave")
col1, col2, col3, col4 = st.columns(4)

# Valores de ejemplo, luego se conectará a la BBDD
total_ot = 128
pendientes = 45
en_proceso = 60
terminadas = 23

col1.metric("Total OT", total_ot, delta=None)
col2.metric("Pendientes", pendientes, delta=None)
col3.metric("En Proceso", en_proceso, delta=None)
col4.metric("Terminadas", terminadas, delta=None)

st.markdown("---")

# -----------------------------
# Gráficos de ejemplo
# -----------------------------
st.subheader("Distribución de OT por Línea")
lineas = ["Línea 1", "Línea 2", "Línea 3", "Línea 4"]
valores = [30, 50, 20, 28]
df_lineas = pd.DataFrame({"Línea": lineas, "Cantidad OT": valores})
st.bar_chart(df_lineas.set_index("Línea"))

st.subheader("Estado de las OT")
estados = ["Pendientes", "En Proceso", "Terminadas"]
valores_estado = [pendientes, en_proceso, terminadas]
df_estado = pd.DataFrame({"Estado": estados, "Cantidad": valores_estado})
st.pyplot(df_estado.plot.pie(y="Cantidad", labels=df_estado["Estado"], autopct="%1.1f%%", legend=False).figure)
