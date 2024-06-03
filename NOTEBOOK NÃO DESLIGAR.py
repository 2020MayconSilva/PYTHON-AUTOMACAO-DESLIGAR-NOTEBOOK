#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import psutil # vou utilizar essa biblioteca para fechar o notpad 
import pyautogui # biblioteca para apertar determinado tecla
import time # biblioteca para determina o tempo de pausa 

contador = 0

# função para abri o bloco de notas
def open_notepad():
    # Simular a combinação de teclas Win + R para abrir a janela "Executar"
    pyautogui.hotkey('win', 'r')
   
    # Aguardar um pouco para garantir que a janela "Executar" esteja aberta
    time.sleep(1)
    
    # Digitar um comando na janela "Executar"  notepad e pressionar Enter
    pyautogui.typewrite("notepad", interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)
    
# Função para encontrar e fechar o Bloco de Notas
def close_notepad():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'notepad.exe':
            proc.terminate()

#função para digitar automaticamente
def digitar(): 
    pyautogui.typewrite("nao desligar o notebook", interval=0.1)
    time.sleep(3)
    
# loop enquanto contador for diferente de determinado número             
while contador != 30:
    #chamando as funções
    open_notepad()
    digitar()
    close_notepad()
    time.sleep(1800)
    # contador para sair do loop do enquanto
    contador += 1
   


