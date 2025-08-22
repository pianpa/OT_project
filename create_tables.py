from db import get_connection

def create_tables():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ordenes_trabajo (
                id SERIAL PRIMARY KEY,
                descripcion TEXT NOT NULL,
                linea VARCHAR(50) NOT NULL,
                estado VARCHAR(20) DEFAULT 'pendiente',
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabla 'ordenes_trabajo' creada exitosamente.")

    if __name__ == "__main__":
        create_tables()
