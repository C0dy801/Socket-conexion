import socket as soc
import argparse
import time


#Argumentos
parser = argparse.ArgumentParser(description="Conexion listener!")

#Argumentos del host y puerto
parser.add_argument('--host',required=True,type=str,help="Conexion al host ejemplo: --host 127.0.0.1")
parser.add_argument('--port',required=True,type=int,help="Conexion del puerto ejemplo: --port 4444")

Parsers = parser.parse_args()


#Conexion
conexion = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
if Parsers.host and Parsers.port:
    try:
        serv = conexion.connect_ex((Parsers.host,Parsers.port))
        while True:
            if serv == 0:
                print(f"Conexion del host:{Parsers.host}, Puerto en:{Parsers.port}")
                msg = conexion.recv(4096).decode('utf-8')
                if msg.lower()=="exit":
                    print("Conexion Terminada")
                    break
                print(msg)

            else:
                print("Error al conectarse")
    #Manejo de errores
    except soc.timeout:
        print("Conexion agotada")
        time.sleep(1)
    except ConnectionError as e:
        print(f"Problemas con: {e}")
        time.sleep(1)
    except Exception as e:
        print(f"Problemas con {e}")
        time.sleep(1)
else:
    print("Debe poner un host y un puerto especifico para conectarse! ejemplos: --host 127.0.0.1 --port 4444")