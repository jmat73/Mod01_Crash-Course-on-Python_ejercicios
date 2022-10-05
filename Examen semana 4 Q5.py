# Complete el código para iterar a través de las claves y valores del diccionario car_prices, imprimiendo información sobre cada uno.
def car_listing(car_prices):
	result = ""
	for car, price in car_prices.items():
		if car not in result: 
			result += "{} costs {} dollars".format(car , price) + "\n"
	return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))