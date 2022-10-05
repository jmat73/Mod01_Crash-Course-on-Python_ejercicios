#Tenemos dos muebles: una mesa de madera marrón y un sofá de cuero Complete los espacios en blanco después de la creación de cada instancia de
#clase de Muebles, de modo que la función describe_muebles pueda formatear una oración que describa estas piezas de la siguiente manera: "Esta pieza de 
#mueble está hecha de muebles de clase de {color} {material}"

	color = ""
	material = ""

table = Furniture()
___
___

couch = Furniture()
___
___

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"
