"""
Este código implementa el patrón Singleton en Python utilizando una metaclase.

Definición de la metaclase SingletonMeta:

Esta es una metaclase que hereda de type, la metaclase básica de Python.
Dentro de esta metaclase, se define un diccionario _instances para mantener las instancias únicas de las clases Singleton.
El método __call__ es un método especial que se ejecuta cuando se crea una nueva instancia de la clase. 
Este método garantiza que una clase Singleton tenga solo una instancia.
Dentro de __call__, se verifica si ya existe una instancia de la clase Singleton en el diccionario _instances. 
Si no existe, se crea una nueva instancia utilizando super().__call__(*args, **kwargs) y se almacena en el 
diccionario _instances. Luego, se devuelve esa instancia.
"""
from clases import Auto, Cliente, Venta


class SingletonMeta(type):
	"""
	La clase Singleton puede ser implementada de diferentes maneras en Python. Algunos
	métodos posibles incluyen: clase base, decorador, metaclase. Utilizaremos la
	metaclase porque es la más adecuada para este propósito.
	"""
	_instances = {}

	def __call__(cls, *args, **kwargs):
		"""
		Los posibles cambios en el valor del argumento '__init__' no afectan
		a la instancia devuelta.
		"""
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]



"""
Con esta implementación la clase ServicioDeVenta es Singleton
"""
class ServicioDeVenta(metaclass=SingletonMeta):	
	def __init__(self):
		self.autos = []
		self.clientes = []
		self.ventas = []

	def agregar_auto(self, auto):
		if auto not in self.autos:
			self.autos.append(auto)

	def agregar_cliente(self, cliente):
		if cliente not in self.clientes:
			self.clientes.append(cliente)

	def agregar_venta(self, venta):
		if venta not in self.ventas:
			self.ventas.append(venta)

	def lista_de_autos(self):
		return self.autos

	def lista_de_clientes(self):
		return self.clientes

	def lista_de_ventas(self):
		return self.ventas

	def existe_cliente_con_ci(self, cedula):
		for c in self.clientes:
			if c.get_cedula() == cedula:
				return True
		return False

	def registrar_cliente(self, nombre, apellido, cedula):
		if not self.existe_cliente_con_ci(cedula):
			cliente = Cliente(nombre, apellido, cedula)
			self.agregar_cliente(cliente)
			return cliente
		return None

	def existe_auto_con_matricula(self, matricula):
		for a in self.autos:
			if a.get_matricula() == matricula:
				return True
		return False

	def registrar_auto(self, matricula, marca, modelo, anio, precio):
		if not self.existe_auto_con_matricula(matricula):
			auto = Auto(matricula, marca, modelo, anio, precio)
			self.agregar_auto(auto)
			return auto
		return None

	def existe_venta(self, auto, cliente):
		for v in self.ventas:
			if auto == v.get_auto() and cliente == v.get_cliente():
				return True
		return False

	def registrar_venta(self, cliente, auto, precio):
		if not self.existe_venta(auto, cliente):
			venta = Venta(auto, cliente, precio)
			cliente.agregar_auto(auto)
			self.agregar_venta(venta)
			return venta
		return None


"""
Con esta implementación la clase Fachada es Singleton
"""
class Fachada(metaclass=SingletonMeta):
	def __init__(self):
		self.servicio = ServicioDeVenta()

	def registrar_cliente(self, nombre, apellido, cedula):
		return self.servicio.registrar_cliente(nombre, apellido, cedula)

	def registrar_auto(self, matricula, marca, modelo, anio, precio):
		return self.servicio.registrar_auto(matricula, marca, modelo, anio, precio)

	def registrar_venta(self, cliente, auto, precio):
		return self.servicio.registrar_venta(cliente, auto, precio)

	def lista_de_autos(self):
		return self.servicio.lista_de_autos()

	def lista_de_clientes(self):
		return self.servicio.lista_de_clientes()

	def lista_de_ventas(self):
		return self.servicio.lista_de_ventas()