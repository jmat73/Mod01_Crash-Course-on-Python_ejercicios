 # “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):

#Aquí, a pesar de que G.B. Cita de Shaw, nuestros personajes han comenzado con 
#diferentes cantidades de manzanas para que podamos observar mejor los resultados.
#Vamos a hacer que Martin y Johanna intercambien TODAS sus manzanas entre ellos.
#Pista: ¿cómo cambiarías los valores de las variables,
#para que "tú" y "yo" intercambiemos TODAS sus manzanas entre nosotros?
#¿Necesita una variable temporal para almacenar uno de los valores?
#Es posible que necesite más de una línea de código para hacer eso, lo cual está bien. 
    you.apples=johanna.apples
    me.apples=martin.apples
    you.apples, me.apples =me.apples, you.apples
    	
    return you.apples, me.apples
    	
    
def exchange_ideas(you, me): 						#"tú" y "yo" compartiremos nuestras ideas.
    you.ideas= johanna.ideas
    me.ideas = martin.ideas
    ideas_tot = johanna.ideas + martin.ideas
    you.ideas, me.ideas = ideas_tot , ideas_tot #you.ideas 									#Qué operaciones deben realizarse, para que cada objeto reciba el número compartido de ideas? 
    			#¿Necesita una variable temporal para almacenar la suma de ideas, o puedes encontrar otra manera?
													#Use tantas líneas de código como necesite aquí.
    												

    
    
    
exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
