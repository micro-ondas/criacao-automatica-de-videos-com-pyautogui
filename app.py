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


# ========= INÍCIO ========= #
# fechar vscode
pyautogui.hotkey("win", "d")
time.sleep(1)

# abrir paginaweb chatgpt
pyautogui.click(900, 50, clicks=2)
time.sleep(1)

esperar_e_clicar("chatgpt1.png")
pyautogui.click()

# pedir promps pro chat
esperar_e_clicar("chatgpt2.png")
esperar_imagem("chatgpt4.png")
pyautogui.typewrite('Chose all random')
time.sleep(1)
pyautogui.hotkey("enter")
# esperar resposta aparecer
time.sleep(4)
esperar_imagem("chatgpt4.png", region=(300, 400, 1000, 500))
# copiar prompt1
pyautogui.click(1700, 700)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
# abrir gemini
time.sleep(1)
pyautogui.hotkey("ctrl", "t")
time.sleep(2)
pyautogui.typewrite("https://gemini.google.com/u/1/app?pageId=none")
pyautogui.hotkey("enter")
# esperar carregar gemini
esperar_e_clicar("gemini1.png")
time.sleep(1)
esperar_e_clicar("gemini2.png")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

# ========= LOOP ========= #
# pedir imagens com prompts
i = 0

while i < num_imgs:
    time.sleep(1)

    pyautogui.hotkey("ctrl", "1")
    time.sleep(1)

    pyautogui.typewrite("next")
    pyautogui.hotkey("enter")

    # esperar nova resposta
    time.sleep(3)
    esperar_imagem("chatgpt4.png", region=(300, 400, 1000, 500))
    pyautogui.click(1700, 700)
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("enter")

    time.sleep(1)
    pyautogui.hotkey("ctrl", "2")

    # esperar imagem do gemini

    while True:
        print("Procurando imagem 1...")
        pos = esperar_imagem("gemini3.png", timeout=30)

        if pos is None:
            print("gemini3.png não encontrada. Encerrando.")
            break

        print("Imagem 1 encontrada!")
        time.sleep(1)

        pos2 = esperar_imagem("gemini4.png", timeout=5, r=True)

        if pos2 is not None:
            print("Imagem 2 encontrada. Voltando ao início...")
            continue

        print("Imagem 2 não encontrada. Continuando o processo...")
        pyautogui.moveTo(pos)
        pyautogui.moveRel(400, 140)
        pyautogui.rightClick()
        break

    esperar_e_clicar("pc1.png")
    if i == 0:
        time.sleep(1)
        pos = esperar_imagem("pc2.png")
        pyautogui.moveTo(pos)
        pyautogui.moveRel(50, 0)
        time.sleep(1)
        pyautogui.click()

        time.sleep(1)
        pyautogui.typewrite(
            f"{pasta}")
        pyautogui.hotkey("enter")
        time.sleep(1)

        pos = esperar_imagem("pc3.png")
        time.sleep(1)
        pyautogui.moveTo(pos)
        pyautogui.moveRel(210, 0)
        time.sleep(0.5)
        pyautogui.click()

    pos = esperar_imagem("pc3.png")
    time.sleep(1)
    pyautogui.typewrite(f"img0.{i}")
    pyautogui.hotkey("enter")

    time.sleep(1)
    # pedir imagem
    if i != num_imgs - 1:
        esperar_e_clicar("gemini2.png")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("enter")
    i += 1

# ========= VIDEO ========= #
time.sleep(4)
pyautogui.hotkey("ctrl", "t")
time.sleep(1)
pyautogui.typewrite("https://labs.google/fx/pt/tools/flow")
pyautogui.hotkey("enter")
esperar_e_clicar("flow1.png")
time.sleep(4)
i = 0

# colocar as imgs no flow
esperar_e_clicar("flow2.png")
esperar_e_clicar("flow3.png")
pos = esperar_imagem("pc2.png")
pyautogui.moveTo(pos)
pyautogui.moveRel(50, 0)
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite(f"{pasta}", 0.05)
time.sleep(0.5)
pyautogui.hotkey("enter")

pos = esperar_imagem("pc3.png")
time.sleep(1)
pyautogui.moveTo(pos)
pyautogui.moveRel(210, 0)
time.sleep(0.5)
pyautogui.click()

time.sleep(1)
esperar_imagem("pc4.png")
pyautogui.typewrite(
    '"img0.8" "img0.0" "img0.1" "img0.2" "img0.3" "img0.4" "img0.5" "img0.6" "img0.7" ', 0.2)
time.sleep(0.5)
pyautogui.hotkey("enter")

time.sleep(4)
i = 0
while i < num_videos:
    # criar videos no flow
    time.sleep(1)
    esperar_e_clicar("flow6.png")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    esperar_e_clicar("flow4.png")
    time.sleep(1)
    esperar_e_clicar("flow5.5.png")
    pyautogui.typewrite(f"img0.{i}", 0.2)
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(1)
    esperar_e_clicar("flow5.png")
    time.sleep(1)
    esperar_e_clicar("flow5.5.png")
    pyautogui.typewrite(f"img0.{1+i}", 0.2)
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(1)
    esperar_e_clicar("flow7.png")
    if i != 2:
        pyautogui.hotkey("ctrl", "1")
        time.sleep(1)
        pyautogui.typewrite("next")
        pyautogui.hotkey("enter")
        # esperar nova resposta
        time.sleep(3)
        esperar_imagem("chatgpt4.png", region=(300, 400, 1000, 500))
        # esperar_e_clicar("chatgpt3.png")
        pyautogui.click(1700, 700)
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("enter")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "3")
    i += 1

# esperar carregar os videos
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
while i < num_videos - 1:
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
pyautogui.hotkey("ctrl", "a")
time.sleep(2)
pyautogui.typewrite("#reformas #satisfactory #home")
time.sleep(1)
pyautogui.hotkey("enter")
