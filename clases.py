from enum import Enum
from patron import Observable, Observador



class Evento(Enum):
	CONTACTO_AGREGADO = 1
	CONTACTO_ELIMINADO = 2
	EVENTO_GENERICO = 3

################################################################################

class Contacto:
	def __init__(self, nombre, telefono):
		self.nombre = nombre
		self.telefono = telefono

	def __str__(self):
		return self.nombre + " - " + self.telefono

################################################################################		

class Agenda(Observable, Observador):
	def __init__(self):
		super().__init__()
		# Agrego la Agenda a la lista de observadores de la clase Observable
		self.agregar_observador(self)
		self.contactos = []

	def get_contactos(self):
		return self.contactos

	def agregar_contacto(self, contacto):
		if contacto not in self.contactos:
			self.contactos.append(contacto)
			self.avisar(Evento.CONTACTO_AGREGADO)

	def eliminar_contacto(self, contacto):
		if contacto in self.contactos:
			self.contactos.remove(contacto)
			self.avisar(Evento.CONTACTO_ELIMINADO)

	def buscar_contacto_por_nombre(self, nombre):
		for contacto in self.contactos:
			if nombre == contacto.nombre:
				return True
		return False

	def buscar_contacto_por_nro(self, numero):
		for contacto in self.contactos:
			if numero == contacto.telefono:
				return True
		return False

	def cantidad_de_contactos(self):
		return len(self.contactos)

	def lista_de_contactos(self):
		return self.contactos

	def __str__(self):
		return " <Agenda> "

	def actualizar(self, obs_origen, evento):
		if evento == Evento.CONTACTO_AGREGADO and obs_origen == self:
			print("Se agregó un contacto a la agenda")
		elif evento == Evento.CONTACTO_ELIMINADO and obs_origen == self:
			print("Se eliminó un contacto de la agenda")
		elif evento == Evento.EVENTO_GENERICO and obs_origen == self:
			print("Se ha recibido un evento genérico")

################################################################################

class EventoGenerico(Observable, Observador):
	def __init__(self):
		super().__init__()
		self.agregar_observador(self)

	def disparar_evento(self):
		self.avisar(Evento.EVENTO_GENERICO)

	def __str__(self):
		return " <EventoGenerico> "

	def actualizar(self, obs_origen, evento):
		if evento == Evento.EVENTO_GENERICO:
			print("Se ha recibido un evento genérico, disparado por la clase <EventoGenerico>")

