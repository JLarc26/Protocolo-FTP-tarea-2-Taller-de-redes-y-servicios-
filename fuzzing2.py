from scapy.all import *
import random

ip_servidor = "172.17.0.2"
puerto = 21

payloads_malformados = [
    b"A" * 1000 + b"\r\n",
    b"\x00\x01\x02\x03\x04\x05\r\n",
    b"USER " + b"A" * 500 + b"\r\n",
    b"PASS " + b"\xff" * 100 + b"\r\n",
    b"RETR " + b"/" * 200 + b"\r\n",
    b"\r\n\r\n\r\n",
    b"!@#$%^&*()_+\r\n",
    b"USER\x00admin\r\n",
    b"STOR " + b"." * 300 + b"\r\n",
    b"\xff\xfe" * 50 + b"\r\n",
]

print("Iniciando fuzzing con payloads malformados...")
for i, payload in enumerate(payloads_malformados):
    pkt = IP(dst=ip_servidor)/TCP(dport=puerto, flags="PA")/Raw(load=payload)
    send(pkt, verbose=0)
    print(f"[FUZZING {i+1}] Enviado payload malformado de {len(payload)} bytes")

print("Fuzzing completado.")
