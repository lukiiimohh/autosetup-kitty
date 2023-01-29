## <img src="/icons/espana.png" width="25px"/>
<details>
<summary>README en Español</summary>

<h1 align="center">
  <img width=25px src=icons/linux-tux.png>
  TAMOSHACK SCRIPT
</h1>

Este es un script que funciona en mi entorno `BPSWM` y en el sistema operativo <img width="15px" src="icons/arch-linux-icon.png" />RCH.


**1.-** El script consiste en que te abre una terminal, `kitty` (en mi caso, se puede cambiar) en el escritorio 6 y te escribe el comando para que inicies la VPN.


**2.-** Luego se va al escritorio 1 y abre otra nueva terminal la cual se ubica en un directorio que se crea gracias a los parámetros que le vamos a pasar al script en la ruta que queramos. En mi caso `/home/luk/Desktop/HTB/Machines/NombreHTB`. Y que dentro de este mismo directorio crea 3 carpetas con un comando predefinido que tengo en la `~/.zshrc` que es `mkt`, el cual crea los directorios `content, exploit, nmap`.


**3.-** Luego crea `tabs` nuevas en kitty con los nombres de `Scanning - Nombre - NC - Exploits`  
En cada una de estas se escriben unos comandos, en los cuales si hace falta que el usuario ponga su contraseña, esperará 7 segundos.

<details>
<summary>¿Que comandos pone?</summary>
  
**Scanning**  
Escribe el comando `sudo nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn IP -oG allPorts`  
El cual va a ejecutar un escaneo con nmap a la IP que le hemos otorgado al ejecutar el script. Si quieres saber que hace cada parámetro mira esta página: https://explainshell.com/explain?cmd=sudo+nmap+-p-+--open+-sS+--min-rate+5000+-vvv+-n+-Pn+IP+-oG+allPorts


**Nombre**  
En este apartado no se escribe nada simplemente está pensado para que el usuario escriba los comandos necesarios durante el proceso de resolución de la máquina.


**NC**  
Escribe el comando `nc -lvnp 4456` el cuál es mi puerto favorito cuando me pongo en escucha para entablar conexión con algún agente externo, pero se puede cambiar.


**Exploits**  
Inicia la consola de metasploit con `msfconsole`. Se puede quitar o cambiar por alguna otra cosa.

</details>

<details>
<summary>Como cambiar el script a tu manera y como hacer un alias</summary>

**¿Cómo cambio mi script?**  
Bueno una vez que ya sabemos como funciona el script es hora de modificarlo, pues viene con mis ajustes y por lo tanto a tí no te van a funcionar. 
En el propio script hay algo tal que así `# <--------------------------------- AQUÍ` eso significa que ahí puedes cambiar algún tipo de información por lo que tu quieras.  

Por ejemplo cuando nos encontramos esta línea:
```python
pyautogui.typewrite('luk') # <--------------------------------- AQUÍ
```
Significa que donde pone `luk` podemos cambiar a nuestro usuario, por ejemplo `pepito`. Y así con todas las demás líneas que nos encontramos.


**¿Cómo hago un alias?**  
Si queremos que nuestro script se llame con un alias, en lugar de tener que invocar el comando entero y que además podamos ejecutarlo desde cualquier terminal que use la shell que tengamos podemos hacerlo como indico abajo.

**1.- Saber que shell estamos usando**  
Para saber la shell que estamos usando debemos hacerlo con el comando `echo $SHELL` en mi caso el resultado es este.  
<img src=icons/echoshell.png>  
Por lo que estoy usando la shell `zsh`.

**2.- Modificar nuestro archivo de configuración**  
Una vez tenemos esta información es hora de ir a nuestro archivo de configuración de shell que normalmente está ubicado en `~/.TUSHELLrc` en mi caso `~/.zshrc`.  
Solo debemos de crear un alias que invoque al script y decirle que le vamos a pasar 2 argumentos, siendo el argumento `$1` la IP y el argumento `$2` el NOMBRE.
  
Aquí dejo una imagen de como queda mi `~/.zshrc`  
<img src=icons/aliaszshrc.png>

</details>

Una vez que tengamos todo hecho el script lo podemos ejecutar con `alias $IP $NOMBRE` o si no hemos creado el alias `python3 /ruta/al/archivo/script.py IP NOMBRE`

</details>


## <img src="/icons/reino-unido.png" width="25px"/>
<details>
<summary>English README</summary>
  
<h1 align="center">
  <img width=25px src=icons/linux-tux.png>
  TAMOSHACK SCRIPT
</h1>

This is a script that works in my `BPSWM` environment and on the <img width="15px" src="icons/arch-linux-icon.png" />RCH operating system

**1.-** The script consists of opening a terminal, `kitty` (in my case, can be changed) on desktop 6 and writing the command to start the VPN.

**2.-** Then it goes to desktop 1 and opens another new terminal which is located in a directory that is created thanks to the parameters that we will pass to the script in the path we want. In my case `/home/luk/Desktop/HTB/Machines/NameHTB`. And that within this same directory creates 3 folders with a predefined command that I have in the `~/.zshrc` that is `mkt`, which creates the directories `content, exploit, nmap`.

**3.-** Then it creates new `tabs` in kitty with the names of `Scanning - Name - NC - Exploits`
In each of these a few commands are written, in which if the user needs to enter their password, it will wait for 7 seconds.

<details>
<summary>What commands does it place?</summary>

**Scanning**  
It writes the command `sudo nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn IP -oG allPorts`
Which will execute a scan with nmap to the IP that we have given to the script when executed. If you want to know what each parameter does look at this page: https://explainshell.com/explain?cmd=sudo+nmap+-p-+--open+-sS+--min-rate+5000+-vvv+-n+-Pn+IP+-oG+allPorts

**Name**  
In this section nothing is written, it is simply thought for the user to write the necessary commands during the machine resolution process.

**NC**  
It writes the command `nc -lvnp 4456` which is my favorite port when I listen for connection with some external agent, but it can be changed.

**Exploits**  
It starts the metasploit console with `msfconsole`. It can be removed or changed for something else.

</details>

<details>
<summary>How to change the script to your liking and how to make an alias</summary>

**How do I change my script?**  
Well once we know how the script works it's time to modify it, as it comes with my settings and therefore it won't work for you.
In the script itself there is something like this `# <--------------------------------- AQUÍ` (AQUÍ is spanish, because I am a native spanish speaker) that means that you can change some information there for what you want.

For example when we find this line:
```python
pyautogui.typewrite('luk') # <--------------------------------- AQUÍ
```
Means that where it says `luk` we can change to our user, for example `james`. And so with all the other lines that we find.

**How do I make an alias?**  
If we want our script to be called with an alias, instead of having to invoke the entire command and also be able to run it from any terminal that uses the shell we have, we can do it as indicated below.

**1.- Know what shell we are using**  
To know the shell we are using, we must do it with the command `echo $SHELL` in my case the result is this.  
<img src=icons/echoshell.png>  
So I am using the `zsh` shell.

**2.- Modify our configuration file**  
Once we have this information, it is time to go to our shell configuration file, which is normally located in `~/.YOURSHELLrc` in my case `~/.zshrc`.
We only need to create an alias that invokes the script and tell it that we are going to pass 2 arguments, being the argument `$1` the IP and the argument `$2` the NAME.

Here is an image of how my `~/.zshrc` looks like  
<img src=icons/aliaszshrc.png>  

</details>

Once we have everything done, the script can be executed with `alias $IP $NAME` or if we haven't created the alias `python3 /path/to/file/script.py IP NAME`

</details>

## Video 📸
Aquí tienes un vídeo para ver como funciona el script `/` Here you can see a video of how the script works!  
https://youtu.be/XEXcTLyDg6Q
