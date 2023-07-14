from functions import generate_combinations


chars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*_+=-?.,"


def generate(characters: str = chars, min_length: int = 4, max_length: int = 8):
    with open('../wordlists/combinations.txt', 'w') as file:
        for x in generate_combinations(characters, min_length, max_length):
            file.write(f'{x}\n')
