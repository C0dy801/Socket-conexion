import argparse
import socket as soc
from cryptography.fernet import Fernet
from time import sleep
from dotenv import load_dotenv
import os
from colorama import Fore
import threading


load_dotenv()
KEY = os.getenv('KEY')
F = Fernet(KEY)

#Argumentos
args = argparse.ArgumentParser(description="Conexion")
args.add_argument('-H','--host',type=str,required=True,help="Example: --host 127.0.0.1")
args.add_argument('-p','--port',type=int,required=True,help="Example: --port 4444")
args.add_argument('-u','--user',required=True,help="Example: --user JohnDoe")
parser = args.parse_args()


def conn(Host,port,user):
    with soc.socket(soc.AF_INET,soc.SOCK_STREAM) as connexion:
        try:
            print("[*]Cargando....")
            sleep(1.5)
            connexion.connect_ex((Host,port))
            print(f"Conexion establecida en la ip: {Host} y el puerto: {port}")
            while True:
                serv = connexion.recv(4096).decode('utf-8')
                if not serv:
                    msg = "[*] No se recivieron datos"
                    print(Fore.CYAN+msg)
                    break
                if serv.lower()=="exit":
                    print()

                try:
                    encrypt_serv = F.encrypt(serv.encode('utf-8'))
                    descrypt_serv = F.decrypt(encrypt_serv).decode('utf-8')
                    print(descrypt_serv)
                except Exception as e:
                    print(f"Error: {e}")

                msg_user = input("Usted: ")
                encrypt_msg = F.encrypt(msg_user.encode('utf-8'))
                payload = f"{user}: ".encode('utf-8') + encrypt_msg
                connexion.send(payload)

        except Exception as e:
            print(e)

def main():
    if parser.host and parser.port and parser.user:
        t = threading.Thread(target=conn,args=(parser.host,parser.port,parser.user)).start()
    else:
        print("[*]Debe ingresar un host,puerto y usuario!")

if __name__ == "__main__":
   main()