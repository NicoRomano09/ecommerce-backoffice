-- Base de Datos --
CREATE DATABASE ecommerce_backoffice;

ALTER DATABASE ecommerce_backoffice
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

-- Tablas --
CREATE TABLE tipo_incidencia (
id_tipo_incidencia INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre_incidencia VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE estado_incidencia (
id_estado_incidencia INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre_estado_incidencia VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE tipo_gestion (
id_tipo_gestion INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre_gestion VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE estado_pedido (
id_estado_pedido INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre_estado_pedido VARCHAR(60) UNIQUE NOT NULL,
orden INT UNIQUE NOT NULL
);

CREATE TABLE cliente (
id_cliente INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
numero_documento VARCHAR(15) UNIQUE NOT NULL,
nombre_cliente VARCHAR(50) NOT NULL,
apellido_cliente VARCHAR(100) NOT NULL,
telefono VARCHAR(20) NOT NULL,
email VARCHAR(100) NOT NULL,
calle VARCHAR(100) NOT NULL,
numero VARCHAR(10) NOT NULL,
depto VARCHAR(5) NULL,
piso VARCHAR(5) NULL,
barrio VARCHAR(50) NULL,
codigo_postal VARCHAR(10) NOT NULL,
ciudad VARCHAR(100) NOT NULL,
provincia VARCHAR(100) NOT NULL
);

CREATE TABLE pedido (
id_pedido INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
fecha_hora_pedido DATETIME NOT NULL,
id_cliente INT NOT NULL,
id_estado_pedido INT NOT NULL,
total DECIMAL(12,2) NOT NULL,
costo_total DECIMAL(12,2) NOT NULL,
fecha_entrega_estimada DATE NOT NULL,
fecha_entrega_real DATE NULL,
CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT fk_pedido_estado_pedido FOREIGN KEY (id_estado_pedido) REFERENCES estado_pedido(id_estado_pedido) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT chk_total_positivo CHECK (total >= 0),
CONSTRAINT chk_costo_positivo CHECK (costo_total >= 0)
);

CREATE TABLE producto (
id_producto INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre_producto VARCHAR(100) NOT NULL,
categoria VARCHAR(50) NOT NULL,
precio_unitario DECIMAL(12,2) NOT NULL,
costo_unitario DECIMAL(12,2) NOT NULL,
CONSTRAINT chk_precio_unitario_positivo CHECK(precio_unitario > 0),
CONSTRAINT chk_costo_unitario_positivo CHECK(costo_unitario > 0)
);

CREATE TABLE detalle_pedido (
id_detalle_pedido INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
id_pedido INT NOT NULL,
id_producto INT NOT NULL,
cantidad INT NOT NULL,
precio_unitario DECIMAL(12,2) NOT NULL,
costo_unitario DECIMAL(12,2) NOT NULL,
CONSTRAINT fk_detalle_pedido_pedido FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
CONSTRAINT fk_detalle_pedido_producto FOREIGN KEY (id_producto) REFERENCES producto(id_producto) ON DELETE RESTRICT,
CONSTRAINT chk_cantidad_positiva CHECK(cantidad>0)
);

CREATE TABLE incidencia (
id_incidencia INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
id_pedido INT NOT NULL,
id_tipo_incidencia INT NOT NULL,
prioridad INT NOT NULL,
id_estado_incidencia INT NOT NULL,
fecha_hora_incidencia DATETIME NOT NULL,
CONSTRAINT fk_incidencia_pedido FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
CONSTRAINT fk_incidencia_tipo_incidencia FOREIGN KEY (id_tipo_incidencia) REFERENCES tipo_incidencia(id_tipo_incidencia) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT fk_incidencia_estado_incidencia FOREIGN KEY (id_estado_incidencia) REFERENCES estado_incidencia(id_estado_incidencia) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT chk_rango_prioridad CHECK(prioridad BETWEEN 1 AND 4)
);

CREATE TABLE gestion (
id_gestion INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
id_incidencia INT NOT NULL,
id_tipo_gestion INT NOT NULL,
observacion TEXT NULL,
fecha_hora_gestion DATETIME NOT NULL,
CONSTRAINT fk_gestion_incidencia FOREIGN KEY (id_incidencia) REFERENCES incidencia(id_incidencia) ON DELETE CASCADE,
CONSTRAINT fk_gestion_tipo_gestion FOREIGN KEY (id_tipo_gestion) REFERENCES tipo_gestion(id_tipo_gestion) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE historial_estado (
id_historial_estado INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
id_pedido INT NOT NULL,
id_estado_pedido INT NOT NULL,
fecha_hora_estado DATETIME NOT NULL,
CONSTRAINT fk_historial_estado_pedido FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
CONSTRAINT fk_historial_estado_estado_pedido FOREIGN KEY (id_estado_pedido) REFERENCES estado_pedido(id_estado_pedido) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Indices --
CREATE INDEX idx_pedido_cliente
ON pedido(id_cliente);

CREATE INDEX idx_pedido_estado
ON pedido(id_estado_pedido);

CREATE INDEX idx_pedido_fecha
ON pedido(fecha_hora_pedido);

CREATE INDEX idx_historial_pedido
ON historial_estado(id_pedido);

CREATE INDEX idx_historial_fecha
ON historial_estado(fecha_hora_estado);

CREATE INDEX idx_incidencia_pedido
ON incidencia(id_pedido);

CREATE INDEX idx_incidencia_estado
ON incidencia(id_estado_incidencia);

CREATE INDEX idx_incidencia_tipo
ON incidencia(id_tipo_incidencia);

CREATE INDEX idx_gestion_incidencia
ON gestion(id_incidencia);

CREATE INDEX idx_gestion_tipo
ON gestion(id_tipo_gestion);

CREATE INDEX idx_dashboard
ON pedido(fecha_hora_pedido,id_estado_pedido);