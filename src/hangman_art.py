stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
you_win = '''
                                         
__   _____  _   _  __        _____ _   _ 
\ \ / / _ \| | | | \ \      / |_ _| \ | |
 \ V | | | | | | |  \ \ /\ / / | ||  \| |
  | || |_| | |_| |   \ V  V /  | || |\  |
  |_| \___/ \___/     \_/\_/  |___|_| \_|
                                         
'''
you_lose = '''
                                             
__   _____  _   _     _     ___  ____  _____ 
\ \ / / _ \| | | |   | |   / _ \/ ___|| ____|
 \ V | | | | | | |   | |  | | | \___ \|  _|  
  | || |_| | |_| |   | |__| |_| |___) | |___ 
  |_| \___/ \___/    |_____\___/|____/|_____|
                                                                                      
'''                                                          
                                                                    
# Importa o módulo 'os', que permite interagir com o sistema operacional.
import os

# Define a função 'clear', que limpa o console/terminal onde o script está sendo executado.
def clear():
    # Verifica qual sistema operacional está em uso:
    # - 'os.name' retorna 'nt' se for Windows.
    # - Para outros sistemas, como Linux ou macOS, retorna 'posix'.
    # Dependendo do sistema, o comando correto para limpar o console é usado:
    # - 'cls' para Windows
    # - 'clear' para Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')