# Definición de Clases

class Auto():
	def __init__(self, matricula, marca, modelo, anio, precio):
		self.matricula = matricula
		self.marca = marca
		self.modelo = modelo
		self.anio = anio
		self.precio = precio

	def __str__(self):
		return self.matricula + ' | ' + self.marca + ', ' + self.modelo

	def get_matricula(self):
		return self.matricula

	def get_precio(self):
		return str(self.precio)


class Cliente():
	def __init__(self, nombre, apellido, cedula):
		self.nombre = nombre
		self.apellido = apellido
		self.cedula = cedula
		self.autos = []

	def __str__(self):
		return f'{self.cedula} : {self.nombre} {self.apellido}'

	def get_cedula(self):
		return self.cedula

	def get_autos(self):
		return self.autos

	def agregar_auto(self, auto):
		if auto not in self.autos:
			self.autos.append(auto)


class Venta():
	id_venta = 100
	def __init__(self, auto, cliente, precio):
		self.id = Venta.id_venta
		self.auto = auto
		self.cliente = cliente
		self.precio = precio
		Venta.aumentar_id_venta()

	@staticmethod
	def aumentar_id_venta():
		Venta.id_venta += 1

	def __str__(self):
		return f'{self.cliente} - {self.auto} - U$S {self.precio}'

	def get_cliente(self):
		return self.cliente

	def get_precio(self):
		return self.precio

	def get_auto(self):
		return self.auto

	def get_id(self):
		self._id
