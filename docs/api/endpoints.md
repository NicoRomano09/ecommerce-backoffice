# API REST - Endpoints

## Descripción

Este documento define los endpoints de la API REST que serán consumidos por el frontend desarrollado en Angular.

Todos los endpoints devolverán información en formato JSON.

---

# Dashboard

## Obtener métricas generales

GET /dashboard

### Descripción

Obtiene los indicadores principales del sistema.

### Respuesta esperada

- Total de pedidos.
- Pedidos entregados.
- Pedidos pendientes.
- Pedidos cancelados.
- Incidencias abiertas.
- Ganancias.
- Costos.
- Rentabilidad.

---

# Pedidos

## Obtener listado de pedidos

GET /pedidos

### Parámetros (opcionales)

- fecha_desde
- fecha_hasta
- estado

---

## Obtener detalle de un pedido

GET /pedidos/{id}

---

# Historial de Pedido

## Obtener historial de estados

GET /pedidos/{id}/historial

---

# Incidencias

## Obtener incidencias

GET /incidencias

### Parámetros (opcionales)

- estado
- prioridad
- tipo

---

## Obtener detalle de una incidencia

GET /incidencias/{id}

---

# Gestión

## Registrar una gestión

POST /gestion

### Body

- id_incidencia
- id_tipo_gestion
- observacion

---

## Obtener gestiones de una incidencia

GET /incidencias/{id}/gestiones

---

# Indicadores

## Obtener indicadores por período

GET /indicadores

### Parámetros

- fecha_desde
- fecha_hasta

---

# Exportación

## Exportar pedidos

GET /export/pedidos

---

## Exportar incidencias

GET /export/incidencias

---

# Convenciones

## Código HTTP

| Código  | Significado           |
|---------|-----------------------|
| 200     | OK                    |
| 201     | Recurso creado        |
| 400     | Solicitud inválida    |
| 404     | Recurso no encontrado |
| 500     | Error interno         |

---

## Formato de respuesta

Éxito

```json
{
  "success": true,
  "data": {}
}
```

Error

```json
{
  "success": false,
  "message": "Descripción del error"
}
```