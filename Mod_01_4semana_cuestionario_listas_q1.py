filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
filenames_new_ext = []
i = 0
for files in filenames:
	if ".hpp" in files:
		sep_ext = files.split(".")  #crear variable separador extension > sep_ext, para separa el archivo de la extension de los files.hpp.
		newfilenames +=[sep_ext[i] +".h"] # unir el archivo a la  nuenva extension e ir añadiendo a la lista nueva.
	
	else:
		newfilenames+= [files]
		
print(newfilenames)

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
