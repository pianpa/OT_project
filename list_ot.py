from db import get_connection

def list_ordenes_trabajo():
    try:
        connection = get_connection()
        cursor = connection.cursor()
    
        cursor.execute("SELECT * FROM ordenes_trabajo")
        ordenes = cursor.fetchall()
        
        print("Listado de Órdenes de Trabajo:")
        for ot in ordenes:
            print(f"OT: {ot[1]} (Línea: {ot[2]}) - Estado: {ot[3]}")
        
        cursor.close()
        connection.close()
    
    except Exception as e:
        print(f"Error al listar las OTs: {e}")

if __name__ == "__main__":
    list_ordenes_trabajo()
        