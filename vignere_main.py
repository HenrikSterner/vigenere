import streamlit as st

st.title("Vigenere Kryptering")

st.write("Dette er en simpel Vigenere krypteringsapp.")

def vigenere_encrypt(plaintext, key):
    encrypted = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    for i in range(len(plaintext_int)):
        if plaintext[i].isalpha():
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            encrypted.append(chr(value + 65))
        else:
            encrypted.append(plaintext[i])
    return ''.join(encrypted)

def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            decrypted.append(chr(value + 65))
        else:
            decrypted.append(ciphertext[i])
    return ''.join(decrypted)

st.subheader("Krypter Tekst")
plaintext = st.text_area("Indtast tekst til kryptering:")
key = st.text_area("Indtast nøgle:",key="key_input")
if st.button("Krypter"):
    if plaintext and key:
        ciphertext = vigenere_encrypt(plaintext.upper(), key.upper())
        st.write("Krypteret tekst:", ciphertext)
    else:
        st.write("Indtast både tekst og nøgle.")

st.subheader("Dekrypter Tekst")
ciphertext = st.text_area("Indtast tekst til dekryptering:")
key = st.text_area("Indtast nøgle:", key="key_input_decrypt")
if st.button("Dekrypter"):
    if ciphertext and key:
        decrypted_text = vigenere_decrypt(ciphertext.upper(), key.upper())
        st.write("Dekrypteret tekst:", decrypted_text)
    else:
        st.write("Indtast både tekst og nøgle.")
