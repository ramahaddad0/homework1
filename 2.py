def binary(d):
    binary = []
    while d>0:
        binary.append(d%2)
        d//=2
    binary.reverse()
    return binary
n=int(input('enter a number '))
res=binary(n)
for i in res:
    print(i,end='')

