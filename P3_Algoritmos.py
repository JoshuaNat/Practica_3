class Proceso:
	"""Una clase simple para almacenar procesos"""

	def __init__(self, nombre, t_eje, prioridad):
		"""Inicializa los atributos de la clase"""
		self.nombre = nombre
		self.t_eje = t_eje
		self.prioridad = prioridad
		self.t_lle = 0
		self.t_esp = 0
		self.t_res = 0
		self.t_ret = 0
		self.t_fin = 0

	def get_tabla(self):
		"""Imprime una tabla"""
		tabla = f"|{self.nombre}|{self.t_lle}|{self.t_esp}|{self.t_res}|{self.t_eje}|{self.t_ret}|{self.t_fin}|"
		return tabla

#Lista de procesos
cola = []

def lista_procesos(filename):
	"""Función para obtener la lista de procesos"""
	with open(filename) as file_obj:
		for procesos in file_obj:
			valor = procesos.split(",")
			cola.append(Proceso(valor[0], int(valor[1]), int(valor[2])))

lista_procesos("procesos.txt")
for obj in cola:
	print(obj.get_tabla())