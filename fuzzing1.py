from scapy.all import *
import random
import string

def generar_comando_aleatorio():
    comandos = ['ABOR', 'ACCT', 'ALLO', 'APPE', 'CDUP', 'CWD', 'DELE', 
                'HELP', 'LIST', 'MKD', 'MODE', 'NLST', 'NOOP', 'PASS', 
                'PASV', 'PORT', 'PWD', 'QUIT', 'REIN', 'REST', 'RETR', 
                'RMD', 'RNFR', 'RNTO', 'SITE', 'SIZE', 'SMNT', 'STAT', 
                'STOR', 'STOU', 'STRU', 'SYST', 'TYPE', 'USER']
    comando = random.choice(comandos)
    argumento = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1,20)))
    return f"{comando} {argumento}\r\n".encode()

ip_servidor = "172.17.0.2"
puerto = 21

print("Iniciando fuzzing con comandos FTP aleatorios...")
for i in range(10):
    payload = generar_comando_aleatorio()
    pkt = IP(dst=ip_servidor)/TCP(dport=puerto, flags="PA")/Raw(load=payload)
    send(pkt, verbose=0)
    print(f"[FUZZING {i+1}] Enviado: {payload.decode().strip()}")

print("Fuzzing completado.")
