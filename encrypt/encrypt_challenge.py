#!/usr/bin/env python3
import random
import base64
import codecs

def gen_question():
    questions = [
        ("base64", lambda x: base64.b64encode(x.encode()).decode(), lambda s: base64.b64decode(s.encode()).decode()),
        ("rot13", lambda x: codecs.encode(x, 'rot_13'), lambda s: codecs.decode(s, 'rot_13')),
        ("hex", lambda x: x.encode().hex(), lambda s: bytes.fromhex(s).decode()),
        ("reverse", lambda x: x[::-1], lambda s: s[::-1]),
        ("caesar +3", lambda x: caesar(x, 3), lambda s: caesar(s, -3))
    ]
    label, enc_func, dec_func = random.choice(questions)
    plaintext = random_string()
    challenge = enc_func(plaintext)
    return label, challenge, dec_func, plaintext

def random_string(length=6):
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))

def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def main():
    correct = 0
    flag = "alx{flag}"

    print("Selamat datang di tantangan encoding!\nJawab 5 soal berturut-turut dengan benar untuk mendapatkan flag!\n")

    while correct < 5:
        label, encoded, decoder, plain = gen_question()
        print(f"Decode ({label}): {encoded}")
        try:
            ans = input("Jawabanmu: ").strip()
            if ans == plain:
                print("✅ Benar!\n")
                correct += 1
            else:
                print("❌ Salah, diulang dari awal!\n")
                correct = 0
        except:
            print("❌ Error decode, diulang dari awal!\n")
            correct = 0

    print(f"\n🎉 Selamat! Ini flag kamu: {flag}")
    
if __name__ == "__main__":
    main()

