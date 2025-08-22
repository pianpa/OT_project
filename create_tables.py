from db import get_connection

def create_tables():
    try:
        connection = get_connection()
        cur = connection.cursor()

        #Crear tabla de ordenes de trabajo
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ordenes_trabajo (
                id SERIAL PRIMARY KEY,
                descripcion TEXT NOT NULL,
                linea VARCHAR(50) NOT NULL,
                estado VARCHAR(20) DEFAULT 'pendiente',
                fecha_creacion TIMESTAMP DEFAULT now()
            );
        """)
        connection.commit()
        cur.close()
        connection.close()
        print("Tabla 'ordenes_trabajo' creada exitosamente.")

    except Exception as e:
        print(f"Error al crear la tabla 'ordenes_trabajo': {e}")

if __name__ == "__main__":
    create_tables()