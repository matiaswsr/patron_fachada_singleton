from fachada import ServicioDeVenta, Fachada

if __name__ == "__main__":

	s1 = ServicioDeVenta()
	s2 = ServicioDeVenta()

	f1 = Fachada()
	f2 = Fachada()
	f3 = Fachada()

	# Probando el patrón Singleton
	if id(s1) == id(s2):
		print("(ServicioDeVenta) Singleton OK!, ambas instancias son la misma")
	else:
		print("(ServicioDeVenta) Singleton FALLÓ!, las instancias son diferentes")

	if id(f1) == id(f2) and id(f3) == id(f1):
		print("(Fachada) Singleton OK!, todas las instancias son la misma")
	else:
		print("(Fachada) Singleton FALLÓ!, las instancias son diferentes")


	# Registrar Clientes, Autos y Ventas
	c1 = f1.registrar_cliente("Matias","Santos","111")
	c2 = f3.registrar_cliente("Manuela","Santos","222")	
	c3 = f1.registrar_cliente("Jaime","Lopez","333")
	c4 = f3.registrar_cliente("Andrea","Soria","444")
	c5 = f2.registrar_cliente("Laura","Pereira","555")

	c6 = f3.registrar_cliente("Manuela","Santos","222")
	c7 = f3.registrar_cliente("Manuela","Santos","222")
	

	print("")
	print("Clientes registrados:")
	lista_clientes = f1.lista_de_clientes()
	for c in lista_clientes:
		print(c)

	a1 = f1.registrar_auto("AA11", "Audi", "A6", "2024", 45000)
	a2 = f3.registrar_auto("BB11", "BMW", "Z6", "2024", 63000)
	a3 = f2.registrar_auto("CC11", "Morris", "Mini Morris", "2023", 43000)
	a4 = f1.registrar_auto("DD11", "Mercedes Benz", "Coupe", "2024", 73000)

	a5 = f2.registrar_auto("DD11", "Mercedes Benz", "Coupe", "2024", 73000)
	a6 = f1.registrar_auto("BB11", "BMW", "Z6", "2024", 63000)

	print("")
	print("Autos registrados:")
	lista_autos = f3.lista_de_autos()
	for a in lista_autos:
		print(a)

	v1 = f1.registrar_venta(c1, a1, a1.get_precio())
	v2 = f1.registrar_venta(c1, a2, a2.get_precio())
	v3 = f2.registrar_venta(c2, a3, a3.get_precio())
	v4 = f3.registrar_venta(c3, a4, a4.get_precio())
	
	v5 = f2.registrar_venta(c1, a2, a2.get_precio())
	v6 = f3.registrar_venta(c1, a2, a2.get_precio())

	print("")
	print("Ventas registradas:")
	lista_ventas = f2.lista_de_ventas()
	for v in lista_ventas:
		print(v)

	print("")
	print("Autos de: \n" + str(c1))
	for auto in c1.get_autos():
		print(auto)