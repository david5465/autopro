import time
import signal
import sys
import pyautogui

def ejecutar_accion():
    print("Ejecutando acción con PyAutoGUI")
    pyautogui.hotkey('ctrl', 'alt', 'z')
    pyautogui.hotkey('ctrl', 'alt', 'r')
    

def main():
    ejecutar_accion_cada = 180  # segundos

    def handler(sig, frame):
        print("Deteniendo el script...")
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)

    while True:
        ejecutar_accion()
        time.sleep(ejecutar_accion_cada)

main()
   