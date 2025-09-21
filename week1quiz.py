def g(y):
  b=0
  while y>=3:
    (y,b)=(y/3,b+1)
  return b
print(g(728))
def f(n):
    s = 0
    for i in range(2,n):
        if n%i == 0 and i%2 == 1:
            s = s+1
    return(s)
print(f(90)-f(89))
def h(n):
    s = True
    for i in range(1,n+1):
        if i*i == n:
            s = False
    return(s)
print(h(25))
def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
print(foo(4))