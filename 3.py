def extractfield(file,n):
    infile = open(file, 'r')
    return [line.rstrip().split(',')[n-1] for line in infile]
infile='infile.csv'
outfile=open('outfile.csv','w')
user=input('enter your name: ')
q=extractfield(infile,1)
a=extractfield(infile,2)
count=0
for i in range(len(a)):
    print(q[i])
    s=input()
    if s == a[i]:
        count+=1
l=[user+",",str(count)]
print(l)
outfile.writelines(l)
outfile.close()
