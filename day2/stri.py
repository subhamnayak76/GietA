st = " w3resource"
s = []
def fun(st):


    if len(st) >= 2:
        s = st[0:2] + st[-2:]
        print(s)
    else:
        print(-1)
