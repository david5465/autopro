import pyautogui as p
import sys

# Definir el número máximo de intentos
max_intentos = 5

def click_imagen(image_path, confidence):
    intentos = 0
    while intentos < max_intentos:
        try:
            p.click(p.locateOnScreen(image_path, confidence=confidence))
            return True  # Si se encuentra la imagen, devuelve verdadero
        except Exception as e:
            print(f"No se encuentra la imagen en el intento {intentos + 1}")
            intentos += 1
            p.sleep(1)
    print(f"Se agotaron los intentos para encontrar la imagen: {image_path}")
    sys.exit('Fin del script')

if click_imagen('C:/David/AutoPro/img/botonmas.png', confidence=0.8):
    p.sleep(2)
    p.write('co')
    p.sleep(0.5)
    p.press('tab')
    p.sleep(0.5)
    p.write('canal')
    p.sleep(0.7)
    p.press('tab')
    p.sleep(0.5)
    p.write('desact')
    p.sleep(0.5)
    p.press('tab')
    p.sleep(0.2)
    p.write('se deriva a baja')
    p.sleep(0.5)
    p.press('tab')
    p.sleep(0.5)
    if click_imagen('C:/David/AutoPro/img/lupa.png', confidence=0.9):
        p.sleep(1)
        if click_imagen('C:/David/AutoPro/img/activo.png', confidence=0.89):
            p.sleep(1)
            if click_imagen('C:/David/AutoPro/img/aceptar.png', confidence=0.89):
                p.sleep(0.5)
                p.hotkey('ctrl','s')
                p.sleep(1.2)
                if click_imagen('C:/David/AutoPro/img/133.png', confidence=0.87):
                    p.sleep(2)
                    if click_imagen('C:/David/AutoPro/img/ea.png', confidence=0.8):
                        p.sleep(0.5)
                        p.press('up')
                        p.press('enter')
                        if click_imagen('C:/David/AutoPro/img/er.png', confidence=0.8):
                            p.sleep(0.5)
                            p.press('down')
                            p.press('enter')
                            p.sleep(0.5)
                            p.hotkey('ctrl','s')