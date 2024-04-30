# comentario de pruebas
class Hotel:
    
    def __init__(self, habitacion_sencilla = 10, habitacion_doble = 20, habitacion_suite = 5, reservas = None):
        self.habitacion_sencilla = habitacion_sencilla
        self.habitacion_doble = habitacion_doble
        self.habitacion_suite = habitacion_suite
        self.reservas = reservas
    
    def comprobar_disponibilidad(self): 
        
        eleccion_habitacion = input("Disponibilidad de la habitación que desea ver (sencilla, doble o suite): ").lower()
        
        if eleccion_habitacion == 'sencilla':
            habitacion = self.habitacion_sencilla
        elif eleccion_habitacion == 'doble':
            habitacion = self.habitacion_doble
        elif eleccion_habitacion == 'suite':
            habitacion = self.habitacion_suite
        else:
            print("No es una habitación válida.")   
        return habitacion
    
    def restar_habitacion(self):
        
        reserva_habitacion = str(input("Tipo de habitación que quieres reservar: "))
        if reserva_habitacion == 'sencilla':
            self.habitacion_sencilla -= 1
        elif reserva_habitacion == 'doble':
            self.habitacion_doble -= 1
        elif reserva_habitacion == 'suite':
            self.habitacion_suite -= 1
            
    # retocar poniendo que tiene que ser mayor que 0 el numero de habitaciones disponibles 
    
class Habitacion:
    
    def __init__(self, precio, orientacion, categoria):
        self.precio = precio
        self.orientacion = orientacion
        self.categoria = categoria 
        
    def precio_con_descuento(self, precio, precio_con_descuento):
        
        self.precio = precio * 0.85
        return precio_con_descuento
            
class Cliente:
    
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre 
        self.apellidos = apellidos
        self.dni = dni
    
def dar_alta_cliente():
    
    nombre = str(input("Nombre: "))
    apellidos = str(input("Apellidos: "))
    dni = str(input("DNI: "))
    return Cliente(nombre, apellidos, dni)
        
class Reserva:
    
    def __init__(self, fecha, cliente, tipo_habitacion):
        self.fecha = fecha
        self.cliente = cliente
        self.tipo_habitacion = tipo_habitacion      
    
class App: 

    def main(self):
    
        lista_clientes = []
        hotel = Hotel()
        
        while True:
            
            print("1. Dar de alta a un cliente.")
            print("2. Comprobar disponibilidad habitación.")
            print("3. Realizar reserva.")
            print("4. Cerrar aplicación.")
            opcion = int(input("Elige una opción: "))
            
            if opcion == 1:
                lista_clientes.append(dar_alta_cliente())
                
            elif opcion == 2:
                ver_disponibilidad = hotel.comprobar_disponibilidad()
                print("Hay", ver_disponibilidad, "habitaciones disponibles.")
                    
            elif opcion == 3:
                for i, cliente in enumerate(lista_clientes):
                    print(f"{i + 1}. Nombre: {cliente.nombre} Apellidos: {cliente.apellidos} DNI: {cliente.dni}")
                    
                cliente_reserva = int(input("Cliente para la reserva: ")) - 1 # porque empieza la lista desde 0
                
                cliente = cliente[cliente_reserva] # ver que pasa 
                hotel.restar_habitacion()
                #reserva = Reserva(cliente, tipo_habitacion, fecha_reserva)
                
            elif opcion == 4:
                print("Cerrando aplicación...")
                break
            
            else:
                print("Elija una opción válida.")
                
App().main()