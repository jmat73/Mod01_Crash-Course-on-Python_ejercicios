def count_letters(text):
  result = []
  dicc_conteo = {}
  lst_100_wrd_most_used = "De,La,Que,El,En,Y,A,Los,Se,Del,Las,Un,Por,Con,No,Una,Su,Para,Es,Al,Lo,Como,Más,O,Pero,Sus,Le,Ha,Me,Si,Sin,Sobre,Este,Ya,Entre,Cuando,Todo,Esta,Ser,Son,Dos,También,Fue,Había,Era,Muy,Años,Hasta,Desde,Está,Mi,Porque,Qué,Sólo,Han,Yo,Hay,Vez,Puede,Todos,Así,Nos,Ni,Parte,Tiene,Él,Uno,Donde,Bien,Tiempo,Mismo,Ese,Ahora,Cada,E,Vida,Otro,Después,Te,Otros,Aunque,Esa,Eso,Hace,Otra,Gobierno,Tan,Durante,Siempre,Día,Tanto,Ella,Tres,Sí,Dijo,Sido,Gran,País,Según,Menos"
  lst_100_wrd_most_used =  lst_100_wrd_most_used.lower()
  print(lst_100_wrd_most_used)


  char_not_valid = "=" "'" "!" "¡" "?" "¿" "." "+" "-" "," ":" "-" "_"    # Prepare the string for count 
  for i in range(len(char_not_valid)):                            # Checking if the characters not valid for the count
    text = text.replace(char_not_valid[i],"").lower()             # Firts will its erased the charactersnot valid, second convert the string in lowercase
    text ="".join([char for char in text if not char.isdigit()])
    words= text.split(" ")  # Prepare the string erased the numbers for the count
  
  for word in words:
    if word in lst_100_wrd_most_used:
      words.remove(word)
      print(words)

  for word in words:
    if word.isalpha():
      result.append(word)
  
  for word in result:         # Go through each letter in the text
    if word not in dicc_conteo: 
                 # Check if the letter needs to be counted or not
      dicc_conteo[word] = 1
      #print(dicc_conteo)
     
    else:
      dicc_conteo[word] += 1     # Add or increment the value in the dictionary


  return dicc_conteo


print(count_letters("Math y is un para de fun! 2+2=4  y Samuel1 tambien por que samuel2 es top 777 hola 9383 ¿?! lugar lugar hola pedro don quijote mancha lugar donde samuel3 sigie siendo top in samuel "))
