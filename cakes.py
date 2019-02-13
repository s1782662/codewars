recipes,available = {'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}


print(min([available.get(k,0) // recipes[k]  for k in recipes]))
