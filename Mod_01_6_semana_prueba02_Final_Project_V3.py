def calculate_frequencies(file_contents):

  # Here is a list of punctuations and uninteresting words you can use to process your text
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
  # LEARNER CODE START HERE 

  # start variables
  text = file_contents  
  result = []
  dicc_count = {}
  
  # Prepare the string for count 
  for i in range(len(punctuations)):                            # Checking if the characters not valid for the count
    text = text.replace(punctuations[i],"").lower()             # Firts will its erased the charactersnot valid, second convert the string in lowercase
    words= text.split(" ")                                      # Prepare the string erased the numbers for the count
   
  
  for word in words:
    if word.isalpha():
      result.append(word)
  print(result)  

  for word_1 in uninteresting_words:
    for word_2 in result:
      if word_1 == word_2: 
        print(word_1)
        print(word_2) 
        result.remove(word_1)
        print(result)
        
  #print(words)
      
  for word in result:         # Go through each letter in the text
    if word not in dicc_count: 
                 # Check if the letter needs to be counted or not
      dicc_count[word] = 1
      #print(dicc_conteo)
     
    else:
      dicc_count[word] += 1     # Add or increment the value in the dictionary


  return dicc_count
   
print(calculate_frequencies("Prueba to all to home all because all no This all glossary does not aim at completeness, and it is not primarily a glossary of rare or 'hard' words. A good working knowledge of Middle "))
