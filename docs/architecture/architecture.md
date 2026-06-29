# Arquitectura del Sistema

## Arquitectura General

```
                    Usuario
                       │
                       ▼
     Frontend (Angular + TypeScript)
                       │
                 HTTP / JSON
                       │
                       ▼
             API REST (FastAPI)
                       │
                       ▼
            Lógica de Negocio
      (Dashboard / Pedidos / Incidencias)
                       │
                       ▼
               SQLAlchemy (ORM)
                       │
                       ▼
                     MySQL
                       ▲
                       │
        Script de carga de datos
     (Python + Pandas + Faker)
```

---

## Flujo de una consulta

```
Usuario
    │
    ▼
Dashboard
    │
    ▼
Angular
    │
    ▼
GET /dashboard
    │
    ▼
FastAPI
    │
    ▼
SQLAlchemy
    │
    ▼
MySQL
    │
    ▼
Respuesta JSON
    │
    ▼
Angular renderiza gráficos
```

---

## Flujo de una gestión

```
Usuario
    │
    ▼
Selecciona una incidencia
    │
    ▼
Angular
    │
    ▼
POST /gestion
    │
    ▼
FastAPI
    │
    ▼
Validación de reglas de negocio
    │
    ▼
SQLAlchemy
    │
    ▼
MySQL
    │
    ▼
Respuesta OK
    │
    ▼
Angular actualiza la interfaz
```

---

## Stack Tecnológico

| Capa                      | Tecnología        |
|---------------------------|-------------------|
| Frontend                  | Angular           |
| Lenguaje Frontend         | TypeScript        |
| Componentes UI            | Bootstrap         |
| Enrutamiento              | Angular Router    |
| Comunicación HTTP         | HttpClient        |
| Backend                   | Python + FastAPI  |
| ORM                       | SQLAlchemy        |
| Base de Datos             | MySQL             |
| Migraciones               | Alembic           |
| API                       | REST              |
| Generación de datos       | Faker             |
| Procesamiento de datos    | Pandas            |
| Control de versiones      | Git + GitHub      |

---

## Descripción de Tecnologías

### Angular
Framework para el desarrollo del frontend basado en componentes.

### TypeScript
Lenguaje utilizado por Angular que agrega tipado estático sobre JavaScript.

### Bootstrap
Framework CSS para construir interfaces responsivas.

### FastAPI
Framework de Python para construir APIs REST de alto rendimiento.

### SQLAlchemy
ORM que permite interactuar con MySQL utilizando objetos Python en lugar de escribir consultas SQL para todas las operaciones.

### Alembic
Herramienta para versionar y administrar cambios en el esquema de la base de datos mediante migraciones.

### MySQL
Sistema gestor de bases de datos relacional utilizado para almacenar la información del sistema.

### Pandas
Librería de Python para manipular, transformar y cargar grandes volúmenes de datos.

### Faker
Librería utilizada para generar datos ficticios (clientes, direcciones, teléfonos, pedidos, etc.) con el objetivo de poblar la base de datos para pruebas y desarrollo.

### Git + GitHub
Herramientas utilizadas para el control de versiones y la gestión del repositorio del proyecto.