def f(N):
    current = 0
    
    while current <= N:
        reset = yield current
        if reset is not None:
            if reset % 2 == 0:
                current = reset - 2
            #elif reset == 0:
            #    current = -2
                
            else:
                current = reset - 1
        current += 2
        
g = f(71)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for e in g:
    print(e)