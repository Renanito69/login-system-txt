import os

# Menu principal
def menu_entrada():
    while True:
        os.system('cls')
        print("1 - Cadastro")
        print("2 - Entrar")
        print("0 - Sair")

        try:
            escolha = int(input("\nEscolha: "))

            if escolha == 1:
                cadastrar_usuario()
            elif escolha == 2:
                pass
            elif escolha == 0:
                print("Saindo")
                break

        except ValueError:
            print("\nERRO!!!")
            print("Coloque apenas numeros")
            input("precione alguma tecla para voltar para o menu")

# Responsavel por cadastrar um usuario novo
def cadastrar_usuario():
    with open("Cadastros.txt", "a") as arquivo:
        usuario_novo_usuario = str(input("Nome de Usuario: "))
        senha_novo_usuario = str(input("Nova Senha: "))
        
        if len(senha_novo_usuario) >= 4: # para verificar se a senha tem 4 ou mais caracter
            confirmacao_senha_usuario = str(input("Confirma Senha: "))
            
            if confirmacao_senha_usuario == senha_novo_usuario: # para confirmar a senha
                arquivo.write(f"{usuario_novo_usuario};{senha_novo_usuario}" + '\n')
            else:
                input("Senhas não parecidas")
        else:
            input("A senha precisa ter mais do que 4")




#Programa inicial
menu_entrada()
