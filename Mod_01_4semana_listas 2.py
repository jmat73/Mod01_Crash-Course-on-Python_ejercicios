def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in elements [0:]:
		# Does this element belong in the resulting list?
		if new_list.index(i)==i:
			# Add this element to the resulting list
			new_list.append(i)
		# Increment i
		i+=""

		return new_list

	return []

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
