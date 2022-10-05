def count_letters(text):
  result = {}

  char_not_valid = "='!?.+-" " "                                  # Prepare the string for count 
  for i in range(len(char_not_valid)):                            # Checking if the characters not valid for the count
    text = text.replace(char_not_valid[i],"").lower()             # Firts will its erased the charactersnot valid, second convert the string in lowercase
    text ="".join([char for char in text if not char.isdigit()])  # Prepare the string erased the numbers for the count
    
  for letter in text:         # Go through each letter in the text
    if letter not in result:  # Check if the letter needs to be counted or not
      result[letter] = 1
    else:
      result[letter] +=1      # Add or increment the value in the dictionary
     
  return result

#print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
