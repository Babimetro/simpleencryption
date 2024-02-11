# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:29:28 2023

@author: babak.i
"""
from cryptography.fernet import Fernet

def encrypt_fernet(key,filename):
        
    # using the generated key
    fernet = Fernet(key)
    
    # opening the original file to encrypt
    with open(filename, 'rb') as file:
    	original = file.read()
    	
    # encrypting the file
    encrypted = fernet.encrypt(original)
    
    # opening the file in write mode and
    # writing the encrypted data
    with open(filename, 'wb') as encrypted_file:
    	encrypted_file.write(encrypted)

def decrypt_fernet(key,filename):
    # using the key
    fernet = Fernet(key)
    
    # opening the encrypted file
    with open(filename, 'rb') as enc_file:
    	encrypted = enc_file.read()
    
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    
    # opening the file in write mode and
    # writing the decrypted data
    with open(filename, 'wb') as dec_file:
    	dec_file.write(decrypted)