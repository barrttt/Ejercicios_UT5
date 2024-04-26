"""Sobre el ejercicio uno de los productos agroalimentarios, añade la siguiente funcionalidad:

- Sobrescribe la función __str__ para que se imprima la información de cada clase
- Añade las propiedades peso y medidas
- Implementa un método calcular_coste_envio:
- Cualquier producto costará enviarlo una relacionada con su peso: 3 euros por kilo
- Los productos congelados llevan un extra de 5 euros de transporte
- Los productos refrigerados llevan un extra de 2 euros de transporte
- Añade al menú la posibilidad de eliminar un producto. Para ello primero imprime una lista numerada
- Añade al menú la opción de obtener el coste de envío de cualquier producto"""

class Producto:
    
    def __init__(self, fecha_caducidad, numero_lote, peso, medida):
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
        self.peso = peso
        self.medida = medida
    
    def calcular_gastos_envio(self):
        return int(self.peso) * 3 # 3 euros por kilo
        
class Fresco(Producto):
    
    def __init__(self, fecha_caducidad, numero_lote, peso, medida, fecha_envasado, pais_origen):
        super().__init__(fecha_caducidad, numero_lote, peso, medida)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen
    
    def __str__(self):
        return  f"Fecha de caducudad: {self.fecha_caducidad} Número de lote: {self.numero_lote} Peso: {self.peso} Medida: {self.medida} País de origen: {self.pais_origen}"
    
    def calcular_coste_envio(self):
        return super().calcular_gastos_envio() 

class Refrigerado(Producto):
    
    def __init__(self, fecha_caducidad, numero_lote, peso, medida, codigo_supervision):
        super().__init__(fecha_caducidad, numero_lote, peso, medida)
        self.codigo_supervision =codigo_supervision
        
    def __str__(self):
        return f"Fecha de caducidad: {self.fecha_caducidad} Número de lote: {self.numero_lote} Peso: {self.peso} Medida: {self.medida} Código de supervisión: {self.codigo_supervision}"
        
    def calcular_coste_envio_refrigerado(self):
        return super().calcular_gastos_envio() + 2  # 2 euros extra por ser refrigerado
           
class Congelado(Producto):
    
    def __init__(self, fecha_caducidad, numero_lote, peso, medida, temperatura_recomendada):
        super().__init__(fecha_caducidad, numero_lote, peso, medida)
        self.temperatura_recomendada = temperatura_recomendada
    
    def __str__(self):
        return f"Fecha de caducidad: {self.fecha_caducidad} Número de lote: {self.numero_lote} Peso: {self.peso} Medida: {self.medida} Temperatura recomendada: {self.temperatura_recomendada}"
    
    def calcular_coste_envio_congelado(self):  
        return super().calcular_gastos_envio()  + 5 # 5 euros extra por ser congelado
    
def datos_comunes():
    fecha_caducidad = input("Fecha de caducidad:")      
    numero_lote = input("Número de lote: ")
    peso = input("Peso del producto: ")
    medida = input("Medida del producto: ")
    return Producto(fecha_caducidad, numero_lote, peso, medida)

def crear_producto_fresco():
    fresco_temporal = datos_comunes()
    fecha_envasado = input("Fecha de envasado: ")
    pais_origen = input("País de origen: ")
    return Fresco(fresco_temporal.fecha_caducidad, fresco_temporal.numero_lote, fresco_temporal.peso, fresco_temporal.medida, fecha_envasado, pais_origen)

def crear_producto_refrigerado():
    refrigerado_temporal = datos_comunes()
    codigo_supervision = input("Código de supervisión: ")
    return Refrigerado(refrigerado_temporal.fecha_caducidad, refrigerado_temporal.numero_lote, refrigerado_temporal.peso, refrigerado_temporal.medida, codigo_supervision)

def crear_producto_congelado():
    congelado_temporal = datos_comunes()
    temperatura_recomendada = str(input("Temperatura recomendada: "))
    return Congelado(congelado_temporal.fecha_caducidad, congelado_temporal.numero_lote, congelado_temporal.peso, congelado_temporal.medida, temperatura_recomendada)
    
def eliminar_producto(lista):
    if lista:
        for i, producto in enumerate(lista):
            print(f"{i + 1}. {producto}")
        eliminar_producto = int(input("¿Qué producto deseas eliminar?")) - 1
        if 0 <= eliminar_producto < len(lista):
            lista.pop(eliminar_producto)
            print("Producto eliminado.")
        else:
            print("Selecciona un número válido.")
    else:
        print("No hay productos en la lista.")
   
class App:
    
    def main():
        
        lista_frescos = []
        lista_refrigerados = []
        lista_congelados = []
         
        while True:
        
            print("1. Crear producto fresco.")
            print("2. Crear producto refrigerado.")
            print("3. Crear producto congelado.")
            print("4. Mostrar productos.")
            print("5. Eliminar producto de la lista.")
            print("6. Calcular coste de envío.")
            print("7. Cerrar aplicación.")
            opcion = int(input("¿Qué quieres hacer? "))
             
            if opcion == 1:
                producto_fresco = crear_producto_fresco()
                lista_frescos.append(producto_fresco)
            elif opcion == 2:
                producto_refrigerado = crear_producto_refrigerado()
                lista_refrigerados.append(producto_refrigerado)
            elif opcion == 3:
                producto_congelado = crear_producto_congelado()
                lista_congelados.append(producto_congelado)
            elif opcion == 4:
                ver_producto = int(input("Indica el tipo de producto que quieres ver (1(fresco), 2(refrigerado) 0 3(congelado)): "))
                if ver_producto == 1:
                    for i, producto_fresco in enumerate(lista_frescos):
                        print(f"{i + 1}. {producto_fresco}")
                elif ver_producto == 2:
                    for i, producto_refrigerado in enumerate(lista_refrigerados):
                        print(f"{i + 1}. {producto_refrigerado}")
                elif ver_producto == 3:
                    for i, producto_congelado in enumerate(lista_congelados):
                        print(f"{i + 1}. {producto_congelado}")
                else:
                    print("No es una selección válida.")
                        
            elif opcion == 5:
                tipo_producto = int(input("Indica el tipo de producto que quieres eliminar (1-fresco, 2-refrigerado, 3-congelado): "))
                if tipo_producto == 1:
                    eliminar_producto(lista_frescos)
                elif tipo_producto == 2:
                    eliminar_producto(lista_refrigerados)
                elif tipo_producto == 3:
                    eliminar_producto(lista_congelados)
                else:
                    print("Tipo de producto inválido.")

            elif opcion == 6:
                coste_envio_producto = int(input("¿De qué tipo de producto quieres saber los gastos de envío? (1-fresco), (2-refrigerado) o (3-congelado) "))
                if coste_envio_producto == 1:
                    for i, producto_fresco in enumerate(lista_frescos):
                        print(f"{i + 1}. {producto_fresco}")
                    if lista_frescos:
                        envio_fresco = int(input("¿De qué producto quieres saber los gastos de envío? "))
                        if 0 <= envio_fresco <= len(lista_frescos):
                            gasto_envio_fresco = lista_frescos[envio_fresco - 1].calcular_coste_envio()
                            print(f"Los gastos de envío de este producto son: {gasto_envio_fresco} €.")
                        else:
                            print("Selecciona un número válido.")
                    else:
                        print("No hay productos frescos disponibles.")

                elif coste_envio_producto == 2:
                    for i, producto_refrigerado in enumerate(lista_refrigerados):
                        print(f"{i + 1}. {producto_refrigerado}")
                    if lista_refrigerados:
                        envio_refrigerado = int(input("¿De qué producto quieres saber los gastos de envío? "))
                        if 0 <= envio_refrigerado <= len(lista_refrigerados):
                            gasto_envio_refrigerado = lista_refrigerados[envio_refrigerado - 1].calcular_coste_envio_refrigerado()
                            print(f"Los gastos de envío de este producto son: {gasto_envio_refrigerado} €.")
                        else:
                            print("Selecciona un número válido.")
                    else:
                        print("No hay productos refrigerados disponibles.")   

                elif coste_envio_producto == 3:
                    for i, producto_congelado in enumerate(lista_congelados):
                        print(f"{i + 1}. {producto_congelado}")
                    if lista_congelados:
                        envio_congelado = int(input("¿De qué producto quieres saber los gastos de envío? "))
                        if 0 <= envio_congelado <= len(lista_congelados):
                            gasto_envio_congelado = lista_congelados[envio_congelado - 1].calcular_coste_envio_congelado()
                            print(f"Los gastos de envío de este producto son: {gasto_envio_congelado} €.")
                        else:
                            print("Selecciona un número válido.")
                    else:
                        print("No hay productos congelados disponibles.")
                        
            elif opcion == 7:
                print("Cerrando aplicación...")
                break
            else:
                ("Selecciona una opción válida.")
                 
App.main()