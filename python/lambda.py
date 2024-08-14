#sort

data = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
sorted_data = sorted(data, key=lambda x: x[1])  # Sort by the second element (fruit name)

#filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

#map
numbers = [1, 2, 3]
squared_numbers = list(map(lambda x: x**2, numbers)) 
