import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import get_connection
from psycopg2 import sql
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Administrar OT", layout="wide")
st.title("Administrar Órdenes de Trabajo")

# -----------------------------
# Listado de OT
# -----------------------------
try:
    conn = get_connection()
    cur = conn.cursor()
    query = sql.SQL("""
        SELECT id, descripcion, linea, estado, fecha_creacion, causa, motivo
        FROM ordenes_trabajo
        ORDER BY fecha_creacion DESC;
    """)
    cur.execute(query)
    resultados = cur.fetchall()
    cur.close()
    conn.close()

    df = pd.DataFrame(resultados, columns=["ID", "Descripción", "Línea", "Estado", "Fecha de Creación", "Motivo", "Causa"])
    df.set_index("ID", inplace=True)
    st.dataframe(df)

except Exception as e:
    st.error(f"❌ Error al listar OT: {e}")

# -----------------------------
# Selección de OT para editar o eliminar
# -----------------------------
ot_seleccionada = st.selectbox(
    "Seleccionar OT por ID para editar/eliminar",
    df.index.tolist() if not df.empty else []
)

if ot_seleccionada:
    ot_info = df.loc[ot_seleccionada]

    st.subheader("Editar OT")
    descripcion = st.text_input("Descripción", value=ot_info["Descripción"])
    linea = st.text_input("Línea", value=ot_info["Línea"])
    estado = st.selectbox(
        "Estado",
        ["Pendiente", "En Proceso", "Cancelada", "Terminada"],
        index=["Pendiente","En Proceso","Cancelada","Terminada"].index(ot_info["Estado"])
    )
    causa = st.text_input("Causa de la falla", value=ot_info.get("Causa Falla",""))
    motivo = st.text_input("Motivo", value=ot_info.get("Motivo",""))

    if st.button("Guardar cambios"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            query = sql.SQL("""
                UPDATE ordenes_trabajo
                SET descripcion=%s, linea=%s, estado=%s, causa_falla=%s, motivo=%s
                WHERE id=%s
            """)
            cur.execute(query, (descripcion, linea, estado, causa, motivo, ot_seleccionada))
            conn.commit()
            cur.close()
            conn.close()
            st.success("✅ OT actualizada correctamente")
        except Exception as e:
            st.error(f"❌ Error al actualizar OT: {e}")

    if st.button("Eliminar OT"):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM ordenes_trabajo WHERE id=%s", (ot_seleccionada,))
            conn.commit()
            cur.close()
            conn.close()
            st.success("❌ OT eliminada")
        except Exception as e:
            st.error(f"❌ Error al eliminar OT: {e}")
