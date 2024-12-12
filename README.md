# Hangman (Jogo da Forca)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen) ![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-yellow)

Este projeto é parte do curso [**100 Days of Code: The Complete Python Pro Bootcamp**](https://www.udemy.com/course/100-days-of-code/), ministrado por Angela Yu. Ele corresponde ao desafio do **Dia 7** e tem como objetivo criar um jogo da forca (“Hangman”) utilizando Python. Este é um projeto iniciante, projetado para ser executado no terminal.

## Descrição do Projeto

O jogo da forca é um jogo clássico onde o jogador deve adivinhar uma palavra secreta, letra por letra. Para este projeto:

- Uma palavra é escolhida aleatoriamente de uma lista pré-definida.
- O jogador tem 6 vidas, perdendo uma a cada tentativa incorreta.
- O progresso é exibido no terminal, incluindo as letras adivinhadas corretamente e o estágio atual do boneco da forca.
- O jogo termina quando o jogador adivinha toda a palavra ou perde todas as vidas.

## Funcionalidades

- Exibição do logo do jogo e dos estágios gráficos da forca.
- Verificação de letras já tentadas.
- Informações de feedback sobre palpites corretos e incorretos.
- Mensagens claras de vitória ou derrota.

## Como Jogar

1. Clone ou baixe este repositório.
2. Certifique-se de ter o Python instalado (versão 3.9 ou superior).
3. Execute o código no terminal com:
   ```bash
   python hangman.py
   ```
4. Siga as instruções exibidas no terminal para adivinhar a palavra.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Módulo Random**: Utilizado para selecionar palavras aleatoriamente.

## Estrutura do Código

- **`hangman_art.py`**: Contém os recursos visuais, como o logo, estágios da forca e mensagens de vitória/derrota.
- **`hangman_words.py`**: Contém a lista de palavras usadas no jogo.
- **`hangman.py`**: Contém a lógica principal do jogo.

## Preview

Aqui está um exemplo da interface no terminal durante o jogo:

```
Adivinhe uma letra: a
_ a _ _ _

Adivinhe uma letra: e

Você adivinhou e, isso não está na palavra. Você perdeu uma vida.

    +---+
    |   |
    O   |
   /|\  |
         |
   =========

_ a _ _ _
```
