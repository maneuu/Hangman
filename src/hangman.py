import random
import hangman_art
import hangman_words


# Escolhe uma palavra aleatória da lista
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Variáveis de controle do jogo
end_of_game = False
lives = 6

# Limpa o console e exibe o logo do jogo
hangman_art.clear()
print(hangman_art.logo)

# Testando o código
# print(f'Pssst, a solução é {chosen_word}.')

# Cria os espaços em branco para as letras
display = []
for _ in range(word_length):
    display += "_"

guesses = []

# Loop principal do jogo
while not end_of_game:
    # Solicita ao usuário para adivinhar uma letra
    guess = input("Adivinhe uma letra: ").lower()
    hangman_art.clear()

    # Verifica se a letra já foi adivinhada
    if guess not in guesses:
        
        # Verifica a letra e coloca na posição correta
        for position in range(word_length):
            letter = chosen_word[position]
            
            if letter == guess:
                display[position] = letter

        # Verifica se o palpite está errado
        if guess not in chosen_word:
            print(f"\nVocê adivinhou {guess}, isso não está na palavra. Você perdeu uma vida")
            lives -= 1
            
            # Verifica se as vidas acabaram
            if lives == 0:
                end_of_game = True
                hangman_art.clear()

                print(hangman_art.you_lose)
                break
    else:
        print(f"Você já adivinhou a letra {guess}")
    
    # Exibe as letras acertadas até o momento
    print(f"{' '.join(display)}")
    
    # Adiciona o palpite à lista de tentativas
    guesses.append(guess)

    # Verifica se o jogador acertou todas as letras
    if "_" not in display:
        end_of_game = True
        hangman_art.clear()
        print(hangman_art.you_win)
        break

    # Exibe o estágio atual baseado no número de vidas restantes
    print(hangman_art.stages[lives])