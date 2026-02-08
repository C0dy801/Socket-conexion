from colorama import Fore
import socket as soc
from time import sleep
import argparse

msg = 'Loading...'
print(Fore.GREEN+msg)
sleep(1)
Parser = argparse.ArgumentParser(description="Conexion listener!")
#Conexion
def conexion(ip,port):
    with soc.socket(soc.AF_INET,soc.SOCK_STREAM) as conn:
        try:
            conn.connect_ex((ip,port))
            print(f"Conexion en la ip:{ip} y puerto:{port}")
            while True:
                serv = conn.recv(4096).decode('utf-8')
                print(f"Serv: {serv}")
                if serv.lower()=="exit":
                    break
        #Manejo de errores
        except soc.timeout:
            print("Conexion agotada")
            sleep(1)
        except ConnectionError as e:
            print(f"Problemas con: {e}")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    host = Parser.add_argument('--host',required=True,help="Conexion al host ejemplo: --host 127.0.0.1")
    port = Parser.add_argument('--port',required=True,help="Conexion del puerto ejemplo: --port 4444")
    args = Parser.parse_args()
    if args.host and args.port:
        conexion(args.host,args.port)
    else:
        print("Debe poner un host y un puerto especifico para conectarse! ejemplos: --host 127.0.0.1 --port 4444")
