import itertools
from array import array
import paramiko


def generate_combinations_helper(characters, max_length):
    if max_length == 0:
        yield ''
    else:
        for char in characters:
            for combo in generate_combinations_helper(characters, max_length - 1):
                yield char + combo


def generate_combinations(characters, min_length, max_length):
    for length in range(min_length, max_length + 1):
        yield from generate_combinations_helper(characters, length)


def ssh_login(hostname, port, username, password):
    """
    Verifica se é possível realizar o login SSH
    :param hostname: host a ser verificado
    :param port: porta a ser verificada
    :param username: usuário a ser verificado
    :param password: senha a ser verificada
    :return: True se o login for bem-sucedido, False caso contrário
    """
    # Cria uma instância do cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Realiza a conexão SSH
        client.connect(hostname, port, username, password)
        client.close()
        return True
    except paramiko.AuthenticationException:
        return False
