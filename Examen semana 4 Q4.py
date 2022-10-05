# Use a list comprehension. The function receives the variables start and end, and returns a list of squares 
# of consecutive numbers between start and end inclusively.For example, squares(2, 3) should return [4, 9].

def squares(start, end):

	squares = [i * i for i in range (start, end+1)] # 1º--> variable cuadrados = 2º--> recorremos i en range->star a stop +1 para que stop
	
	return squares

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]