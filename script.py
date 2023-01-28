import pyautogui
import os
import time
import argparse
import pyperclip

# Creamos las variables que hay que pasarle al script
parser = argparse.ArgumentParser()
parser.add_argument("IP", help="IP de la máquina")
parser.add_argument("NOMBRE", help="Nombre de la máquina")
args = parser.parse_args()

# Abrimos una terminal en el escritorio 1, para que todo lo demás funcione (sin tener una terminal en ese escritorio no funcionaría el flujo del programa)
os.system("bspc desktop -f 6 $(kitty) &")

# Cambiamos hacía el escritorio 1 y esperamos
os.system("bspc desktop -f 6 &")
time.sleep(0.5)

#Cambiamos al directorio de la VPN
pyautogui.typewrite('cd ')
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('home') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('luk') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('Desktop') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('HTB') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('VPN') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'l')

# Escribimos la conexión VPN
pyautogui.typewrite('sudo openvpn lab_LukiiiMohh.ovpn') # <--------------------------------- AQUÍ
pyautogui.press('enter')
time.sleep(7)

# Abrimos una terminal en el escritorio 1, para que todo lo demás funcione (sin tener una terminal en ese escritorio no funcionaría el flujo del programa)
os.system("bspc desktop -f $(kitty) &")

# Cambiamos hacía el escritorio 1 y esperamos
os.system("bspc desktop -f 1 &")
time.sleep(0.5)

# Creamos el directorio de la máquina
os.system(f"mkdir -p ~/Desktop/HTB/Machines/{args.NOMBRE}HTB") # <--------------------------------- AQUÍ

# Configuramos la terminal base
pyautogui.hotkey('super', 'enter')

#Vamos a la carpeta que le corresponde a la máquina, es tan largo porque pyautogui es una mierda que no detecta las / como strings
pyautogui.typewrite('cd ')
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('home') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('luk') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('Desktop') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('HTB') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite('Machines') # <--------------------------------- AQUÍ
pyautogui.hotkey('shift', '7')
pyautogui.typewrite(args.NOMBRE)
pyautogui.typewrite('HTB') # <--------------------------------- AQUÍ
pyautogui.press('enter')

# Hacemos 'mkt' dentro del directorio de la máquina que corresponde para crear las carpetas necesarias
pyautogui.typewrite('mkt') # <--------------------------------- AQUÍ
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'l')

# Entramos al directorio de nmap
pyautogui.typewrite('cd nmap') # <--------------------------------- AQUÍ
pyautogui.press('enter')

# Escribimos el comando de nmap y lo dejamos sin ejecutar
pyautogui.typewrite('sudo nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn ') # <--------------------------------- AQUÍ
pyautogui.typewrite(args.IP)
pyautogui.typewrite(' -oG allPorts') # <--------------------------------- AQUÍ
pyautogui.hotkey('ctrl', 'l')
pyautogui.press('enter')
time.sleep(7) # <--------------------------------- AQUÍ

# CambiarNTAB
pyautogui.hotkey('ctrl', 'shift', 'alt', 't')

# Cambiamos el nombre a 'Scanning'
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'k')
pyautogui.typewrite('Scanning') # <--------------------------------- AQUÍ
pyautogui.press('enter')

# TAB NOMBRE Y CAMBIAMOS AL DIRECTORIO DE NMAP
pyautogui.hotkey('ctrl', 'shift', 't')

# CambiarNTAB
pyautogui.hotkey('ctrl', 'shift', 'alt', 't')

# Cambiamos el nombre a 'NOMBRE'
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'k')
pyautogui.typewrite(args.NOMBRE) # <--------------------------------- AQUÍ
pyautogui.press('enter')

# Salimos del directorio de nmap (salimos aquí porque antes al haber dejado un comando listo para ejecutar, el de nmap si escribiamos algo se rompía el comando)
pyautogui.typewrite('cd ..') # <--------------------------------- AQUÍ
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'l')

# TAB NC
pyautogui.hotkey('ctrl', 'shift', 't')

# CambiarNTAB
pyautogui.hotkey('ctrl', 'shift', 'alt', 't')

# Cambiamos el nombre a 'NC'
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'k')
pyautogui.typewrite('NC') # <--------------------------------- AQUÍ
pyautogui.press('enter')

# Dejamos el comando del NC en el puerto que solemos utilizar
pyautogui.typewrite('nc -lvnp 4456') # <--------------------------------- AQUÍ

# TAB Exploits
pyautogui.hotkey('ctrl', 'shift', 't')

# CambiarNTAB
pyautogui.hotkey('ctrl', 'shift', 'alt', 't')

# Cambiamos el nombre a 'Exploits'
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'k')
pyautogui.typewrite('Exploits') # <--------------------------------- AQUÍ
pyautogui.press('enter')

# Entramos dentro del directorio exploits
pyautogui.typewrite('cd exploits') # <--------------------------------- AQUÍ
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'l')

# Ejecutamos msfconsole 
pyautogui.typewrite('msfconsole') # <--------------------------------- AQUÍ
pyautogui.press('enter')
