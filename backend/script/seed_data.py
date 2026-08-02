# CONSTANTES para inserción de datos de tablas catalogos

ESTADOS_PEDIDO = [
    {
        "nombre_estado_pedido": "CREADO", 
        "orden": 1
    },
    {
        "nombre_estado_pedido": "RECIBIDO",
        "orden": 2
    },
    {
        "nombre_estado_pedido": "EN_PREPARACION",
        "orden": 3
    },
    {
        "nombre_estado_pedido": "EN_TRANSITO",
        "orden": 4
    },
    {
        "nombre_estado_pedido": "ENTREGADO",
        "orden": 5
    },
    {
        "nombre_estado_pedido": "FINALIZADO",
        "orden": 6
    },
    {
        "nombre_estado_pedido": "CANCELADO",
        "orden": 7
    },
    {
        "nombre_estado_pedido": "DEVUELTO",
        "orden": 8
    },
    {
        "nombre_estado_pedido": "PARA_CAMBIO",
        "orden": 9
    },
    {
        "nombre_estado_pedido": "AUSENTE",
        "orden": 10
    }
]

TIPOS_INCIDENCIA = [
    {
        "nombre_incidencia": "LOGISTICA"
    },
    {
        "nombre_incidencia": "PAGO"
    },
    {
        "nombre_incidencia": "TECNICA"
    }
]

ESTADOS_INCIDENCIA = [
    {
        "nombre_estado_incidencia": "ABIERTA"
    },
    {
        "nombre_estado_incidencia": "EN_PROCESO"
    },
    {
        "nombre_estado_incidencia": "RESUELTA"
    },
    {
        "nombre_estado_incidencia": "SIN_RESOLUCION"
    }
]

TIPOS_GESTION = [
    {
        "nombre_gestion": "CONTACTO_CLIENTE"
    },
    {
        "nombre_gestion": "RESOLUCION_TECNICA"
    },
    {
        "nombre_gestion": "REEMBOLSO"
    },
    {
        "nombre_gestion": "CAMBIO_PRODUCTO"
    },
    {
        "nombre_gestion": "ESCALAMIENTO_SUPERVISOR"
    },
    {
        "nombre_gestion": "GESTION_LOGISTICA"
    }
]

PRODUCTOS_POR_CATEGORIA = {
    "Tecnología": [
        "Smartphone",
        "Notebook",
        "Auriculares",
        "Cámara",
        "Smart TV",
        "Smartwatch",
        "Parlante Bluetooth",
        "Consola de videojuegos",
        "Tablet",
        "Impresora"
    ],
    "Hogar": [
        "Cafetera",
        "Aspiradora",
        "Plancha",
        "Secador de pelo",
        "Batidora",
        "Microondas",
        "Refrigerador",
        "Cocina",
        "Lavadora",
        "Pava eléctrica",
        "Aire acondicionado",
        "Calefactor",
        "Air Fryer"
    ],
    "Indumentaria": [
        "Zapatillas",
        "Camiseta",
        "Remera",
        "Pantalón",
        "Buzo",
        "Vestido",
        "Campera",
        "Bermuda",
        "Gorra"
    ],
    "Deportes": [
        "Bicicleta",
        "Patineta",
        "Pelota de fútbol",
        "Raqueta de tenis",
        "Pelota de tenis",
        "Pelota de golf",
        "Raqueta de pádel",
        "Guantes de boxeo",
        "Pelota de vóley",
        "Balón de baloncesto",
        "Pelota de Rugby",
        "Paleta de ping pong",
        "Cuerda para saltar"
    ],
    "Juguetes": [
        "Auto de juguete",
        "Camión de juguete",
        "Avión de juguete",
        "Barco de juguete",
        "Tren de juguete",
        "Muñeco de acción",
        "Casa de muñecas",
        "Muñeca",
        "Peluche",
        "Ladrillitos de construcción",
        "Alfombra de juegos",
        "Set de arte y manualidades",
        "Rompecabezas",
        "Juego de mesa",
        "Set de cocina para niños",
        "Set de herramientas para niños",
    ],
    "Salud y Belleza": [
        "Perfume",
        "Crema hidratante",
        "Maquillaje",
        "Cepillo de dientes eléctrico",
        "Afeitadora eléctrica",
        "Plancha de pelo",
        "Secador de pelo",
        "Masajeador",
        "Set de manicura",
        "Set de pedicura",
        "Set de cuidado facial",
        "Set de cuidado corporal",
        "Set de cuidado capilar"
    ],
    "Librería": [
        "Libro de aventuras",
        "Novela romántica",
        "Libro de ciencia ficción",
        "Libro de misterio",
        "Libro de fantasía",
        "Libro de historia",
        "Libro de cocina",
        "Libro de autoayuda",
        "Libro de desarrollo personal",
        "Libro de negocios"
    ]
}

RANGOS_COSTOS = {
    "Tecnología": (100000.00, 500000.00),
    "Hogar": (100000.00, 300000.00),
    "Indumentaria": (50000.00, 150000.00),
    "Deportes": (50000.00, 200000.00),
    "Juguetes": (30000.00, 100000.00),
    "Salud y Belleza": (20000.00, 80000.00),
    "Librería": (10000.00, 50000.00)
}


LOCALIDADES_POR_PROVINCIA = {
    "Córdoba": [
        {
            "ciudad": "Córdoba",
            "codigo_postal": "5000"
        },
        {
            "ciudad": "Rio Cuarto",
            "codigo_postal": "5800"
        },
        {
            "ciudad": "Villa María",
            "codigo_postal": "5900"
        },
        {
            "ciudad": "Cruz del Eje",
            "codigo_postal": "5280"  
        },
        {
            "ciudad": "La Falda",
            "codigo_postal": "5172"
        },
        {
            "ciudad": "Cosquin",
            "codigo_postal": "5166"
        },
        {
            "ciudad": "La Cumbre",
            "codigo_postal": "5178"
        },
        {
            "ciudad": "Santa Rosa de Calamuchita",
            "codigo_postal": "5196"
        },
        {
            "ciudad": "Mina Clavero",
            "codigo_postal": "5889"
        },
        {
            "ciudad": "Villa Carlos Paz",
            "codigo_postal": "5152"
        },
        {
            "ciudad": "La Calera",
            "codigo_postal": "5152"
        }
    ],
    "Buenos Aires": [
        {
            "ciudad": "Lanus",
            "codigo_postal": "1824"
        },
        {
            "ciudad": "Morón",
            "codigo_postal": "1708"
        },
        {
            "ciudad": "Avellaneda",
            "codigo_postal": "1870"
        },
        {
            "ciudad": "Tandil",
            "codigo_postal": "7000"
        },
        {
            "ciudad": "Ezpeleta",
            "codigo_postal": "1882"
        },
        {
            "ciudad": "La Plata",
            "codigo_postal": "1900"
        },
        {
            "ciudad": "Mar del Plata",
            "codigo_postal": "7600"
        },
        {
            "ciudad": "Bahía Blanca",
            "codigo_postal": "8000"
        },
        {
            "ciudad": "Quilmes",
            "codigo_postal": "1878"
        }
    ],
    "Santa Fe": [
        {
            "ciudad": "Santa Fe",
            "codigo_postal": "3000"
        },
        {
            "ciudad": "Rosario",
            "codigo_postal": "2000"
        },
        {
            "ciudad": "Rafaela",
            "codigo_postal": "2300"
        },
        {
            "ciudad": "Venado Tuerto",
            "codigo_postal": "2600"
        },
        {
            "ciudad": "San Lorenzo",
            "codigo_postal": "2200"
        }
    ]
}

CODIGOS_AREA = {
    "Córdoba": {
        "codigo" : "351",
        "digitos" : 7
    },
    "Buenos Aires": {
        "codigo" : "11",
        "digitos" : 8
    },
    "Santa Fe": {
        "codigo" : "342",
        "digitos" : 7
    }
}

BARRIOS_POR_PROVINCIA = {
    "Córdoba" : [
        "Nueva Córdoba",
        "Centro",
        "San Martín",
        "Las Margaritas",
        "Alta Córdoba",
        "Jardín",
        "Alberdi",
        "Güemes",
        "Gral. Paz",
        "Juniors",
        "Alto Verde",
        "Los Paraísos",
        "Las Magnolias",
        "Cerro de las Rosas",
        "Poeta Lugones",
        "San Vicente",
        "Yapeyú"
    ],
    "Santa Fe" : [
        "Candioti",
        "Cabaña Leiva",
        "San José",
        "Chalet",
        "Roma",
        "El Pozo",
        "Colastiné Norte"
    ],
    "Buenos Aires" : [
        "Las Flores",
        "Wilde",
        "Piñeyro",
        "Barrio Inglés",
        "San José",
        "Barrio Marítimo",
        "Ranelagh",
        "Villa La Florida",
        "Don Bosco",
        "Barrio Parque",
        "Villa Adelina",
        "La Lucila",
        "Carapachay",
        "Villa Sarmiento",
        "Las Lomas"
    ]
}

PESOS_ESTADOS = {
    1: 5,
    2: 7,
    3: 10,
    4: 12,
    5: 25,
    6: 35,
    7: 3,
    8: 1,
    9: 1,
    10: 1
}

DIAS_ENTREGA = {
    "Buenos Aires" : [1, 2],
    "Córdoba" : [3, 4, 5, 6],
    "Santa Fe" : [3, 4, 5, 6]
}

ESTADOS_CON_FECHA_REAL = {
    "ENTREGADO",
    "FINALIZADO",
    "DEVUELTO",
    "PARA_CAMBIO",
    "AUSENTE"
}

FLUJOS_ESTADOS = {
    6: [1, 2, 3, 4, 5, 6],      # FINALIZADO
    7: [1, 2, 7],               # CANCELADO
    8: [1, 2, 3, 4, 5, 8],      # DEVUELTO
    9: [1, 2, 3, 4, 5, 9],      # PARA_CAMBIO
    10: [1, 2, 3, 4, 10]        # AUSENTE
}

TRANSICIONES_ESTADOS = {
    ("CREADO", "RECIBIDO"): (0, 0),
    ("RECIBIDO", "EN_PREPARACION"): (0, 1),
    ("EN_PREPARACION", "EN_TRANSITO"): (1, 2),
    ("ENTREGADO", "FINALIZADO"): (7, 15),
    ("RECIBIDO", "CANCELADO"): (0, 3),
    ("ENTREGADO", "DEVUELTO"): (1, 10),
    ("ENTREGADO", "PARA_CAMBIO"): (1, 10),
    ("EN_TRANSITO", "AUSENTE"): (1, 1)
}

ESTADOS_CON_INCIDENCIA_OBLIGATORIA = {
    7,   # CANCELADO
    8,   # DEVUELTO
    9,   # PARA_CAMBIO
    10   # AUSENTE
}

ESTADOS_CON_INCIDENCIA_ALEATORIA = {
    1, # CREADO
    2, # RECIBIDO
    3, # EN_PREPARACION
    4, # EN_TRANSITO
    5, # ENTREGADO
    6 #FINALIZADO
}

TIPOS_INCIDENCIA_POR_ESTADO = {
    1 : ["TECNICA"],
    2 : ["LOGISTICA", "TECNICA"],
    3 : ["LOGISTICA"],
    4 : ["LOGISTICA"],
    5 : ["LOGISTICA", "TECNICA"],
    6 : ["LOGISTICA", "TECNICA", "PAGO"],
    7 : ["LOGISTICA", "PAGO"],
    8 : ["LOGISTICA", "TECNICA"],
    9 : ["TECNICA"],
    10 : ["LOGISTICA"]
}

PRIORIDAD_INCIDENCIA = {
    1 : [2, 4], # PAGO
    2 : [3, 4], # TECNICA
    3 : [1, 3]  # LOGISTICA
}

TIPOS_GESTION_POR_INCIDENCIA = {
    1: ["RESOLUCION_TECNICA", "REEMBOLSO", "CONTACTO_CLIENTE"],
    2: ["RESOLUCION_TECNICA", "ESCALAMIENTO_SUPERVISOR"],
    3: ["REEMBOLSO", "GESTION_LOGISTICA", "CONTACTO_CLIENTE"]
}

OBSERVACIONES = {
    "CONTACTO_CLIENTE": [
        "Se estableció contacto con el cliente para informar el estado del caso.",
        "Se solicitó información adicional al cliente para continuar con la gestión.",
        "Se confirmó con el cliente la resolución propuesta."
    ],
    "RESOLUCION_TECNICA": [
        "Se aplicó una corrección técnica sobre el inconveniente reportado.",
        "El área técnica verificó y resolvió la incidencia informada.",
        "Se realizaron pruebas y el inconveniente quedó solucionado."
    ],
    "REEMBOLSO": [
        "Se aprobó el reintegro correspondiente al pedido.",
        "Se inició el proceso de devolución del importe abonado.",
        "Se gestionó el reembolso según la política comercial vigente."
    ],
    "CAMBIO_PRODUCTO": [
        "Se autorizó el cambio del producto solicitado por el cliente.",
        "Se coordinó el reemplazo del producto afectado.",
        "Se registró la solicitud de cambio y quedó pendiente de despacho."
    ],
    "ESCALAMIENTO_SUPERVISOR": [
        "La incidencia fue derivada a un supervisor para su análisis.",
        "Se escaló el caso por requerir una resolución excepcional.",
        "El supervisor tomó intervención debido a la complejidad del caso."
    ],
    "GESTION_LOGISTICA": [
        "Se coordinó una nueva distribución del pedido.",
        "Se actualizó la información logística para continuar con la entrega.",
        "Se inició una revisión del circuito logístico del pedido."
    ]
}
