try:
    t = int(input())
    for i in range(t):
        r, c = [int(x) for x in input().split()]
        if (r != 1) and (c != 1):
            if r == c:
                print(17)
                print("1 1")
                #print(f"{r} {c}")
            else:
                print(18)
                #print(f"{r} {c}")
                e = int((r + c)/2)
                print(f"{e} {e}")
                print("1 1")
        else:
            print(16)
        print("8 8")
        print("7 7")
        print("8 6")
        print("3 1")
        print("1 3")
        print("6 8")
        print("5 7")
        print("8 4")
        print("5 1")
        print("1 5")
        print("4 8")
        print("3 7")
        print("8 2")
        print("7 1")
        print("1 7")
        print("2 8")
except:
    pass