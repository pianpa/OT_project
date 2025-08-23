# Proyecto OT - Gestión de Órdenes de Trabajo

Este proyecto es un sistema básico para registrar y listar órdenes de trabajo (OT) de mantenimiento, usando **Python**, **PostgreSQL** y buenas prácticas de desarrollo.

---

## Estructura del proyecto

```
mantenimiento_ot/
├── .gitignore
├── .env
├── README.md
├── db/
│   ├── db.py
│   └── create_tables.py
├── scripts/
│   ├── insert_ot.py
│   └── list_ot.py
├── tests/
└── docs/
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

## Uso

1. Crear la tabla de órdenes de trabajo:

```bash
python db/create_tables.py
```

2. Insertar órdenes de trabajo de ejemplo:

```bash
python scripts/insert_ot.py
```

3. Listar órdenes de trabajo:

```bash
python scripts/list_ot.py
```

---



