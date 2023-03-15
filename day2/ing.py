st = input()
if len(st)<3:
    print(st)
else:
    if st[-3:]!="ing":
        st = st + "ing"
    else:
        st = st + "ly"
    print(st)             
