from db import get_connection

def insert_orden_trabajo(descripcion, linea, estado="pendiente"):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO ordenes_trabajo (descripcion, linea, estado) 
            VALUES (%s, %s, %s)
        """, (descripcion, linea, estado))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"OT insertada: {descripcion} ({linea}) exitosamente.")
    except Exception as e:
        print(f"Error al insertar la OT: {e}")

if __name__ == "__main__":
    insert_orden_trabajo("Teste Standby step 2", "L05A")
    insert_orden_trabajo("Teste Final bloqueado", "L05B")
