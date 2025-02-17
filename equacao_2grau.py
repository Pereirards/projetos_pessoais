import math

def calcular_delta(a, b, c):
    
    delta =  math.pow(b,2) - 4 * a * c
    return delta

def valor_raizes(a, b, c):

    valor_delta = int(calcular_delta(a, b, c))
    
    if valor_delta > 0:
        x1 = (-b + math.isqrt(valor_delta))/2*a
        x2 = ((-b - math.isqrt(valor_delta))/2*a)
        print(f"As raizes da equação são os valores {x1} e {x2}")

    elif valor_delta == 0:
        x = (-b + math.isqrt(valor_delta))/2*a
        print(f'O delta é igual a zero, logo só existe a raiz {x}')

    else:
        print("O delta é negativo, logo não existe raiz no campo dos reais")

try:
    valor_a = float(input("Digite o valor do coeficiente a = "))
    valor_b = float(input("Digite o valor do coeficiente b = "))
    valor_c = float(input("Digite o valor do coeficiente c = "))

    valor_raizes(valor_a, valor_b, valor_c)

except ValueError:
    print("Por favor, digite apenas números")
