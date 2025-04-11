import pyautogui as pyauto
import pandas as pd
import time

URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
FILE = "produtos.csv"
BROWSER = "brave"
ENTER = "enter"

LOGIN = "aoba123@gmail.com"
SENHA = "testeteste"


data = pd.read_csv(FILE)
pyauto.PAUSE = 0.5

# Open Browser

pyauto.press("win")
pyauto.write(BROWSER)
pyauto.press(ENTER)

# Wait Browser Open

time.sleep(2)

# Go to Website

pyauto.write(URL)
pyauto.press(ENTER)

# Wait website load

time.sleep(2)

# Click on the Login Input

pyauto.mouseDown((937,366))
pyauto.click()

# Insert Info on Inputs and Login

pyauto.write(LOGIN)
pyauto.press('tab')
pyauto.write(SENHA)
pyauto.press(ENTER)

for row in data.index:
    # Go to first input field
    pyauto.mouseDown((879,246))

    # Start register
    pyauto.write(data.loc[row, 'codigo'])
    pyauto.press('tab')

    pyauto.write(data.loc[row, 'marca'])
    pyauto.press('tab')

    pyauto.write(data.loc[row, 'tipo'])
    pyauto.press('tab')

    pyauto.write(str(data.loc[row, 'categoria']))
    pyauto.press('tab')

    pyauto.write(str(data.loc[row, 'preco_unitario']))
    pyauto.press('tab')

    pyauto.write(str(data.loc[row, 'custo']))
    pyauto.press('tab')

    if not pd.isna(data.loc[row, 'obs']):
        pyauto.write(data.loc[row, 'obs'])
    pyauto.press('tab')
    
    pyauto.press(ENTER)
    pyauto.scroll(1000)
