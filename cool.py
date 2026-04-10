import tkinter as tk
from tkinter import scrolledtext

morse_dict = {
    "A": ".-..-",
    "B": "..--.",
    "C": "-..--.",
    "D": "...-..",
    "E": "-.-.-",
    "F": ".--..-",
    "G": "-....-",
    "H": ".-.-..",
    "I": "..-..-",
    "J": "--...",
    "K": "-.-.-.",
    "L": "..---.",
    "M": "...---",
    "N": ".-....",
    "O": ".---..",
    "P": "-.-...",
    "Q": "..-.-.",
    "R": "---..-",
    "S": "-.--..",
    "T": ".-.-.-",
    "U": "-..-..",
    "V": "--..-.",
    "W": "-..-..-",
    "X": ".-.-..-",
    "Y": "--.-..",
    "Z": "-...-.",

    "0": "-..-.-",
    "1": ".-.--",
    "2": "--..--",
    "3": "..-.--",
    "4": ".---.-",
    "5": "-.-..-",
    "6": "...--.",
    "7": "-...--",
    "8": ".-...-",
    "9": "--.-.-"
}

# Reverse dictionary
reverse_morse = {v: k for k, v in morse_dict.items()}

# ================================
# FUNCTIONS
# ================================

def decode_text():
    message = input_box.get("1.0", tk.END).strip()
    words = message.split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_word = ""

        for letter in letters:
            decoded_word += reverse_morse.get(letter, "?")

        decoded_words.append(decoded_word)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, " ".join(decoded_words))


def encode_text():
    text = input_box.get("1.0", tk.END).strip().upper()
    words = text.split()
    encoded_words = []

    for word in words:
        encoded_letters = []

        for char in word:
            if char in morse_dict:
                encoded_letters.append(morse_dict[char])
            else:
                encoded_letters.append("?")

        encoded_words.append(" ".join(encoded_letters))

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, " / ".join(encoded_words))


def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# ================================
# GUI SETUP
# ================================

root = tk.Tk()
root.title("Custom Morse Decoder")
root.geometry("600x400")

# Input label
tk.Label(root, text="Input:", font=("Arial", 12)).pack()

# Input box
input_box = scrolledtext.ScrolledText(root, height=5)
input_box.pack(fill="both", padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Decode → English", command=decode_text).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Encode → Morse", command=encode_text).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear", command=clear_text).grid(row=0, column=2, padx=5)

# Output label
tk.Label(root, text="Output:", font=("Arial", 12)).pack()

# Output box
output_box = scrolledtext.ScrolledText(root, height=5)
output_box.pack(fill="both", padx=10, pady=5)

# Run app
root.mainloop()
