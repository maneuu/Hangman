import random
import hangman_art
import hangman_words
import os

# Função para limpar a tela, compatível com diferentes sistemas operacionais
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Limpa o console e exibe o logo do jogo
clear()
print(hangman_art.logo)

# Mensagem de boas-vindas e explicação do jogo
print("\U0001F3AE Bem-vindo ao Jogo da Forca! \U0001F3AE")
print("""
Você deve adivinhar a palavra secreta letra por letra. A cada erro, você perde uma vida, e o boneco da forca ficará mais próximo do fim! 
Você tem 6 vidas ao todo. Use apenas letras, e uma letra por vez. Boa sorte!
""")

# Escolhe uma palavra aleatória da lista de palavras disponíveis
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Variáveis de controle do jogo
end_of_game = False  # Indica se o jogo terminou
lives = 6  # Quantidade inicial de vidas

guesses = []  # Lista para armazenar os palpites já feitos

# Cria uma lista com underscores para representar as letras não adivinhadas da palavra
# Exemplo: para a palavra "python", será ["_", "_", "_", "_", "_", "_"]
display = ["_"] * word_length

# Função para validar o palpite do jogador, permitindo apenas uma letra e sem símbolos ou números
def is_valid_guess(guess):
    return guess.isalpha() and len(guess) == 1

# Loop principal do jogo
while not end_of_game:
    # Solicita ao jogador uma letra e converte para minúscula
    guess = input("\U0001F4AD Adivinhe uma letra: ").lower()
    clear()

    # Verifica se o palpite é válido
    if not is_valid_guess(guess):
        print("\U0001F6AB Apenas letras são permitidas e apenas uma letra por vez! Tente novamente.")
        continue

    # Verifica se a letra já foi adivinhada anteriormente
    if guess in guesses:
        print(f"\U0001F914 Você já adivinhou a letra '{guess}'. Tente outra!")
    else:
        # Adiciona o palpite à lista de letras já tentadas
        guesses.append(guess)

        # Verifica se a letra está na palavra escolhida
        if guess in chosen_word:
            # Substitui os underscores pelas letras corretas nas posições correspondentes
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
            print(f"\U0001F60E Ótimo! A letra '{guess}' está na palavra.")
        else:
            # Reduz uma vida caso o palpite esteja errado
            lives -= 1
            print(f"\U0001F62D A letra '{guess}' não está na palavra. Você perdeu uma vida. {lives} vidas restantes.")

    # Exibe o estado atual da palavra, com as letras acertadas e underscores para as não descobertas
    print(f"\U0001F4D6 Palavra: {' '.join(display)}")

    # Verifica se o jogador acertou toda a palavra
    if "_" not in display:
        end_of_game = True
        print("\U0001F389 Parabéns! Você ganhou! \U0001F389")
    # Verifica se o jogador perdeu todas as vidas
    elif lives == 0:
        end_of_game = True
        print(f"\U0001F480 Você perdeu! A palavra era '{chosen_word}'. \U0001F480")

    # Exibe o estado atual do boneco na forca, baseado nas vidas restantes
    print(hangman_art.stages[lives])
