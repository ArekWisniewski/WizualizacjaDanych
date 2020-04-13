def liczby1():
    A=[1/x for x in range(10,50)]
    B=[2**x for x in range(0,50,)]
    C=[x for x in B if x%4==0]
    print(A)
    print(B)
    print(C)
