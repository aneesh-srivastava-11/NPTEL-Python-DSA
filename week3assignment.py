#q1
def expanding(l):
    if len(l) <= 2:
        return(True)
    diff = abs(l[1]-l[0])
    return(diff < abs(l[2]-l[1]) and expanding(l[1:]))

def expanding_iterative(l):
    if len(l) <= 2:
        return(True)
    olddiff = abs(l[1]-l[0])
    for i in range(2,len(l)):
        newdiff = abs(l[i]-l[i-1])
        if newdiff <= olddiff:
            return(False)
        olddiff = newdiff
    return(True)
def even(n):
    return(n%2 == 0)
def sumsquare(l):
    oddsum = 0
    evensum = 0
    for n in l:
        if even(n):
            evensum += n*n
        else:
            oddsum += n*n
    return([oddsum,evensum])
#q3
def transpose(l):
  outl = []
  for row in l[:1]:
    for i in range(len(row)):
      outl.append([])
  for row in l:   
    for i in range(len(row)):
      outl[i].append(row[i])
  return(outl)