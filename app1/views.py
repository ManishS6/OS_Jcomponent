from django.shortcuts import render
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
# Create your views here.

def home(req):
    return render(req,'home.html',{"name":"Manish"})

def add(req):
    choice = req.POST['choice'] # value of selected radio button
    val1 = req.POST['text1']
    val2 = req.POST['text2']
    result = choice+val1+val2
    key_128 = "kuch bhi"
    iv = "InitializationVe"
    aesCipher = AESCipher(key_128)
    print(aesCipher.key)
    sentence = "manish swami"
    print(aesCipher.encrypt(sentence))
    return render(req, 'result.html' ,{'result': result})

def test(req):
    var1 = req.POST['choice'] # choice of radio button
    var2 = req.POST['text2'] # key
    tester = var1 + " " + var2
    return({'choice': tester})
