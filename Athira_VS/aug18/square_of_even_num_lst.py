lst = [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: x*x,filter(lambda a: a % 2 == 0,lst))))