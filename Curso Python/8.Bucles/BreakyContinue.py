# Break sirbe para cortar el ciclo.
# Continue corta una parte del ciclo y continua.  

for i in range(1, 11):
    print(i)
    if i == 5:
        break

# Va a contar hasta 5 y ahi corta el conteo. 


for i in range(1, 11):
    print(i)
    if i == 5:
        continue
    print(i)
