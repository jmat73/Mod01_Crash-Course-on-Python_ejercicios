def pig_latin(text):
	string = ""
  	# Separate the text into words
	words = text.split(" ")
	print(words) 
	for word in words: # Create the pig latin word and add it to the list
  		first_letter = word[0]
  		rest_word= word[1:] 
  		string = string + rest_word + first_letter+ "ay" + " "

	
    # Turn the list back into a phrase
	return (string)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"








