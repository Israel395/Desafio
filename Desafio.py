from decimal import Decimal
import decimal
extrato = ""
saque = 0
saldo = 2000
contadorSaque = 0
while True:
    try:
        comando = int(input("Escolha uma operação: \n[1]-Depositar \n[2]-Sacar \n[3]-Extrato \n[4]-Sair"))

        try:
            if(comando == 1):
                deposito = Decimal(input("Informe o valor do deposito: "))

                if(deposito < 0):
                    print("Erro valor invalido!")

                else:
                    saldo += deposito
                    print(f"Deposito realizado com sucesso! \nSaldo R$ {saldo:.2f}")

            elif(comando == 2):
                if(contadorSaque >= 3):
                    print("Você excedeu a quantidade de saques diaria")

                else:
                    saque = Decimal(input("Informe a quantia que deseja realizar o saque:"))

                    if(saque > 500):
                        print("Voce não pode sacar um valor maior que R$ 500.00")

                    elif(saque > saldo):
                        print("Você não possui saldo o suficiente")

                    elif(saque < 0):
                        print("Erro! Valor invalido!")

                    else:
                        saldo -= saque
                        extrato += f"Saque de R$ {saque:.2f}\n"
                        print(f"saque realizado com sucesso \nSaldo de R$ {saldo:.2f}")
                        contadorSaque += 1

            elif(comando == 3):
                if(extrato == ""):
                    extrato += f"Não foram realizadas movimentações \nSaldo:  R$ {saldo:.2f}"
                    print(extrato)

                else:
                    extrato += f"Saldo:  R$ {saldo:.2f}"
                    print("\n================ EXTRATO ================")
                    print(extrato)
                    print("===========================================\n")

            elif(comando == 4):
                break

            else:
                print("Operaçãp invalida!")

        except decimal.InvalidOperation:
            print("Erro! Insira um valor valido!")

    except ValueError:
        print("Erro! Insira um valor valido!")