# Codificação e Decodificação de Texto em Código Morse

Este projeto implementa um sistema simples de **criptografia e descriptografia** utilizando o **Código Morse**. O usuário pode converter texto em Código Morse e vice-versa por meio de um menu interativo.

## Tecnologias Utilizadas
- **Python 3**

## Como Funciona
O programa permite que o usuário escolha entre **codificar** (converter texto em Código Morse) ou **decodificar** (converter Código Morse em texto legível). O processo segue as regras do Código Morse padrão.

## Estrutura do Código

### 1. Dicionário de Conversão
```python
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

MORSE_TO_TEXT = {v: k for k, v in MORSE_CODE.items()}
```
- **MORSE_CODE**: Dicionário que converte caracteres alfanuméricos em Código Morse.
- **MORSE_TO_TEXT**: Dicionário inverso que converte Código Morse de volta para texto.

### 2. Exibição do Menu
```python
def show_menu():
    print("\n------- [MENU] -------")
    print("[1] - Codificar")
    print("[2] - Decodificar")
    print("[3] - Sair")
    print("----------------------")
```
- Exibe as opções do programa para o usuário.

### 3. Função de Codificação
```python
def encode(text):
    return ' '.join(MORSE_CODE.get(char, '') for char in text.upper())
```
- Converte um texto em Código Morse, substituindo cada caractere por seu equivalente no dicionário **MORSE_CODE**.
- Usa **.upper()** para garantir que todas as letras sejam convertidas para maiúsculas antes da codificação.

### 4. Função de Decodificação
```python
def decode(morse):
    return ''.join(MORSE_TO_TEXT.get(code, '') for code in morse.split())
```
- Converte um Código Morse em texto normal.
- Usa **.split()** para separar os códigos Morse e buscar seus equivalentes no dicionário **MORSE_TO_TEXT**.

### 5. Loop Principal do Programa
```python
def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            text = input("Digite o texto para codificar: ")
            print("Texto codificado:", encode(text))
        elif choice == '2':
            morse = input("Digite o código Morse para decodificar: ")
            print("Texto decodificado:", decode(morse))
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
```
- Exibe o menu e solicita uma opção ao usuário.
- Se a opção for **1**, solicita um texto e exibe a versão codificada em Morse.
- Se a opção for **2**, solicita um Código Morse e exibe a versão traduzida para texto.
- Se a opção for **3**, encerra o programa.

## Como Executar o Projeto
### 1. Instale o Python 3
Se ainda não tiver o Python instalado, baixe e instale em: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Execute o Código
Salve o script como **morse.py** e execute no terminal:
```sh
python morse.py
```

### 3. Utilize as Funções do Programa
1. Escolha a opção **1** para codificar um texto para Código Morse.
2. Escolha a opção **2** para decodificar um Código Morse para texto.
3. Escolha a opção **3** para sair do programa.

---
