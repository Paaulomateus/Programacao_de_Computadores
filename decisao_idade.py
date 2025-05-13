acompanhado = input("Estar acompanhado? [S]/[N]: ")

if acompanhado.upper() == "S":
    idade = int(input("Digite sua idade: "))  
    if idade >= 18:
        print("Você é maior de idade e está acompanhado. Pode entrar!")
    else:
        print("Você é menor de idade, mas está acompanhado. Pode entrar com restrições.")
elif acompanhado.upper() == "N":
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade e não está acompanhado. Pode entrar!")
    else:
        print("Você é menor de idade e não está acompanhado. Não pode entrar!")
else:
    print("Opção inválida. Saiu do sistema.")