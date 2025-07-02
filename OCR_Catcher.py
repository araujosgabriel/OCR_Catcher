import cv2
import numpy as np
import pyautogui
import pytesseract
import time
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

TEXTO_ALVO = input("Insira o texto desejado: ")

try:
    while True:
        print(f"Monitorando a tela inteira em busca do texto '{TEXTO_ALVO}'... Pressione Ctrl+C para parar.")
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        dados = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

        encontrado = False
        for i, texto in enumerate(dados['text']):
            if TEXTO_ALVO.lower() in texto.lower():
                x = dados['left'][i]
                y = dados['top'][i]
                w = dados['width'][i]
                h = dados['height'][i]

                centro_x = x + w // 2
                centro_y = y + h // 2

                print(f"✅ Texto '{TEXTO_ALVO}' encontrado em ({centro_x}, {centro_y}), clicando...")
                pyautogui.click(centro_x, centro_y)
                encontrado = True
                break

        if not encontrado:
            print("Texto ainda não encontrado...")

        time.sleep(1)
        os.system("cls")

except KeyboardInterrupt:
    print("Encerrado pelo usuário.")
