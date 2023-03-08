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
	cont = 0
	tam = len(rr)
	for obj in rr:
		cont += 1
		if obj.t_eje <= q:
			resp = q_actual
			t_actual += obj.t_eje
			ret = q_actual + obj.t_eje
			fin = ret
			esp = ret - obj.t_eje
			obj.update_tiempos(esp, resp, ret, fin)
			q_actual += obj.t_eje
			tam -= 1
			print(obj.get_tabla())
		else:
			if obj.t_eje % 3 == 0:
				trozos = obj.t_eje // q -1
			else:
				trozos = obj.t_eje // q
			faltan = tam - cont
			resp = q_actual
			t_actual += obj.t_eje
			q_actual += 3
			fin = t_actual + (q*trozos*tam)
			ret = fin - obj.t_lle
			esp = ret - obj.t_eje
			obj.update_tiempos(esp, resp, ret, fin)
			tam -= 1
			print(obj.get_tabla())

def col_inicio(filename, proceso):
        with open(filename) as file_obj:
                contenido = file_obj.read()
                
        nuevo_cont = proceso + '\n' + contenido
        
        with open(filename, 'w') as file_obj:
                file_obj.write(nuevo_cont)
                
def col_final(filename, proceso):
        with open(filename, "a") as file_obj:
                linea = f"\n{proceso}"
                file_obj.write(linea)

def add_process():
        while True:
                nombre = input("Nombre del proceso: ")
                tiempo = input("Tiempo de duración: ")
                prio = input("Prioridad del proceso: ")
                linea = nombre + ", " + tiempo + ", " + prio
                posi = int(input("1)Colocar al principio\n2)Colocar al final\n3)Cancelar\nSeleccione una opcion: "))
                if posi == 1:
                        col_inicio("procesos.txt", linea)
                        print(f"Se agrego el proceso {nombre} con duracion {tiempo} y prioridad {prio}")
                elif posi == 2:
                        col_final("procesos.txt", linea)
                        print(f"Se agrego el proceso {nombre} con duracion {tiempo} y prioridad {prio}")
                elif posi == 3:
                        break
                else:
                        print("Ingrese una opcion valida")



def menu():
        while True:
                if cola:
                        cola.clear()
                lista_procesos("procesos.txt")
                print("Seleccione un algoritmo")
                print("1)FCFS\n2)SJB\n3)Prioridades\n4) Round Robin\n5)Agregar Proceso\n6)Salir")
                opcion = int(input("Ingrese un numero: "))
                if opcion == 1:
                        FCFS()
                elif opcion == 2:
                        SJB()
                elif opcion == 3:
                        Priority()
                elif opcion == 4:
                        Round_Robin()
                elif opcion == 5:
                        add_process()
                elif opcion == 6:
                        break
                else:
                        print("Ingrese un valor valido")

	
        
menu()

