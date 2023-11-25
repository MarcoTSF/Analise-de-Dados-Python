import re  # Módulo para expressões regulares

def validar_senha(senha):
    if len(senha) < 8:
        return False

    if not any(char.isupper() for char in senha):
        return False

    if not any(char.isdigit() for char in senha):
        return False

    if not re.search("[!@#$&*]", senha):
        return False

    return True

senha_usuario = input("Crie uma senha: ")

if validar_senha(senha_usuario):
    print("Senha válida. Parabéns!")
else:
    print("A senha não atende aos critérios especificados. Por favor, tente novamente.")