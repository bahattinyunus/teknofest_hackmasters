import sys
import socket
import argparse
from datetime import datetime

def scan_target(target, ports):
    print(f"[*] Hedef taranıyor: {target}")
    print(f"[*] Başlangıç zamanı: {datetime.now()}")
    
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} açık")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Tarama iptal edildi.")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Hedef sunucu çözümlenemedi.")
        sys.exit()
    except socket.error:
        print("\n[!] Sunucuya bağlanılamadı.")
        sys.exit()

def main():
    parser = argparse.ArgumentParser(description="HackMasters Basit Port Tarayıcı")
    parser.add_argument("target", help="Taranacak hedef IP veya domain")
    parser.add_argument("--ports", nargs="+", type=int, default=[21, 22, 80, 443, 3306, 8080], help="Taranacak portlar (varsayılan: 21 22 80 443 3306 8080)")
    
    args = parser.parse_args()
    
    print("-" * 50)
    print("      TEKNOFEST HACKMASTERS GÜVENLİK TARAYICI      ")
    print("-" * 50)
    
    scan_target(args.target, args.ports)

if __name__ == "__main__":
    main()
