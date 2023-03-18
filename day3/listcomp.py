# list compheresion
#for loop
result = []
for i in range(11):
    result.append(i)
print(result)

#list compheresion
# print(i for i in range(11))
com =[]
com =[i for i in range(11)]
#print(com)

#odd element is list comphrension
odd =[]
odd = [i for i in range(11) if i % 2 != 0]
print(odd)

#list compherension using if else
oddsquare = []
oddsquare = [i if i % 2 != 0 else i**2 for i in range(11)]
print(oddsquare)