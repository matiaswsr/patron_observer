from clases import Agenda, Contacto, EventoGenerico

def iniciar():
	contacto1 = Contacto("Matias", "099000000")
	contacto2 = Contacto("Valeria", "099111111")
	contacto3 = Contacto("Manuela", "099222222")
	contacto4 = Contacto("Marcos", "099333333")
	contacto5 = Contacto("Pablo", "099444444")

	agenda = Agenda()
	agenda.agregar_contacto(contacto1)
	agenda.agregar_contacto(contacto1)
	agenda.agregar_contacto(contacto2)
	agenda.agregar_contacto(contacto3)
	agenda.agregar_contacto(contacto4)
	agenda.agregar_contacto(contacto5)

	agenda.eliminar_contacto(contacto3)
	agenda.eliminar_contacto(contacto3)

	print("")
	print("Contactos de la agenda: ")
	contactos_agenda = agenda.lista_de_contactos()
	for c in contactos_agenda:
		print(c)

	print("")
	evento = EventoGenerico()
	evento.disparar_evento()

	print("")
	print("Lista de Clases Observadoras:")
	lista_obs = agenda.mostrar_observadores()
	for o in lista_obs:
		print(o)



if __name__ == "__main__":
	iniciar()