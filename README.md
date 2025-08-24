# Sistema de Gestión de Órdenes de Trabajo (OT)

Este proyecto es una aplicación web desarrollada en **Python** utilizando **Streamlit** para la gestión de órdenes de trabajo en línea de producción. Permite registrar, administrar y visualizar las OT, con integración a una base de datos PostgreSQL.

---

## Estructura del proyecto

```
OT/
├── assets/ # Imágenes, logos, etc.
│ └── keen-logo.png
├── db/ # Conexión y funciones de base de datos
│ ├── init.py
│ ├── db.py
│ └── create_tables.py
├── pages/ # Páginas multipágina de la app
│ ├── 0_Dashboard.py
│ ├── 1_Carga_OT.py
│ ├── 2_Administrar_OT.py
│ └── 3_Reportes.py
├── scripts/OLD/ # Scripts antiguos, no utilizados
├── main.py # Entrada principal de la app (homepage)
├── requirements.txt
└── README.md
```

- `db/` → conexión a la base de datos y creación de tablas.  
- `scripts/` → scripts para insertar y listar órdenes de trabajo.  
- `tests/` → pruebas unitarias.  
- `docs/` → documentación del proyecto.  
- `.env` → credenciales de la base de datos (no subir a GitHub).

---

## Instalación

1. Clonar el repositorio:

```bash
git clone git@github.com:tu_usuario/mantenimiento_ot.git
cd mantenimiento_ot
```

2. Crear entorno virtual:

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
# o
source venv/bin/activate       # Linux/Mac
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

> Nota: si no tenés `requirements.txt` todavía, instalar manualmente:  
```bash
pip install psycopg2-binary python-dotenv
```

---

## Configuración de la base de datos

Crear un archivo `.env` en la raíz con tus credenciales de PostgreSQL:

```
DB_NAME=ot_db
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_HOST=host_de_neon
DB_PORT=5432
```

---

## 🚀 Ejecución de la app

1. Activar el entorno virtual:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
Instalar dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecutar la aplicación multipágina desde la raíz:

bash
Copiar
Editar
streamlit run main.py
Esto abrirá la página principal (main.py) como homepage.

Streamlit detectará automáticamente todas las páginas dentro de pages/ y generará el menú lateral con ellas.

