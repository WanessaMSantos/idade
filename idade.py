print("Digite seu nome: ")
nome = input()

executar = True

While(executar == True):
    print("Digite o seu ano de nascimento: ")
    try = int(input())
        if (ano < 1922) or (ano > 2024):
            print("Ano inválido, tente novamente!")

        else:
            idade= 2024 - ano
            print("O usuário " , nome , "completou ou completará", idade , "anos em 2024")
            executar = False
    except:
        print("A idade precisa ser digitada em números!")
        