from abc import ABC, abstractmethod

# Clase abstracta
class Observador(ABC):
	@abstractmethod
	def actualizar(obs_origen, evento):
		pass




class Observable:
	# Lista para guardar observadores
	observadores = []

	def __init__(self):
		pass

	def agregar_observador(self, obs):
		if isinstance(obs, Observador) and obs not in self.observadores:
			self.observadores.append(obs)

	def eliminar_observador(self, obs):
		if obs in self.observadores:
			self.observadores.remove(obs)

	def avisar(self, evento):
		for obs in self.observadores:
			obs.actualizar(self, evento)

	def mostrar_observadores(self):
		return self.observadores