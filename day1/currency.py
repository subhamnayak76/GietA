a = int(input())
type  = input()
if type == "euro":
    print(a*0.01417)
elif type == "pound":
    print(a*0.0100)
elif type == "b.dollar":
    print(a*0.02140)
elif type == "c.dollar":
    print(a*0.2027)
else:
    print(-1)
