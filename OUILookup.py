#Librerias:
import getopt
import sys
import os
#Funciones:
#Instrucciones de uso [--help]
def ayuda():
    print(" *Utilización de parámetros:\n"
        "   ./" + sys.argv[0] + " --ip <IP> || --mac <MAC> || [--help]\n"
        "\n *Lista de Parámetros:\n"
        "   --ip <dirección IP>: Señalará, a partir de la dirección IP local, el fabricante de la tarjeta de red.\n"
        "   --mac <dirección MAC>: Señalará, a partir de la dirección MAC, el fabricante de la tarjeta de red.\n"
        "   --help: Muestra información sobre el uso del programa y parámetros.  [Opcional] \n"
        "\n ****Se requiere el archivo de texto 'dir.txt' en el mismo directorio de este programa.**\n")
    exit(1)
#Busqueda de fabricante a partir de la dirección MAC [--mac]
def dirMAC(a):
	mac = a.upper()
	#Se abre el archivo 'dir.txt' en modo lectura, con formato de codificación utf8, para sobrepasar
	#errores causados por caracteres más allá del idioma ingles predefinido por el lenguaje.
	with open('dir.txt', 'r', encoding="utf8") as texto:
		lineas = texto.readlines()
		for linea in lineas:
			linea = linea.rstrip("\n")
			#Buscar direcciones MAC con extensión
			if (linea[8] == ':'):
				if (linea[0:17] == mac):
					datos = linea.split("\t")
					print("\nMAC: "+ datos[0])
					print("Fabricante: "+ datos[-1]) 
					break
			#Buscar direcciones MAC simples
			elif (linea[0:8] == mac):
				datos = linea.split("\t")
				print("\nMAC: "+ datos[0])
				print("Fabricante: "+ datos[-1])
				break
		#En caso de no encontrarse la MAC
		else:
			print("\nMAC: "+ mac)
			print("Fabricante: Direccion MAC no encontrada")
	exit(1)
#Busqueda de fabricante a partir de la dirección IP local [--ip]
def dirIP(b):
    IP = b
    ip="  "+IP
    os.system('arp -a >Arp.txt')
    with open('Arp.txt', 'r') as texto:
    	lineas = texto.readlines()
    	for linea in lineas:
    		linea = linea.rstrip("\n")
    		linea=linea.split("       ")
    		if(linea[0]==ip):
    			mac=linea[1]
    			mac=mac[3:11]
    			mac=mac.replace("-",":")
    			dirMAC(mac)
    			break
    		

    exit(1)


#Código Principal:
#Intenta conseguir valor de los parámetros:
try:
    opts, args = getopt.getopt(sys.argv[1:],"",['ip=', 'mac=', 'help'])
#En caso de no conseguir ningún valor por parámetro, error:
except:
    print("\n **** ERROR: Parámetros incorrectos. ****\n")
    ayuda()
#Uso de los parámetros:
for opt, arg in opts:
    if opt in ('--help'):
        ayuda()
    elif opt in ('--mac'):
        dirMAC(arg)
    elif opt in ('--ip'):
        dirIP(arg)
#Obligatoriedad de parámetros:
print("\n **** ERROR: Se requiere al menos un parámetro para funcionar. ****\n")
ayuda()



