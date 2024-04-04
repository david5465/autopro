import tkinter as tk
from tkinter import messagebox, ttk 
import subprocess
import time
import threading

script_en_ejecucion = False
proceso_script = None
ultimo_tiempo = None  
estado_actual = "Ready" 

def actualizar_estado(texto=None):
    global estado_actual
    if texto:
        estado_actual = texto
    estado_label.config(text="Status: " + estado_actual)
    root.after(1000, actualizar_estado)  # Actualiza el estado cada segundo
    
def actualizar_contador():
    global ultimo_tiempo
    if ultimo_tiempo:
        segundos_transcurridos = int(time.time() - ultimo_tiempo)
        contador_label.config(text="T: " + str(segundos_transcurridos))
    else:
        contador_label.config(text="T:0")
    root.after(1000, actualizar_contador)       

def ejecutar_script_en_thread(script, duracion_maxima=None):
    thread = threading.Thread(target=ejecutar_script, args=(script, duracion_maxima))
    thread.start()

def ejecutar_script(script, duracion_maxima=None):
    global script_en_ejecucion, proceso_script, ultimo_tiempo
    if not script_en_ejecucion:
        ultimo_tiempo = time.time()  # Guarda el momento actual
        script_en_ejecucion = True
        actualizar_estado("Working: " + script)
        try:
            proceso_script = subprocess.Popen(["python", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            print(f"Error al iniciar el script: {e}")
            script_en_ejecucion = False
            actualizar_estado("Listo")
            return
        
        inicio = time.time()  # Hora de inicio del script
        while proceso_script and proceso_script.poll() is None:
            time.sleep(1)  # Espera activa
            root.update()  # Importante para permitir que la GUI se actualice
            if duracion_maxima:
                tiempo_transcurrido = time.time() - inicio
                progreso = min(int(tiempo_transcurrido / duracion_maxima * 100), 100)
                barra_progreso['value'] = progreso

        if proceso_script:
            for line in proceso_script.stdout:
                print(line.decode(), end='')
            for line in proceso_script.stderr:
                print(line.decode(), end='')
            
        script_en_ejecucion = False
        proceso_script = None
        actualizar_estado("Listo")
        barra_progreso.stop()
    else:
        messagebox.showwarning("Advertencia", "Ya hay un script en ejecución.")
            

def detener_script():
    global script_en_ejecucion, proceso_script
    if script_en_ejecucion:
        proceso_script.terminate()
        script_en_ejecucion = False
        proceso_script = None
        actualizar_estado("Script detenido")
        barra_progreso.stop()
    else:
        messagebox.showwarning("Advertencia", "No hay ningún script en ejecución.")


root = tk.Tk()
root.title("Ejecutar Scripts")
root.geometry("500x360-1620+500")

estado_label = tk.Label(root, text="No script played yet")
estado_label.pack()

contador_label = tk.Label(root, text="T:0")
contador_label.pack()

barra_progreso = ttk.Progressbar(root, orient="horizontal", length=100, mode="determinate")
barra_progreso.pack()

def ejecutar_script_1():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script1.py")
        
def ejecutar_script_2():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script2.py")
    
def ejecutar_script_3():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script3.py")

def ejecutar_script_4():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script4.py")
    
def ejecutar_script_5():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script5.py")
    
def ejecutar_script_6():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script6.py")
    
def ejecutar_script_7():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script7.py")

def ejecutar_script_8(): 
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script8.py")
        
def ejecutar_script_9(): 
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script9.py")

def ejecutar_script_10():
    ejecutar_script_en_thread("C:/David/AutoPro/scripts/script10.py")


button_script_1 = tk.Button(root, text="Reset", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script1.py", 1.5))
button_script_1.pack()

button_script_2 = tk.Button(root, text="Info", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script5.py", 12))
button_script_2.pack()

button_script_3 = tk.Button(root, text="Factu", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script3.py", 12))
button_script_3.pack()

button_script_4 = tk.Button(root, text="Corta", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script4.py", 12))
button_script_4.pack()

button_script_5 = tk.Button(root, text="vicio", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script2.py", 12))
button_script_5.pack()

button_script_6 = tk.Button(root, text="Deriv", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script6.py", 12))
button_script_6.pack()

button_script_7 = tk.Button(root, text="cerrar", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script7.py", 6))
button_script_7.pack()

button_script_8 = tk.Button(root, text="ctrl C", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script8.py", 1.5))
button_script_8.pack()

button_script_9 = tk.Button(root, text="ctrl v", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script9.py", 1.5))
button_script_9.pack()

button_script_10 = tk.Button(root, text="Vnb", width=5, height=1, command=lambda: ejecutar_script_en_thread("C:/David/AutoPro/scripts/script10.py", 10))
button_script_10.pack()

button_detener = tk.Button(root, text='Stop', fg="white", bg="red", width=4, height=1, command=detener_script)
button_detener.pack()

actualizar_contador()

actualizar_estado()

root.mainloop()





