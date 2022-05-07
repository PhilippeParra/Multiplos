"""Dado dos Numeros identificar si son multiplos
entre si"""

print("---------------------------------")
print("------------MULTIPLOS------------")
print("---------------------------------")

X = int(input("Digite el primer valor: "))
Y = int(input("digite el segundo valor: "))

if X > Y:
    Z = X % Y
else:
    Z = Y % X

if Z == 0:
    print("los numeros ", "\n" , X, "\n" , Y, "\nSon Multiplos entre si")