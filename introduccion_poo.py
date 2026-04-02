# 1- EXPLORACIÓN TEÓRICA
# ¿Qué es la POO?: Es un paradigma de programación basado en el concepto de "objetos", 
# que agrupan datos (atributos) y acciones (métodos) en una sola unidad.

# Diferencia con la estructurada: La estructurada se basa en una secuencia lógica de pasos 
# y funciones separadas de los datos, mientras que la POO organiza el código en entidades
# autónomas que interactúan entre sí.

# Ejemplo cotidiano: Un teléfono celular. Tiene atributos (color, modelo, marca) 
# y funciones (llamar, enviar mensaje, tomar foto).




#DEFINICIÓN DE UNA CLASE SIMPLE
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")

# Instancia y llamada al método
mi_perro = Perro("Rex", 3, "Golden Retriever")
mi_perro.ladrar()




#DIFERENCIAR CONCEPTOS
# Clase, instancia y objeto: La clase es el molde o plano (Perro); el objeto es la 
# entidad creada; la instancia es el proceso de crear ese objeto específico.

# Atributo y estado: Los atributos son las variables definidas (nombre, edad); 
# el estado es el valor particular de esos atributos en un momento dado (Rex, 3 años).

# Método y comportamiento: El método es la función definida en el código (ladrar()); 
# el comportamiento es la acción que el objeto realiza cuando se ejecuta ese método.



# PRINCIPIOS DE POO
class Perro:
    def __init__(self, nombre, edad, raza):
        # Atributos encapsulados con prefijo _
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    def ladrar(self):
        print("¡Guau!")

    def mostrar_info(self):
        # Devuelve el estado del objeto
        return f"Perro: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"

# Abstracción: Significa simplificar la realidad enfocándose solo en los detalles 
# relevantes para el sistema. En este ejemplo, ignoramos detalles complejos del perro 
# (como su ADN o sistema digestivo) y solo modelamos lo que nos interesa (nombre, raza).

# Prueba del código modificado
mi_perro_pro = Perro("Luna", 5, "Poodle")
print(mi_perro_pro.mostrar_info())