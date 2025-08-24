import sys
import os
# Agregar la raíz del proyecto al path para que Python encuentre 'db'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from db.db import get_connection
from psycopg2 import sql
from datetime import datetime
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Gestión OT", layout="wide") 


# -----------------------------
# BARRA SUPERIOR / APPBAR
# -----------------------------
logo_path = os.path.join(os.path.dirname(__file__), "../assets/keen-logo.png")
left_co, last_co = st.columns([1,5])
with left_co:
    st.image(logo_path, width=40, use_container_width=True)
with last_co:
    st.markdown("<h2 style='margin-top: 10px; padding-top:20px;'>🏭 Gestión de Órdenes de Trabajo</h2>", unsafe_allow_html=True)



# -----------------------------
# FORMULARIO DE INGRESO DE OT
# -----------------------------
st.subheader("Ingresar nueva OT")

# Obtener líneas de producción desde la BBDD
lineas = ["Selecciona una línea..."]  # Opción inicial vacía
try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT nombre FROM lineas ORDER BY nombre;")
    resultado = cur.fetchall()
    cur.close()
    conn.close()

    # Agregar nombres de líneas desde la BBDD
    lineas.extend([row[0] for row in resultado])

except Exception as e:
    st.error(f"❌ Error al obtener líneas de producción: {e}")

with st.form(key='form_ot', clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        descripcion = st.text_input("Descripción de la OT", key="desc")

    with col2:
        # Opción vacía inicial para obligar a elegir
        linea = st.selectbox("Línea de producción", lineas, key="linea")

    submit_button = st.form_submit_button("Guardar OT")

# -----------------------------
# VALIDACIÓN Y GUARDADO
# -----------------------------
if submit_button:
    if linea == "Selecciona una línea...":
        st.warning("⚠️ Debes seleccionar una línea de producción antes de guardar.")
    elif not descripcion.strip():
        st.warning("⚠️ La descripción no puede estar vacía.")
    else:
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = sql.SQL("""
                INSERT INTO ordenes_trabajo (descripcion, linea)
                VALUES (%s, %s)
                RETURNING id;
            """)
            cur.execute(query, (descripcion, linea))
            new_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            st.success(f"✅ OT creada con ID: {new_id}")

        except Exception as e:
            st.error(f"❌ Error al insertar OT: {e}")

# -----------------------------
# LISTADO DE OT
# -----------------------------
st.subheader("Listado de OT")
try:
    conn = get_connection()
    cur = conn.cursor()
    query = sql.SQL("""
        SELECT id, descripcion, linea, estado, fecha_creacion
        FROM ordenes_trabajo
        ORDER BY fecha_creacion DESC;
    """)
    cur.execute(query)
    resultados = cur.fetchall()
    cur.close()
    conn.close()

    data = []
    for ot in resultados:
        data.append({
            "ID": ot[0],
            "Descripción": ot[1],
            "Línea": ot[2],
            "Estado": ot[3],
            "Fecha de Creación": ot[4].strftime("%d/%m/%Y %H:%M")
        })
    df = pd.DataFrame(data)

    df.set_index('ID', drop=True, inplace=True)
    df = df.drop(columns=['Estado'])  # Ocultar columna Estado para mayor claridad
    st.dataframe(df)

except Exception as e:
    st.error(f"❌ Error al listar OT: {e}")
