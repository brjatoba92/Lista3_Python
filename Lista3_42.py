n25 = []
n50 = []
n75 = []
n100 = []
numero = True
while numero > 0:
    numero = float(input("Digite um número: "))
    if numero > 0 and numero <= 25:
        n25.append(numero)
    elif numero > 25 and numero <= 50:
        n50.append(numero)
    elif numero > 50 and numero <= 75:
        n75.append(numero)
    elif numero > 75 and numero <= 100:
        n100.append(numero)
    
    x = str(input('Digite e para encerrar ou c para continuar: '))# implementar uma opção para continuar ou encerrar 
    if x == "e":
        break
    elif x == "c":
        continue


print("\n[0, 25]: ", len(n25))
print("[26, 50]: ", len(n50))
print("[51, 75]: ", len(n75))
print("[76, 100]: ", len(n100))
