fnotes = int(input())
fonotes = int(input())
cost = int(input())
if(fnotes * 5 + fonotes * 1 < cost):
    print(-1)
else:
    n_five = int(cost / 5)
    print(n_five)
    n_one = cost % 5
    print(n_one)

