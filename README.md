# proyecto
PROYECTO DE DESARROLLO SISTEMA PARA CLINICA
Una clínica nos ha pedido desarrollar un sistema para la producción y venta a
atenciones a pacientes, el cual debe contar con los siguientes módulos:
1. Mantención de maestros: El cual nos permita mantener (crear, modificar,
bloquear):
a. Pacientes.
b. Fármacos.
c. Insumos clínicos.
d. Productos terminados.
e. Prestaciones médicas.
f. Proveedores.
Cada uno de estos maestros debe tener como mínimo los campos de
código y descripción.
2. Inventario: El cual nos permitirá controlar la existencia de Fármacos e
Insumos clínicos:
a. Pedidos a Proveedores.
b. Recepción de Fármacos e Insumos clínicos (donde se debe actualizar
el costo de los Fármacos e Insumos clínicos ingresados).
c. Lista de stock de Fármacos e Insumos clínicos.
d. Reporte de Fármacos e insumos clínicos a comprar (los que tengan un
stock menos a un mínimo establecido por código).
3. Producción: El cual debe permitir producir productos términos, los cuales se
hacen mezclando fármacos e insumos clínicos:
a. Crear composición de Productos terminados ( donde se debe indicar
los códigos de los fármacos o insumos y la cantidad a utilizar de cada
uno de ellos.
b. Crear Orden de producción: Donde se indicar que producto terminado
a fabricar y la cantidad.
c. Fabricación: Donde se indica la Orden de producción a realizar, lo cual
debe realizar el descuento de las unidades que se ocuparon de
Fármacos e insumos clínicos y aumentar las unidades del producto
terminado que se fabricó.
d. Reporte de Stock Productos Terminados: Reporte que me indique la
cantidad de productos terminados existentes.
4. Ventas: El cual debe permitir registrar las atenciones a los pacientes.
a. Crear el episodio: Se debe registrar la fecha de atención y el paciente
involucrado.
b. Asignar atención: Se debe registrar los productos terminados
utilizados en el paciente, los fármacos o insumos aplicados directos
al paciente, en todos los casos se debe dejar registrado el costo de
cada ítem ingresado.
Además se debe permitir ingresar prestaciones médicas, las cuales
deben pedir el costo de estas.
c. Calcular precio de atención: Se debe solicitar el código de episodio y
determinar el precio de venta de acuerdo a la siguiente tabla:
i. Producto terminado: Es el 60% del costo.
ii. Fármaco : Es el 50% del costo.
iii. Insumos clínicos: Es el 40% del costo.
iv. Prestaciones médicas: Es el 55% del costo.
d. Reporte de Ventas: Se debe generar un reporte de las ventas
(episodio) realizados en un período de tiempo, indicando episodio,
paciente, costo , venta, y margen
