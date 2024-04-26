class Pelicula:
    
    def __init__(self, titulo, duracion, clasificacion_de_edad, director):
        
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion_de_edad = clasificacion_de_edad
        self.director = director
        
    def mostrar_info_pelicula(self):
        pass
        
class Sala: 
    
    def __init__(self, numero_sala, capacidad, tipo_de_proyeccion):
        
        self.numero_sala = numero_sala
        self.capacidad = capacidad
        self.tipo_de_proyeccion = tipo_de_proyeccion
      
class Sesion:
    
    def __init__(self, pelicula: Pelicula, sala: Sala, hora_inicio, precio):
        
        self.pelicula = pelicula
        self.sala = sala
        self.hora_inicio = hora_inicio
        self.precio = precio
        
    """def asignar_pelicula(self, pelicula):
        self.pelicula = pelicula"""
    
class Entrada: 
    
    def __init__(self, sesion: Sesion, asiento, precio):
        
        self.sesion = sesion
        self.asiento = asiento
        self.precio = precio
    
    @property
    def verificar_disponibilidad(self):
        pass
     
class Cine:
        
        def main (self):
            
            lista_pelicula = []
            lista_sala = []
            lista_sesion = []
            
            while True:
            
                print("1. Añadir película.")
                print("2. Añadir sala.")
                print("3. Añadir sesión.")
                print("4. Mostrar cartelera.")
                print("5. Vender entrada.")
                eleccion = int(input())
        
                if eleccion == 1:
                    titulo = input("Nombre película: ")
                    duracion = input("Duración (minutos): ")
                    clasificacion_de_edad = int(input("Clasificación de edad (años): "))
                    director = input("Director: ")
                    
                    lista_pelicula.append(Pelicula(titulo, duracion, clasificacion_de_edad, director))
                
                elif eleccion == 2:
                    numero_sala = int(input("Número de la sala: "))
                    capacidad = int(input("Capacidad de la sala: "))
                    tipo_de_proyeccion = input("Tipo de proyección (2D, 3D, IMAX): ")
                    
                    lista_sala.append(Sala(numero_sala, capacidad, tipo_de_proyeccion))
                    
                elif eleccion == 3:
                    hora_inicio = input("Hora de la sesión: ")
                    precio = float(input("Precio de la sesión: "))
                    num_lista_pelicula = int(input("Indique el número de la posición de la película a añadir (la primera es la 0): "))
                    num_lista_sala = int(input("Indique el número de la sala a añadir (la primera es la 0): "))
                    
                    lista_sesion.append(Sesion(lista_pelicula[num_lista_pelicula], lista_sala[num_lista_sala], hora_inicio, precio))
                    
                elif eleccion == 4:
                    for sesion in lista_sesion:
                        print(f"Pelicula: {sesion.pelicula.titulo} Sala: {sesion.sala.numero_sala} Hora: {sesion.hora_inicio} Precio: {sesion.precio}€.")
                
                elif eleccion == 5:
                    sesion = input("Introduzca el número de la sesión a la que desea asistir(empieza por 0): ")
                    asiento = int(input("Seleccione el asiento: "))
                    
                
                else:
                    print("No es una selección válida.")         
                
Cine().main()