# ----------------------------------------------------------------------
# OpenNotepad-Win-R.py - Aprendizado - Robotic Process Automation (RPA)
#                        salvando conteudo via notepad
# HW: Intel
# OS: Windows 10
# Compiler: Python 3.10.4
# PKG: PyAutoGUI 3.10.4
# Criado em: 03/06/2022
# Revisao: 00
# Copyright (c) 2022 by Alan Lopes
# ----------------------------------------------------------------------

# carga das bibliotecas e pacotes
import pyautogui
import time

# iniciando notepad via windows + r
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('notepad')
pyautogui.press('tab')
pyautogui.press('tab')
BotaoOK = pyautogui.locateOnScreen('img\cmd_run\ok.png')
buttonx, buttony = pyautogui.center(BotaoOK)
pyautogui.click(buttonx, buttony)

# escrevendo no notepad
time.sleep(1)
pyautogui.write('Hello world!')
pyautogui.press('enter')
pyautogui.write('Lopes', interval=0.15)

# salvando arquivo texto
pyautogui.hotkey('ctrl', 's')
pyautogui.write('teste.txt', interval=0.10)
BotaoSalvar = pyautogui.locateOnScreen('img\cmd_run\salvar.png')
buttonx, buttony = pyautogui.center(BotaoSalvar)
pyautogui.click(buttonx, buttony)