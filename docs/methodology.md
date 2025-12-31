# Siber Güvenlik Metodolojisi

Bu belge, HackMasters takımı olarak siber güvenlik testlerinde izlediğimiz metodolojiyi özetler.

## 1. Keşif (Reconnaissance)
Hedef sistem hakkında mümkün olduğunca fazla bilgi toplama aşamasıdır.
- Pasif Bilgi Toplama: OSINT araçları, whois sorguları.
- Aktif Bilgi Toplama: Port taramaları, servis versiyon tespiti.

## 2. Tarama ve Zafiyet Analizi (Scanning & Enumeration)
Tespit edilen servisler üzerinde zafiyet taraması yapılır.
- Zafiyet Tarayıcıları kullanımı.
- Manuel doğrulama.

## 3. İstismar (Exploitation)
Doğrulanmış zafiyetlerin kullanılarak sisteme erişim sağlanması.
- Exploit kullanımı.
- Yetki yükseltme (Privilege Escalation).

## 4. Kalıcılık (Persistence)
Sistemde kalıcı erişim sağlamak için arka kapıların (backdoor) bırakılması (Sadece eğitim/simülasyon amaçlıdır).

## 5. Raporlama
Bulguların teknik ve yönetici özeti olarak raporlanması.
