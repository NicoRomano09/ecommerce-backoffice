# API REST - Models

## Descripción

Este documento define los modelos de datos utilizados por la API REST para la comunicación entre el frontend y el backend.

Los modelos serán implementados posteriormente mediante Pydantic en FastAPI.

---

# DashboardResponse

Representa la información mostrada en el Dashboard principal.

## Campos

- total_pedidos
- pedidos_entregados
- pedidos_pendientes
- pedidos_cancelados
- incidencias_abiertas
- ganancias
- costos
- rentabilidad

---

# PedidoResponse

Representa la información resumida de un pedido.

## Campos

- id_pedido
- cliente
- fecha_hora_pedido
- estado
- total
- fecha_entrega_estimada
- fecha_entrega_real

---

# PedidoDetalleResponse

Representa el detalle completo de un pedido.

## Campos

- información del pedido
- detalle de productos
- historial de estados
- incidencias asociadas

---

# IncidenciaResponse

Representa una incidencia registrada sobre un pedido.

## Campos

- id_incidencia
- pedido
- tipo_incidencia
- prioridad
- estado
- fecha_hora_incidencia

---

# GestionRequest

Modelo utilizado para registrar una gestión.

## Campos

- id_incidencia
- id_tipo_gestion
- observacion

---

# GestionResponse

Representa una gestión realizada sobre una incidencia.

## Campos

- id_gestion
- tipo_gestion
- observacion
- fecha_hora_gestion

---

# IndicadoresResponse

Representa los indicadores obtenidos para un período determinado.

## Campos

- fecha_desde
- fecha_hasta
- ventas
- costos
- ganancias
- pedidos
- incidencias