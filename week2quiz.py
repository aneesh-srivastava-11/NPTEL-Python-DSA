x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1
y = x[0:50]                          # Statement 2
z = y                                # Statement 3
w = x                                # Statement 4
x[0] = x[0][:5] + 'ery'              # Statement 5
y[2] = 4                             # Statement 6
z[4] = 42                            # Statement 7
#w[0][:3] = 'fea'                     # Statement 8
x[1][0] = 5555                       # Statement 9
#a = (x[4][1] == 1)                   # Statement 10

b = [23,44,87,100]
a = b[1:]
d = b[2:]
c = b
d[0] = 97
c[2] = 77
print(a[1],b[2],c[2],d[0])
startmsg = "python"
endmsg = ""
for i in range(1,1+len(startmsg)):
  endmsg = startmsg[-i] + endmsg
print(endmsg)
def mystery(l):
  l = l[1:]
  return()

mylist = [7,11,13]
mystery(mylist)
print(mylist)