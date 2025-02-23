# Dicionário do Código Morse
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

# Inverte o dicionário para decodificação
MORSE_TO_TEXT = {v: k for k, v in MORSE_CODE.items()}

def show_menu():
    print("\n------- [MENU] -------")
    print("[1] - Codificar")
    print("[2] - Decodificar")
    print("[3] - Sair")
    print("----------------------")

def encode(text):
    return ' '.join(MORSE_CODE.get(char, '') for char in text.upper())

def decode(morse):
    return ''.join(MORSE_TO_TEXT.get(code, '') for code in morse.split())

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

if __name__ == "__main__":
    main()
