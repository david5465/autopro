import csv
import pyautogui
import time

# Mapeo de nombres de teclas especiales a códigos de teclas de PyAutoGUI
KEY_MAP = {
    'CAPITAL': 'capslock',
    'VK_A': 'a',
    'VK_B': 'b',
    'VK_C': 'c',
    'VK_D': 'd',
    'VK_E': 'e',
    'VK_F': 'f',
    'VK_G': 'g',
    'VK_H': 'h',
    'VK_I': 'i',
    'VK_J': 'j',
    'VK_K': 'k',
    'VK_L': 'l',
    'VK_M': 'm',
    'VK_N': 'n',
    'VK_O': 'o',
    'VK_P': 'p',
    'VK_Q': 'q',
    'VK_R': 'r',
    'VK_S': 's',
    'VK_T': 't',
    'VK_U': 'u',
    'VK_V': 'v',
    'VK_W': 'w',
    'VK_X': 'x',
    'VK_Y': 'y',
    'VK_Z': 'z',
    'LCONTROL': 'ctrl',
    'LMENU': 'alt',
    'LSHIFT': 'shift',
    'TAB': 'tab'
}

# Función para ejecutar una acción según los datos del CSV
def ejecutar_accion(accion):
    x, y = int(accion[0]), int(accion[1])
    tiempo = float(accion[3])
    repeticiones = int(accion[5])
    
    if accion[4] == 'KeyDown':
        key = KEY_MAP.get(accion[2], accion[2])
        for _ in range(repeticiones):
            pyautogui.keyDown(key)
            time.sleep(tiempo)
    elif accion[4] == 'KeyUp':
        key = KEY_MAP.get(accion[2], accion[2])
        for _ in range(repeticiones):
            pyautogui.keyUp(key)
            time.sleep(tiempo)
    elif accion[4] == 'MouseMove':
        pyautogui.moveTo(x, y, duration=tiempo)
    elif accion[4] == 'MouseWheelDown':
        amount = int(accion[2])
        pyautogui.scroll(-amount)
        time.sleep(tiempo)
    elif accion[4] == 'MouseWheelUp':
        amount = int(accion[2])
        pyautogui.scroll(amount)
        time.sleep(tiempo)
    elif accion[4] == 'MouseDown':
        button = accion[2].lower()  # Botón del mouse (izquierda, derecha, medio)
        for _ in range(repeticiones):
            pyautogui.mouseDown(x, y, button=button)
            time.sleep(tiempo)
    elif accion[4] == 'MouseUp':
        button = accion[2].lower()  # Botón del mouse (izquierda, derecha, medio)
        for _ in range(repeticiones):
            pyautogui.mouseUp(x, y, button=button)
            time.sleep(tiempo)
    elif accion[4] == 'Click':
        for _ in range(repeticiones):
            pyautogui.click(x, y)
            time.sleep(tiempo)
    elif accion[4] == 'RightClick':
        for _ in range(repeticiones):
            pyautogui.rightClick(x, y)
            time.sleep(tiempo)
    elif accion[4] == 'MiddleClick':
        for _ in range(repeticiones):
            pyautogui.middleClick(x, y)
            time.sleep(tiempo)
    elif accion[4] == 'DoubleClick':
        for _ in range(repeticiones):
            pyautogui.doubleClick(x, y)
            time.sleep(tiempo)
    elif accion[4] == 'SendKeys':
        texto = accion[2]
        for _ in range(repeticiones):
            pyautogui.typewrite(texto)
            time.sleep(tiempo)

# Función para leer el archivo CSV y ejecutar las acciones
def ejecutar_csv(nombre_archivo):
    with open(nombre_archivo, newline='', encoding='utf-16') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')
        for i, fila in enumerate(lector_csv):
            ejecutar_accion(fila)
    

# Nombre del archivo CSV con las acciones
nombre_archivo = 'acciones.csv'

# Ejecutar las acciones del archivo CSV
ejecutar_csv(nombre_archivo)
