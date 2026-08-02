from app.database.connection import engine
from script.seed_data import (
    ESTADOS_PEDIDO,
    TIPOS_INCIDENCIA,
    ESTADOS_INCIDENCIA,
    TIPOS_GESTION,
    PRODUCTOS_POR_CATEGORIA,
    RANGOS_COSTOS,
    LOCALIDADES_POR_PROVINCIA,
    CODIGOS_AREA,
    BARRIOS_POR_PROVINCIA,
    PESOS_ESTADOS,
    DIAS_ENTREGA,
    ESTADOS_CON_FECHA_REAL,
    FLUJOS_ESTADOS,
    TRANSICIONES_ESTADOS,
    ESTADOS_CON_INCIDENCIA_OBLIGATORIA,
    ESTADOS_CON_INCIDENCIA_ALEATORIA,
    TIPOS_INCIDENCIA_POR_ESTADO,
    PRIORIDAD_INCIDENCIA,
    TIPOS_GESTION_POR_INCIDENCIA,
    OBSERVACIONES
) 
from sqlalchemy import MetaData, Table, func, select
from faker import Faker
from datetime import datetime, timedelta
from decimal import Decimal
import random

# Instancia de Faker / "es_AR" es un locale (región/cultura)
faker = Faker("es_AR")

# Obtener tabla
def obtener_tabla(connection, nombre_tabla):
    metadata = MetaData()
    return Table(
        nombre_tabla, 
        metadata, 
        autoload_with=connection
    )

# Validar si la tabla contiene datos
def tabla_tiene_datos(connection, tabla):
    query = select(func.count()).select_from(tabla)
    cantidad = connection.execute(query).scalar()
    return cantidad > 0

# Obtener tablas catalogo, validar e insertar datos
def cargar_catalogo(connection, nombre_tabla, datos):
    tabla = obtener_tabla(connection, nombre_tabla)
    if tabla_tiene_datos(connection, tabla):
        print(
            f"✗ La tabla '{nombre_tabla}' ya contiene datos. "
            "No se realizará la carga."
        )
        return
    connection.execute(tabla.insert(), datos)
    connection.commit()
    print(f"✓ Datos cargados exitosamente en la tabla '{nombre_tabla}'.")

# Script para poblar la base de datos con datos de prueba
# Tablas Catalogos

def generar_estado_pedido(connection):
    cargar_catalogo(connection, "estado_pedido", ESTADOS_PEDIDO)

def generar_tipo_incidencia(connection):
    cargar_catalogo(connection, "tipo_incidencia", TIPOS_INCIDENCIA)

def generar_estado_incidencia(connection):
    cargar_catalogo(connection, "estado_incidencia", ESTADOS_INCIDENCIA)

def generar_tipo_gestion(connection):
    cargar_catalogo(connection, "tipo_gestion", TIPOS_GESTION)

# Script para generar tablas de entidades maestras
def generar_productos(connection):
    tabla = obtener_tabla(connection, "producto")
    if tabla_tiene_datos(connection, tabla):
        print(
            "✗ La tabla 'producto' ya contiene datos. "
            "No se realizará la carga."
        )
        return
    productos_generados = []
    for categoria, productos in PRODUCTOS_POR_CATEGORIA.items():
        for nombre_producto in productos:
            producto = {
                "nombre_producto": nombre_producto,
                "categoria": categoria,
            }
            productos_generados.append(producto)
    
    random.shuffle(productos_generados)
    productos = productos_generados[:50]
    
    for producto in productos:
        margin = round(random.uniform(1.2, 1.3), 2)
        rango = RANGOS_COSTOS[producto["categoria"]]
        costo_unitario = round(
            random.uniform(rango[0], rango[1]),
            2
        )
        precio_unitario = round(costo_unitario * margin, 2)
        producto["costo_unitario"] = costo_unitario
        producto["precio_unitario"] = precio_unitario
    try: 
        connection.execute(tabla.insert(), productos)
        connection.commit()
        print(
            f"✓ Datos cargados exitosamente en la tabla 'producto'."
            f"Registros insertados: {len(productos)}"
            )
    except Exception as e:
        print(f"✗ Error al insertar productos: {e}")
# Script para generar tablas de entidades transaccionales

def generar_clientes(connection):
    tabla = obtener_tabla(connection, "cliente")
    if tabla_tiene_datos(connection, tabla):
        print(
            "✗ La tabla 'cliente' ya contiene datos. "
            "No se realizará la carga."
        )
        return
    clientes = []
    for c in range(500):
        # Ubicación
        provincia = random.choice(list(LOCALIDADES_POR_PROVINCIA.keys()))
        localidad = random.choice(LOCALIDADES_POR_PROVINCIA[provincia])
        ciudad = localidad["ciudad"]
        codigo_postal = localidad["codigo_postal"]
        datos_area = CODIGOS_AREA[provincia] 
        codigo_area = datos_area["codigo"]
        digitos = datos_area["digitos"]
        telefono = codigo_area
        telefono += faker.numerify("#" * digitos)
        
        # Indentidad 
        numero_documento = str(faker.unique.random_int(min=10000000, max=99999999))
        nombre_cliente = faker.first_name()
        apellido_cliente = faker.last_name()
        email = faker.unique.email()
        
        # Dirección
        calle = faker.street_name()
        numero = str(faker.random_int(min=1, max=9999))
        depto = random.choice([None, None, None, None, "A", "B", "C"])
        piso = random.choice([None, None, None, None, None, None, None, "1", "2", "3", "4", "5"])
        zonas = BARRIOS_POR_PROVINCIA[provincia]
        barrio = random.choice([None, None, None, None] + zonas)
        
        cliente = {
            "numero_documento" : numero_documento,
            "nombre_cliente" : nombre_cliente,
            "apellido_cliente" : apellido_cliente,
            "telefono" : telefono,
            "email" : email,
            "calle" : calle,
            "numero" : numero,
            "depto" : depto,
            "piso" : piso,
            "barrio" : barrio,
            "codigo_postal" : codigo_postal,
            "ciudad" : ciudad,
            "provincia" : provincia
        }
        clientes.append(cliente)
    try:
        connection.execute(tabla.insert(), clientes)
        connection.commit()
        print(
            f"✓ Datos cargados exitosamente en la tabla 'cliente'.\n"
            f"Registros Insertados: {len(clientes)}"
            )
    except Exception as e:
        connection.rollback()
        print(f"✗ Error al insertar clientes: {e}")
        raise

def obtener_clientes(connection):
    tabla = obtener_tabla(connection, "cliente")
    query = select(
        tabla.c.id_cliente,
        tabla.c.provincia
        )
    resultado = connection.execute(query)
    clientes = resultado.mappings().all()
    return clientes

def obtener_estados_pedidos(connection):
    tabla = obtener_tabla(connection, "estado_pedido")
    query = select(
        tabla.c.id_estado_pedido,
        tabla.c.nombre_estado_pedido,
        tabla.c.orden
    )
    resultado = connection.execute(query)
    estados_pedidos = resultado.mappings().all()
    return estados_pedidos

def obtener_productos(connection):
    tabla = obtener_tabla(connection, "producto")
    query = select(
        tabla.c.id_producto,
        tabla.c.precio_unitario,
        tabla.c.costo_unitario
    )
    resultado = connection.execute(query)
    productos = resultado.mappings().all()
    return productos

def seleccionar_estado_ponderado(estados_pedidos):
    pesos = []
    for estado in estados_pedidos:
        peso = PESOS_ESTADOS[estado["orden"]]
        pesos.append(peso)
    estado = random.choices(
        estados_pedidos,
        weights=pesos,
        k=1
    )[0]
    return estado

def generar_fecha_pedido():
    fecha_actual = datetime.now()
    fecha_inicio = fecha_actual - timedelta(days=90)
    diferencia = fecha_actual - fecha_inicio
    segundos = random.randint(
        0, 
        int(diferencia.total_seconds())
    )
    fecha_pedido = fecha_inicio + timedelta(seconds=segundos)
    return fecha_pedido

def obtener_dias_entrega(provincia):
    dias_entrega = random.choice(DIAS_ENTREGA[provincia])
    return dias_entrega

def sumar_dias_habiles(fecha_pedido, dias_entrega):
    fecha_calculada = fecha_pedido
    contador = 0
    while contador < dias_entrega:
        fecha_calculada += timedelta(days=1)
        if fecha_calculada.weekday() < 5:
            contador += 1
    return fecha_calculada

def generar_fechas_entrega(estado, fecha_pedido, provincia):
    dias = obtener_dias_entrega(provincia)
    fecha_entrega_estimada = sumar_dias_habiles(fecha_pedido, dias)
    if estado["nombre_estado_pedido"] in ESTADOS_CON_FECHA_REAL:
        variacion = random.choice([-1, 0, 1])
        if variacion >= 0:
            fecha_entrega_real = sumar_dias_habiles(fecha_entrega_estimada, variacion)
        else:
            fecha_entrega_real = fecha_entrega_estimada + timedelta(days=variacion)
            while fecha_entrega_real.weekday() >= 5:
                fecha_entrega_real += timedelta(days=variacion)
    else:
        fecha_entrega_real = None
    return fecha_entrega_estimada, fecha_entrega_real

def generar_pedido(cliente, estados_pedidos, productos):
    estado_pedido = seleccionar_estado_ponderado(estados_pedidos)
    fecha_pedido = generar_fecha_pedido()
    fecha_entrega_estimada, fecha_entrega_real = generar_fechas_entrega(
        estado_pedido, 
        fecha_pedido, 
        cliente["provincia"]
        )
    cantidad_productos = random.randint(1, 5)
    productos_seleccionados = random.sample(
        productos,
        cantidad_productos
    )
    total = Decimal("0.00")
    costo_total = Decimal("0.00")
    detalles_pedido = []
    for producto in productos_seleccionados:
        id_producto = producto["id_producto"] 
        precio_unitario = producto["precio_unitario"]
        costo_unitario = producto["costo_unitario"]
        cantidad = random.randint(1, 3)
        detalle = {
            "id_producto" : id_producto,
            "cantidad" : cantidad,
            "precio_unitario" : precio_unitario,
            "costo_unitario" : costo_unitario
        }
        detalles_pedido.append(detalle)
        subtotal = cantidad * precio_unitario
        subtotal_costo = cantidad * costo_unitario
        total += subtotal
        costo_total += subtotal_costo
    pedido = {
        "fecha_hora_pedido" : fecha_pedido,
        "id_cliente" : cliente["id_cliente"],
        "id_estado_pedido" : estado_pedido["id_estado_pedido"],
        "total" : total,
        "costo_total" : costo_total,
        "fecha_entrega_estimada" : fecha_entrega_estimada,
        "fecha_entrega_real" : fecha_entrega_real
    }
    return pedido, detalles_pedido

def generar_pedidos(connection):
    clientes = obtener_clientes(connection)
    estados_pedidos = obtener_estados_pedidos(connection)
    productos = obtener_productos(connection)
    tabla_pedido = obtener_tabla(connection, "pedido")
    tabla_detalle_pedido = obtener_tabla(connection, "detalle_pedido")
    tipos_incidencia = obtener_tipos_incidencia(connection)
    tipos_gestion = obtener_tipos_gestion(connection)
    pedidos_insertados = 0
    detalles_insertados = 0
    try:
        for cliente in clientes:
            cantidad_pedidos = random.randint(0, 3)
            for _ in range(cantidad_pedidos):
                pedido, detalles_pedido = generar_pedido(
                    cliente, 
                    estados_pedidos, 
                    productos
                )
                resultado = connection.execute(
                    tabla_pedido.insert(), 
                    pedido
                )
                id_pedido = resultado.inserted_primary_key[0]
                for detalle in detalles_pedido:
                    detalle["id_pedido"] = id_pedido
                connection.execute(
                    tabla_detalle_pedido.insert(),
                    detalles_pedido
                )
                generar_historial_estados(
                    connection,
                    id_pedido,
                    pedido,
                    estados_pedidos,
                    cliente["provincia"]
                )
                incidencia = generar_incidencia(
                    connection,
                    id_pedido,
                    pedido,
                    tipos_incidencia
                )
                if incidencia is not None:
                    generar_gestion(
                        connection,
                        incidencia,
                        tipos_gestion
                    )
                pedidos_insertados += 1
                detalles_insertados += len(detalles_pedido)
        connection.commit()
        print(
            "✓ Pedidos generados exitosamente.\n"
            f"Pedidos insertados: {pedidos_insertados}\n"
            f"Detalles insertados: {detalles_insertados}"
        )
    except Exception as e:
        connection.rollback()
        print(f"✗ Error al generar pedidos: {e}")
        raise

def calcular_siguiente_fecha_estado(fecha_actual, estado_actual, estado_siguiente, provincia):
    transicion = (estado_actual, estado_siguiente)
    if transicion == ("EN_TRANSITO", "ENTREGADO"):
        dias = obtener_dias_entrega(provincia)
    else:
        minimo, maximo = TRANSICIONES_ESTADOS[transicion]
        dias = random.randint(minimo, maximo)
    fecha_estado_siguiente = sumar_dias_habiles(fecha_actual, dias)
    return fecha_estado_siguiente

def generar_historial_estados(connection, id_pedido, pedido, estados_pedidos, provincia):
    tabla_historial = obtener_tabla(connection, "historial_estado")
    estado_actual = pedido["id_estado_pedido"]
    for estado in estados_pedidos:
        if estado_actual == estado["id_estado_pedido"]:
            estado_actual = estado
            break
    if estado_actual["id_estado_pedido"] in FLUJOS_ESTADOS:
        flujo = []
        ids_flujo = FLUJOS_ESTADOS[estado_actual["id_estado_pedido"]]
        for estado in estados_pedidos:
            if estado["id_estado_pedido"] in ids_flujo:
                flujo.append(estado)
    else:
        flujo = []
        for estado in estados_pedidos:
            if estado["orden"] <= estado_actual["orden"]:
                flujo.append(estado)
    fecha = pedido["fecha_hora_pedido"]
    historial_estados = []
    for indice in range(len(flujo)):
        estado = flujo[indice]
        registro = {
            "id_pedido" : id_pedido,
            "id_estado_pedido" : estado["id_estado_pedido"],
            "fecha_hora_estado" : fecha
        }
        if indice < len(flujo) - 1:
            estado_siguiente = flujo[indice + 1]
            fecha = calcular_siguiente_fecha_estado(
                fecha, 
                estado["nombre_estado_pedido"], 
                estado_siguiente["nombre_estado_pedido"],
                provincia
            )
        historial_estados.append(registro)
    connection.execute(tabla_historial.insert(), historial_estados) 

def obtener_pedidos(connection):
    tabla = obtener_tabla(connection, "pedido")
    query = select(
        tabla.c.id_pedido,
        tabla.c.fecha_hora_pedido,
        tabla.c.id_cliente,
        tabla.c.id_estado_pedido,
        tabla.c.fecha_entrega_estimada,
        tabla.c.fecha_entrega_real
    )
    resultado = connection.execute(query)
    pedidos = resultado.mappings().all()
    return pedidos

def obtener_tipos_incidencia(connection):
    tabla = obtener_tabla(connection, "tipo_incidencia")
    query = select(
        tabla.c.id_tipo_incidencia,
        tabla.c.nombre_incidencia
    )
    resultado = connection.execute(query)
    tipos_incidencia = resultado.mappings().all()
    return tipos_incidencia

def generar_fecha_incidencia(fecha_pedido):
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_pedido
    segundos = random.randint(
        0, 
        int(diferencia.total_seconds())
    )
    fecha_hora_incidencia = fecha_pedido + timedelta(seconds=segundos)
    return fecha_hora_incidencia

def generar_incidencia(connection, id_pedido, pedido, tipos_incidencia):
    tabla = obtener_tabla(connection, "incidencia")
    generar = False
    if pedido["id_estado_pedido"] in ESTADOS_CON_INCIDENCIA_OBLIGATORIA:
        generar = True
    elif pedido["id_estado_pedido"] in ESTADOS_CON_INCIDENCIA_ALEATORIA:
        generar = random.random() <= 0.15
    if not generar:
        return None
    tipo_incidencia = random.choice(
        TIPOS_INCIDENCIA_POR_ESTADO[pedido["id_estado_pedido"]]
    )
    id_tipo_incidencia = None
    for tipo in tipos_incidencia:
        if tipo["nombre_incidencia"] == tipo_incidencia:
            id_tipo_incidencia = tipo["id_tipo_incidencia"]
            break
    minimo, maximo = PRIORIDAD_INCIDENCIA[id_tipo_incidencia]
    prioridad = random.randint(minimo, maximo)
    incidencia = {
        "id_pedido": id_pedido,
        "id_tipo_incidencia": id_tipo_incidencia,
        "prioridad": prioridad,
        "id_estado_incidencia": 1,
        "fecha_hora_incidencia": generar_fecha_incidencia(
            pedido["fecha_hora_pedido"]
        )
    }
    resultado = connection.execute(tabla.insert(), incidencia)
    return {
        "id_incidencia": resultado.inserted_primary_key[0],
        "id_tipo_incidencia": id_tipo_incidencia,
        "fecha_hora_incidencia": incidencia["fecha_hora_incidencia"]
    }

def obtener_incidencias(connection):
    tabla = obtener_tabla(connection, "incidencia")
    query = select(
        tabla.c.id_incidencia,
        tabla.c.id_tipo_incidencia,
        tabla.c.fecha_hora_incidencia
    )
    resultado = connection.execute(query)
    incidencias = resultado.mappings().all()
    return incidencias

def obtener_tipos_gestion(connection):
    tabla = obtener_tabla(connection, "tipo_gestion")
    query = select(
        tabla.c.id_tipo_gestion,
        tabla.c.nombre_gestion
    )
    resultado = connection.execute(query)
    tipos_gestion = resultado.mappings().all()
    return tipos_gestion

def generar_fecha_gestion(fecha_hora_incidencia):
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_hora_incidencia
    segundos = random.randint(
        0, 
        int(diferencia.total_seconds())
    )
    fecha_hora_gestion = fecha_hora_incidencia + timedelta(seconds=segundos)
    return fecha_hora_gestion

def generar_gestion(connection, incidencia, tipos_gestion):
    tabla = obtener_tabla(connection, "gestion")
    tipo_gestion = random.choice(
        TIPOS_GESTION_POR_INCIDENCIA[
            incidencia["id_tipo_incidencia"]
        ]
    )
    id_tipo_gestion = None
    for tipo in tipos_gestion:
        if tipo["nombre_gestion"] == tipo_gestion:
            id_tipo_gestion = tipo["id_tipo_gestion"]
            break
    gestion = {
        "id_incidencia": incidencia["id_incidencia"],
        "id_tipo_gestion": id_tipo_gestion,
        "observacion": random.choice(
            OBSERVACIONES[tipo_gestion]
        ),
        "fecha_hora_gestion": generar_fecha_gestion(
            incidencia["fecha_hora_incidencia"]
        )
    }
    connection.execute(tabla.insert(), gestion)

def main():
    try:
        with engine.connect() as connection:
            print("✓ Conexión con la base de datos establecida exitosamente.")
            generar_estado_pedido(connection)
            generar_tipo_incidencia(connection)
            generar_estado_incidencia(connection)
            generar_tipo_gestion(connection)
            generar_productos(connection)
            generar_clientes(connection)
            generar_pedidos(connection)
    except Exception as e:
        print(f"✗ Error al conectar con la base de datos: {e}")
        raise
    
if __name__ == "__main__":
    main()
