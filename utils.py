from os import system, name
from keyboard import read_key
from time import sleep

def clear():
    system("cls" if name == "nt" else "clear")

def wait_keypress():
    sleep(1)
    print("\nPara continuar, carregue numa tecla...")
    read_key()