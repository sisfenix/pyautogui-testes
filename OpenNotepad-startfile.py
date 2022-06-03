# --------------------------------------------------------------------------
# OpenNotepad-startfile.py - Aprendizado - Robotic Process Automation (RPA)
#                               salvando conteudo via notepad
# HW: Intel
# OS: Windows 10
# Compiler: Python 3.10.4
# PKG: PyAutoGUI 3.10.4
# Criado em: 03/06/2022
# Revisao: 00
# Copyright (c) 2022 by Alan Lopes
# --------------------------------------------------------------------------

# carga das bibliotecas e pacotes
import pyautogui
import os
import time

# iniciando notepad via windows + r
os.startfile("Notepad.exe")
time.sleep(1)
pyautogui.write('Hello world!')

# salvando arquivo texto
pyautogui.hotkey('ctrl', 's')
pyautogui.write('teste.txt', interval=0.05)
pyautogui.hotkey('alt', 'l')