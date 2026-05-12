import pyautogui
import time
import keyboard
import os

# ========= FUNÇÕES ========= #
num = "15"
pasta = r"C:\Users\cleid\Desktop\beterraba\tiktik\reformans\pVd0." + num
num_imgs = 9
num_videos = num_imgs - 1


def esperar_imagem(imagem, timeout=30, confidence=0.8, region=()):
    inicio = time.time()

    while True:
        try:
            if keyboard.is_pressed("esc"):
                print("Programa interrompido pelo usuário")
                exit()
            pos = pyautogui.locateCenterOnScreen(
                imagem, confidence=confidence, region=region)

            if pos is not None:
                print(f"{imagem} encontrada")
                return pos

            if int(time.time() - inicio) > timeout:
                print(f"Imagem {imagem} não encontrada")
                exit()

            time.sleep(0.5)
        except:

            print(
                f"procurando por {imagem} , inc: {int(time.time() - inicio)}")


def esperar_e_clicar(imagem, timeout=30, confidence=0.8, region=()):
    pos = esperar_imagem(imagem, timeout, confidence, region)
    time.sleep(1)
    pyautogui.click(pos)


time.sleep(4)
while True:
    print("Procurando imagem 1...")
    pos = esperar_imagem("gemini3.png")

    if pos is not None:
        print("Imagem 1 encontrada!")

        time.sleep(1)  # pequena espera para a tela estabilizar

        pos2 = esperar_imagem("gemini4.png", timeout=5)

        if pos2 is not None:
            print("Imagem 2 encontrada. Voltando ao início...")
            continue  # volta pro começo do while e procura a imagem 1 de novo

        print("Imagem 2 não encontrada. Continuando o processo...")

        # aqui você coloca a ação desejada
        pyautogui.moveTo(pos)
        pyautogui.moveRel(400, 140)
        pyautogui.rightClick()

        break


pos = esperar_imagem("gemini3.png")

# baixar imagens
time.sleep(2)
