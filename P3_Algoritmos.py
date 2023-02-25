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

