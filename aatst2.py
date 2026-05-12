import pyautogui
import time
import keyboard
import os
import sys

# ========= FUNÇÕES ========= #
num = "16"
pasta = r"C:\Users\cleid\Desktop\beterraba\tiktik\reformans\pVd0." + num
num_imgs = 9
num_videos = num_imgs - 1


if (not os.path.exists(pasta)):
    os.mkdir(pasta)


def esperar_imagem(imagem, timeout=30, confidence=0.8, region=None, r=False):
    inicio = time.time()

    while True:
        if keyboard.is_pressed("esc"):
            print("Programa interrompido pelo usuário")
            sys.exit()

        try:
            pos = pyautogui.locateCenterOnScreen(
                imagem,
                confidence=confidence,
                region=region
            )

            if pos is not None:
                print(f"{imagem} encontrada")
                return pos

        except Exception as e:
            print(f"Erro ao procurar {imagem}: {e}")

        if time.time() - inicio > timeout:
            print(f"Imagem {imagem} não encontrada")
            if r == True:
                return None
            else:
                exit()

        print(f"Procurando por {imagem}... {int(time.time() - inicio)}s")
        time.sleep(0.5)


def esperar_e_clicar(imagem, timeout=30, confidence=0.8, region=None, r=False):
    pos = esperar_imagem(imagem, timeout, confidence, region, r)
    if pos is not None:
        time.sleep(1)
        pyautogui.click(pos)
        return True
    return False


time.sleep(4)

esperar_imagem("flow11.png", region=(100, 200, 200, 350), timeout=240)

# baixar videos
i = 0
while i < num_videos:
    pyautogui.rightClick((i+1)*220, 400)
    esperar_e_clicar("flow9.png")
    esperar_imagem("flow10.png")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(f"vid0.{num_videos - i}", 0.1)
    pyautogui.hotkey("enter")
    pyautogui.rightClick((i+1)*220, 400)
    esperar_e_clicar("flow8.png")
    esperar_e_clicar("flow12.png")
    time.sleep(1)
    pyautogui.hotkey("esc")
    time.sleep(1)
    i += 1


# mover para a pasta certa

time.sleep(3)
pyautogui.hotkey("ctrl", "j")
time.sleep(1)
pyautogui.moveTo(1620, 180)
esperar_e_clicar("win1.png")
time.sleep(2)
pyautogui.moveTo(esperar_imagem("win2.png"))
pyautogui.keyDown("ctrl")
i = 0
while i < num_videos:
    pyautogui.moveRel(0, 37)
    pyautogui.click()
    i += 1
pyautogui.keyUp("ctrl")
pyautogui.hotkey("ctrl", "x")
esperar_e_clicar("pc5.png")
pyautogui.moveRel(-20, 0)
pyautogui.click()
time.sleep(1)
pyautogui.typewrite(f"{pasta}")
pyautogui.hotkey("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.hotkey("win", "d")
time.sleep(3)
# capcut

pyautogui.click(330, 40, clicks=2)
esperar_e_clicar("cap1.png")
time.sleep(4)
i = 0
while i < num_videos:

    if i == 0:
        esperar_e_clicar("cap2.png")
        pos = esperar_imagem("pc2.png")
        pyautogui.moveTo(pos)
        pyautogui.moveRel(50, 0)
        time.sleep(1)
        pyautogui.click()

        pyautogui.typewrite(f"{pasta}")
        pyautogui.hotkey("enter")
    if i != 0:
        esperar_e_clicar("cap3.png")

    esperar_e_clicar("pc3.png")
    pyautogui.moveRel(100, 0)
    pyautogui.click()
    pyautogui.typewrite(f"vid0.{i + 1}", 0.2)
    time.sleep(1)
    pyautogui.hotkey("down")
    time.sleep(0.5)
    pyautogui.hotkey("enter")
    time.sleep(1)
    i += 1

pyautogui.mouseDown(170, 180)
pyautogui.mouseUp(730, 550)

pyautogui.mouseDown(410, 240)
pyautogui.moveTo(360, 830, 2)
pyautogui.mouseUp()

time.sleep(1)
pyautogui.click(1730, 10)
time.sleep(3)
pos = esperar_imagem("cap6.png", region=(850, 250, 550, 100))
pyautogui.moveTo(pos)
pyautogui.moveRel(0, -50)
pyautogui.click()
pyautogui.hotkey("ctrl", "a")
pyautogui.typewrite(f"vidtk.{num}")
time.sleep(3)
pyautogui.hotkey("enter")
time.sleep(2)
esperar_e_clicar("cap7.png")
time.sleep(2)
pyautogui.typewrite("#reformas #satisfactory #home")
time.sleep(1)
pyautogui.hotkey("enter")
