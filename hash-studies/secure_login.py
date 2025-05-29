import hashlib

def gerar_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def menu():
    print("\nBem vindo ao meu estudo de hashes ╰(*°▽°*)╯")
    print("1. Gerar hash de um texto")
    print("2. Comparar dois textos")
    print("3. Sair(mas volta depois hein! 😊)")

    return input("Escolha uma opção: ")


while True:
    opcao = menu()

    if opcao == "1":
        texto = input("Digite um texto para gerar o hash: ")
        hash_gerado = gerar_sha256(texto)
        print(f"🔐 Hash SHA256:\n{hash_gerado}")

    elif opcao == "2":
        t1 = input("Digite o primeiro texto: ")
        t2 = input("Digite o segundo texto: ")
        h1 = gerar_sha256(t1)
        h2 = gerar_sha256(t2)
        if h1 == h2:
            print("✅ Os textos geram o MESMO hash!")
        else:
            print("❌ Hashs diferentes! Os textos não são iguais.")

    elif opcao == "3":
        print("Obrigado por testar, até mais! 😎")
        break

    else:
        print("Opção inválida, tenta de novo 😉")
