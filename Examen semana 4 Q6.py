# Complete los espacios en blanco para combinar ambos diccionarios en uno, con cada amigo enumerado solo una vez,y el número de invitados
# del diccionario de Rory tiene prioridad, si se incluye un nombre en ambos diccionarios. Luego imprima el diccionario resultante.

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence

  guests2.update(guests1)
                                                 
  return (guests2)

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))