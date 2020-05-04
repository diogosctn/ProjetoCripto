# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:32:50 2020

@author: diogo
"""

import cryptography.fernet
import argon2
import base64
import os



def encrypt_data(data_bytes, password):
#Farei uma função q associa uma hash para a senha, e com a has encriptografamos
    password_hash = argon2.PasswordHasher().hash(password)
    password_hash = password_hash.encode()
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    encryptor = cryptography.fernet.Fernet(encoded_hash)
    return encryptor.encrypt(data_bytes)


def decrypt_data(cipher_bytes, password):    
    password_hash = argon2.PasswordHasher().hash(password)
    password_hash = password_hash.encode()
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    decryptor = cryptography.fernet.Fernet(encoded_hash)
    return decryptor.decrypt(cipher_bytes)

"""
fl = open('Arquivos/5.jpg','rb').read()

cipher = encrypt_data(fl, "SecretPasword")
decrypted = decrypt_data(cipher, "SecretPassword")

flncrpt = open('ArquivosNcrpt/5.jpg','wb').write(cipher)
fldcrpt = open('ArquivosDcrpt/5.jpg','wb').write(decrypted)
"""

#Agora farei a rotina para encriptografar todos os arquivos de uma pasta

def CriptoFile(origem, destino_cipher,destino_decrypted):
    
   
    for root, dirpath, files in os.walk(origem):
        for names in files:

            fl = open(root + "\\" + names,'rb').read()

            cipher = encrypt_data(fl, "SecretPasword")
            decrypted = decrypt_data(cipher, "SecretPassword")

            flncrpt = open(destino_cipher + "\\" + names,'wb').write(cipher)
            fldcrpt = open(destino_decrypted + "\\" + names,'wb').write(decrypted)

#CriptoFile("Teste Diretório Origem","Teste Diretório Destino","Teste Diretório Destino (1)")

CriptoFile("Arquivos","ArquivosNcrpt","ArquivosDcrpt")
