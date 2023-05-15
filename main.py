from io import StringIO
grau = input("Digite o grau da equação: ")
grau = float(grau)

if grau < 1 or grau > 2:
    print("Grau inválido")
else:
    if grau == 1:
        print("A equação é do primeiro grau")
        a1 = int(input("Digite um valor para a: "))
        if a1 == 0:
            print("Valor de a inválido")
        else: 
            b1 = int(input("Digite uma valor para b: "))
            resultado1 = (-b1/a1)
            print(f'x = {resultado1:.2f}')
    if grau == 2:
        print("A equação é do segundo grau")
        a2 = int(input("Digite um valor para a: "))
        if a2 == 0:
            print("Valor de a inválido")
        else:
            b2 = int(input("Digite um valor para b:" ))
            c2 = int(input("Digite um valor para c: "))
            determinante = float(b2**2 - 4*a2*c2)
            raiz_det = (determinante**(1/2))
            raiz1 = ((-b2 + raiz_det)/2*a2)
            raiz2 = ((-b2 - raiz_det)/2*a2)
        
            if determinante < 0:
                print("A equação não possui raízes reais")
            else:
                if determinante == 0:
                    print("A equação possui uma raiz real")
                    print(f'x = {raiz2:.2f}')
                    
                elif determinante > 0:
                    print("A equação possui duas raízes reais")
                    print (f'{raiz2:.2f},{raiz1:.2f}')
                      
