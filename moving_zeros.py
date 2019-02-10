numbers = ["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]
l = []
count = 0
for i in numbers:
    if type(i) == bool or  i != 0:
        l.append(i)
    else:
        count += 1

l.extend([0]*count)
print(l)




# Improved version

result = [i for i in numbers if isinstance(i,bool) or i! = 0]
print(result + [0]*(len(numbers) - len(result)))
