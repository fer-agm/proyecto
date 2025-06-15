# # # 1. Mantención de Maestros.

pacientes = {}
farmacos = {}
insumos = {}
productos = {}
prestaciones = {}
proveedores = {}

def crear_maestro(maestro,codigo,descripcion):
    maestro[codigo] = {"descripcion":descripcion,"estado": "activo"}

def mod_maestro(maestro,codigo,descrpcion_nueva):
    if codigo in maestro:
        maestro[codigo]["descripcion"] = descrpcion_nueva

def bloq_maestro(maestro,codigo):
    if codigo in maestro:
        maestro[codigo]["estado"] = "bloqueado"

# # # 2. Inventario.
inventario_farm = {}
inventario_insu = {}

def pedido(producto,cantidad,inventario):
    inventario[producto] = inventario.get(producto,0)+cantidad

def entrega(producto,cantidad,costo,inventario,costos):
    inventario[producto] = inventario.get(producto,0)+cantidad
    costos[producto] = costo

def reporte_inv(inventario):
    for prod,cant in inventario.items():
        print(f"{prod}: {cant}")

def reporte_compra(inventario,maestro):
    for codigo,datos in maestro.items():
        print("Hay que comprar:")
        if inventario.get(codigo,0)<3:
            print(f'{codigo}: {datos["descripcion"]}')

# # # 3. Producción.
composicion = {}
stock_prod_terminados = {}
costo_farm = {}
costo_insu = {}
costo_prod_terminados = {}


def crear_composiicon(prod_terminado,componentes):
    composicion[prod_terminado] = componentes

def orden_prod(prod_terminado,cantidad):
    return{f"producto":prod_terminado,"cantidad":cantidad}

def fabricar(orden):
    prod = orden["producto"]
    cant = orden["cantidad"]
    if prod in composicion:
        for comp, cant_comp in composicion[prod].items():
            if comp in inventario_farm:
                inventario_farm[comp] -= cant_comp*cant
            elif comp in inventario_insu:
                inventario_insu[comp] -= cant_comp*cant

        stock_prod_terminados[prod] = stock_prod_terminados.get(prod,0) + cant

def reporte_stock_prod_terminados():
    print("Productos terminados:")
    for prod, cant in stock_prod_terminados.items():
        print(f"{prod}: {cant}")

# # # 4. Ventas.

episodios = []
costo_prest = []

def crear_ep(fecha,paciente):
    episodio = {"fecha":fecha,"paciente":paciente,"items":[]}
    episodios.append(episodio)
    return episodio


def asignar_atencion(episodio,tipo,codigo,cantidad,costo_unitario):
    episodio["items"].append({"tipo":tipo,"codigo":codigo,"cantidad":cantidad,"costo_unitario":costo_unitario})


def calc_precio_att(episodio):
    costo_total = 0
    venta_total = 0

    for item in episodio["items"]:
        costo = item["costo_unitario"]*item["cantidad"]
        if item["tipo"] == "producto_terminado":
            venta = costo * 0.6
        elif item["tipo"] == "farmaco":
            venta = costo *0.5
        elif item["tipo"] == "insumo":
            venta = costo* 0.4
        elif item["tipo"] == "prestacion":
            venta = costo*0.55

        costo_total +=costo
        venta_total += venta

    return costo_total,venta_total,venta_total-costo_total
    

def reporte_vent(since,until):
    for ep in episodios:
        if since <= ep["fecha"] <= until:
            costo,venta,margen = calc_precio_att(ep)
            print(f"Episodio:{ep['fecha']}. \nPaciente:{ep['paciente']}.\nVenta: {venta:.2f}.\nMargen:{margen:.1f}")

# # # Menú interactivo.
def menu_mant():
    seguir = True
    while seguir:
        print("Menú de mantención de maestros")
        menu=input("\n1. Pacientes\n2. Fármacos.\n3. Insumos.\n4. Productos terminados.\n5. Prestaciones.\n6. Proveedores.\n7. Volver.\n")
        if menu == "7":
            seguir = False

    match menu:
        case "1": # PAciente.
            maestro=pacientes
            
            que=input("\n1. Crear-\n2. Modificar.\n3. Bloquear.\n4. Volver\n")
            match que:
                case "1": # crear
                    print("Crear paciente.")
                    codigo = input("Ingrese código para paciente: ")
                    descripcion = input("Ingrese descripción: ")
                    crear_maestro(maestro,codigo,descripcion)

                case "2": # modificar.
                    print("modificar paciente.")

                    codigo = input("Ingrese código nuevo para paciente: ")
                    descripcion = input("Ingrese nueva descripción: ")
                    mod_maestro(maestro,codigo,descripcion)

                case "3": # bloquear
                    print("bloquear paciente.")
                    codigo=input(f"Ingrese código de {maestro} a bloquear.")
                    bloq_maestro(maestro,codigo)
                    print("paciente bloqueado")
                case "4": # volver
                    pass
                case _:
                    print("Opción inválida.")

        case "2": # fármaco
            maestro=farmacos

            que=input("\n1. Crear-\n2. Modificar.\n3. Bloquear.\n4. Volver\n")
            match que:
                case "1": # crear
                    print("Crear fármaco.")
                    codigo = input("Ingrese código para fármaco: ")
                    descripcion = input("Ingrese descripción: ")
                    crear_maestro(maestro,codigo,descripcion)

                case "2": # modificar.
                    print("Modificar fármaco.")

                    codigo = input("Ingrese código nuevo para fármaco: ")
                    descripcion = input("Ingrese nueva descripción: ")
                    mod_maestro(maestro,codigo,descripcion)

                case "3": # bloquear
                    print("Bloquear fármaco.")

                    codigo=input(f"Ingrese código de {maestro} a bloquear.")
                    bloq_maestro(maestro,codigo)
                    print("fármaco bloqueado")
                case "4": # volver
                    pass
                case _:
                    print("Opción inválida.")



        case "3": # insumo
            maestro=insumos

            que=input("\n1. Crear-\n2. Modificar.\n3. Bloquear.\n4. Volver\n")
            match que:
                case "1": # crear
                    print("Crear insumo.")
                    codigo = input("Ingrese código para insumo: ")
                    descripcion = input("Ingrese descripción: ")
                    crear_maestro(maestro,codigo,descripcion)

                case "2": # modificar.
                    print("Modificar insumo.")

                    codigo = input("Ingrese código nuevo para insumo: ")
                    descripcion = input("Ingrese nueva descripción: ")
                    mod_maestro(maestro,codigo,descripcion)

                case "3": # bloquear
                    print("Bloquear insumo.")

                    codigo=input(f"Ingrese código de {maestro} a bloquear.")
                    bloq_maestro(maestro,codigo)
                    print("insumo bloqueado")
                case "4": # volver
                    pass
                case _:
                    print("Opción inválida.")

        case "4": # producto
            maestro=productos

            que=input("\n1. Crear-\n2. Modificar.\n3. Bloquear.\n4. Volver\n")
            match que:
                case "1": # crear
                    print("Crear producto.")
                    codigo = input("Ingrese código para producto: ")
                    descripcion = input("Ingrese descripción: ")
                    crear_maestro(maestro,codigo,descripcion)

                case "2": # modificar.
                    print("Modificar producto")
                    codigo = input("Ingrese código nuevo para producto: ")
                    descripcion = input("Ingrese nueva descripción: ")
                    mod_maestro(maestro,codigo,descripcion)

                case "3": # bloquear
                    print("Bloquear producto")
                    codigo=input(f"Ingrese código de {maestro} a bloquear.")
                    bloq_maestro(maestro,codigo)
                    print("producto bloqueado")

                case "4": # volver
                    pass
                case _:
                    print("Opción inválida.")

        case "5": # prestación.
            maestro=prestaciones

            que=input("\n1. Crear-\n2. Modificar.\n3. Bloquear.\n4. Volver\n")
            match que:
                case "1": # crear
                    print("Crear prestación.")
                    codigo = input("Ingrese código para prestación: ")
                    descripcion = input("Ingrese descripción: ")
                    crear_maestro(maestro,codigo,descripcion)

                case "2": # modificar.
                    print("Modificar prestación.")

                    codigo = input("Ingrese código nuevo para prestación: ")
                    descripcion = input("Ingrese nueva descripción: ")
                    mod_maestro(maestro,codigo,descripcion)

                case "3": # bloquear
                    print("Bloquear prestación.")

                    codigo=input(f"Ingrese código de {maestro} a bloquear.")
                    bloq_maestro(maestro,codigo)
                    print("prestación bloqueada")
                case "4": # volver
                    pass
                case _:
                    print("Opción inválida.")

        case "6": # proveedor
            maestro=proveedores

            que=input("\n1. Crear-\n2. Modificar.\n3. Bloquear.\n4. Volver\n")
            match que:
                case "1": # crear
                    print("Crear proveedor.")
                    codigo = input("Ingrese código para proveedor: ")
                    descripcion = input("Ingrese descripción: ")
                    crear_maestro(maestro,codigo,descripcion)

                case "2": # modificar.
                    print("Modificar proveedor.")
                    codigo = input("Ingrese código nuevo para proveedor: ")
                    descripcion = input("Ingrese nueva descripción: ")
                    mod_maestro(maestro,codigo,descripcion)

                case "3": # bloquear                    
                    print("Bloquear proveedor.")

                    codigo=input(f"Ingrese código de {maestro} a bloquear.")
                    bloq_maestro(maestro,codigo)
                    print("proveedor bloqueado")
                case "4": # volver
                    pass
                case _:
                    print("Opción inválida.")

        case "7": # Salir.
            seguir = False



def menu_inventario():
    seguir=True
    while seguir:
        que=input("\nInventario.\n1. Pedidos a proveedores.\n2.Recepción de fármacos e insumos clínicos.\n3. Lista de stock.\n4. Reporte de producto a comprar.\n5. Volver.")
        match que:
            case "1":
                producto= input("Código del producto: ")
                cantidad = int(input("Cantidad de pedir: "))
                tipo = input("\n1. Fármaco.\n2. Insumo. ")
                if tipo == "1":
                    pedido(producto, cantidad,inventario_farm)
                elif tipo == "2":
                    pedido(producto,cantidad,inventario_insu)
                else:
                    print("Opción inválida.")

            case "2":
                producto = input("Ingrese código de producto: ")
                cantidad = int(input("Ingrese cantidad de productos: "))
                costo = float(input("Costo unitario: $"))
                tipo = input("\n1. Fármaco.\n2. Insumo. ")
                if tipo == "1":
                    entrega(producto,cantidad,costo,inventario_farm,costo_farm)
                elif tipo == "2":
                    entrega(producto,cantidad,costo,inventario_insu,costo_insu)
                else:
                    print("Opción inválida.")
            
            case "3":
                print("\nStock fármacos:")
                reporte_inv(inventario_farm)
                print("\nStock insumos")
                reporte_inv(inventario_insu)

            case "4":
                print("Fármacos a comprar: ")
                reporte_compra(inventario_farm,farmacos)
                print("Insumos a comprar: ")
                reporte_compra(inventario_insu,insumos)

            case "5":
                print("Saliendo...")
                seguir = False

            case _:
                print("Opción inválida.")
        
def menu_produccion():
    seguir=True
    continuar = True
    componentes = {}
    while seguir:
        que=input("\n1. Crear compoisición producto terminado.\n2. Crear oden y fabricar.\n3. Reporte stock productos terminados.\n4. Volver.\n")
        
        match que:
            case "1":
                prod = input("Código producto terminado: ")
                print("Ingrese código y cantidad, o 'fin' para terminar.")
                continuar = True
                while continuar:
                    comp=input("Ingrese código del componente: ")
                    if comp.lower()=="fin":
                        continuar = False
                    
                    try:
                        cant = float(input("Cantidad: "))
                        if cant==int(cant):
                            cant=int(cant)
                    except ValueError:
                        print("Cantidad inválida.")
                        continue
                    componentes[comp]=cant
                crear_composiicon(prod,componentes)
                print("Composición creada")

            case "2":
                prod=input("Código producto terminado: ")
                try:
                    cant=int(input("Cantidad de fabricar: "))
                except ValueError:
                    print("Cantidad inválida.")
                    continue
                orden = orden_prod(prod,cant)
                fabricar(orden)
                print("Fabricación realizada.")

            case "3":
                reporte_stock_prod_terminados()
            case "4":
                pass
            case _:
                print("Opción inválida.")


def menu_ventas():
    seguir=True
    while seguir:
        que=input("\n1. Crear episodio.\n2. Asignar atención.\n3. Calcular precio atención.\n4. Reporte de ventas.\n5. Volver.\n")

        match que:
            case "1":
                fecha = input("Ingrese fecha: (AAAA-MM-DD): ")
                paciente = input("Ingrese código del paciente: ")
                if paciente in pacientes:
                    crear_ep(fecha,paciente)
                    print("Episodio creado.")
                else:
                    print("Paciente no existe.")
            case "2":
                if not episodios:
                    print("No hay episodios creados.")
                else:
                    for i,ep in enumerate(episodios):
                        print(f"{i+1}. Fecha: {ep['fecha']}, Paciente: {ep['paciente']}")
                        try:
                            num_i=int(input("Seleccione episodio: "))-1
                            if num_i<0 or num_i>len(episodios):
                                print("Índice inválido.")
                                continue
                        except ValueError:
                            print("Valor inválido.")

                        ep = episodios[num_i]
                        tipo=input("Tipo (producto_terminado/farmaco/insumo/prestacion): ").lower()
                        codigo = input("Código: ")
                        try:
                            cantidad=int(input("Cantidad: "))
                            costo_unidad = float(input("Costo x unidad: "))
                        except ValueError:
                            print("Cantidad o costo inválidos.")
                            continue
                        asignar_atencion(ep,tipo,codigo,cantidad,costo_unidad)
                        print("Atención asignada.")
            case "3":
                if not episodios:
                    print("No hay episodios creados.")
                    
                for i,ep in enumerate(episodios):
                    print(f"{i+1}. Fecha: {ep['fecha']}. Paciente: {ep['paciente']}")
                    try:
                        num_i = int(input("Seleccione episodio (número)"))-1
                        if num_i<0 or num_i>len(episodios):
                            print("Índice inválido.")
                            continue
                    except ValueError:
                        print("Entrada inválida.")

                    ep=episodios[num_i]
                    costo,venta,margen = calc_precio_att(ep)
                    print(f"Costo total: {costo:.1f}.\nVenta total: {venta:.1f}.\nMargen: {margen:.1f}\n")
            case "4":
                since=input("Fecha desde (AAAA-MM-DD): ").strip()
                until = input("Fecha hasta (AAAA-MM-DD); ").strip()
                reporte_vent(since,until)
            case "5":
                seguir = False

            case _:
                print("Opción inválida.")


def menu_principal():
    terminar = False
    while not terminar:
        que = input("\nMenú principal.\n1. Mantención de maestros.\n2. Inventario.\n3. Producción.\n4. Ventas.\n5. Salir\n")
        match que:
            case "1":
                menu_mant()
            case "2":
                menu_inventario()
            case "3":
                menu_produccion()
            case "4":
                menu_ventas()
            case "5":
                print("Saliendo...")
                terminar = True
            case _:
                print("Opción no válida.")


menu_principal()







