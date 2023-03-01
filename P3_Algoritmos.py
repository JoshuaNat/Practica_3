class Proceso:
	"""Una clase simple para almacenar procesos"""

	def __init__(self, nombre, t_eje, prioridad):
		"""Inicializa los atributos de la clase"""
		self.nombre = nombre
		self.t_eje = t_eje
		self.prioridad = prioridad
		self.t_lle = 0 #Instante en que llegan al procesador
		self.t_esp = 0 #Tiempo en el que estan inactivos
		self.t_res = 0 #Momento en el que entran al procesador
		self.t_ret = 0 #Tiempo de Ejecución + Tiempo de Espera
		self.t_fin = 0 #Momento en el que terminan de trabajar

	def get_tabla(self):
		"""Imprime una tabla"""
		tabla = f"|{self.nombre}|Lle: {self.t_lle}|Esp: {self.t_esp}|Resp: {self.t_res}|Eje: {self.t_eje}|Ret: {self.t_ret}|Fin: {self.t_fin}|"
		return tabla

	def update_tiempos(self, espera, respuesta, retorno, finalizacion):
		"""Actualiza los tiempos de los procesos"""

		self.t_esp = espera #Tiempo en el que estan inactivos
		self.t_res = respuesta #Momento en el que entran al procesador
		self.t_ret = retorno #Tiempo de Ejecución + Tiempo de Espera
		self.t_fin = finalizacion #Momento en el que terminan de trabajar

#Lista de procesos
cola = []

def lista_procesos(filename):
	"""Función para obtener la lista de procesos"""
	with open(filename) as file_obj:
		for procesos in file_obj:
			valor = procesos.split(",")
			cola.append(Proceso(valor[0], int(valor[1]), int(valor[2])))

def FCFS():
	t_actual = 0
	for obj in cola:
		resp = t_actual
		t_actual += obj.t_eje
		fin = t_actual
		ret = fin - obj.t_lle
		esp = ret - obj.t_eje
		obj.update_tiempos(esp, resp, ret, fin)
		print(obj.get_tabla())


def SJB():
	shortest = cola.copy()
	shortest.sort(key=lambda x: x.t_eje)
	t_actual = 0
	for obj in shortest:
		resp = t_actual
		t_actual += obj.t_eje
		fin = t_actual
		ret = fin - obj.t_lle
		esp = ret - obj.t_eje
		obj.update_tiempos(esp, resp, ret, fin)
		print(obj.get_tabla())

def Priority():
	prio = cola.copy()
	prio.sort(key=lambda x: x.prioridad)
	t_actual = 0
	for obj in prio:
		resp = t_actual
		t_actual += obj.t_eje
		fin = t_actual
		ret = fin - obj.t_lle
		esp = ret - obj.t_eje
		obj.update_tiempos(esp, resp, ret, fin)
		print(obj.get_tabla())

def Round_Robin():
	rr = cola.copy()
	t_actual = 0
	q=3
	q_actual=0
	for obj in rr:
		if obj.t_eje <= q:
			resp = t_actual
			t_actual += obj.t_eje
			fin = t_actual
			ret = fin - obj.t_lle
			esp = ret - obj.t_eje
			q_actual += obj.t_eje
			obj.update_tiempos(esp, resp, ret, fin)
			print(obj.get_tabla())

def menu():
	print("Seleccione un algoritmo")
	print("1) FCFS")
	Round_Robin()
        
lista_procesos("procesos.txt")
menu()

