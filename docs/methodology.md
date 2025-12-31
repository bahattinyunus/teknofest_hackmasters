# 🛡️ Siber Güvenlik Metodolojisi: HackMasters Standartları

Bu belge, **Teknofest HackMasters** takımı ve geliştiricileri olarak, siber güvenlik operasyonlarında, sızma testlerinde (Penetration Testing) ve zafiyet analizlerinde izlediğimiz bilimsel ve etik temelli metodolojiyi en ince ayrıntısına kadar açıklar. Bir siber güvenlik operasyonu, sadece araçları çalıştırmak değil, stratejik bir akıl yürütme sürecidir.

## 1. Planlama ve Hazırlık (Scope & Engagement)
Herhangi bir teknik işleme başlamadan önce, operasyonun sınırları (Scope), yasal izinleri ve hedef hedefleri (Objectives) netleştirilir. Bu aşama, siber güvenliğin "Etik" kısmının temelini oluşturur.
- **ROE (Rules of Engagement):** Saldırının hangi saatlerde yapılacağı, hangi sistemlerin kapsam dışı olduğu ve keşfedilen kritik açıkların bildirilme prosedürleri netleştirilir.

## 2. Keşif ve Bilgi Toplama (Reconnaissance)
Hedef sistem hakkında mümkün olduğunca fazla veri toplama aşamasıdır. Başarılı bir sızma testinin %70'i kaliteli bilgi toplamaya dayanır.
- **Pasif Bilgi Toplama (OSINT):** Hedefe dokunmadan; arama motorları, sosyal medya, WHOIS kayıtları, Shodan ve DNS geçmişi üzerinden yapılan araştırmalardır. Gizlilik bu aşamada esastır.
- **Aktif Bilgi Toplama:** Hedefle doğrudan etkileşim kurarak; port taramaları, alt alan adı (subdomain) tespiti ve servis versiyon sorgulamaları yapılır. Burada sistemin tepkileri analiz edilir.

## 3. Tarama ve Zafiyet Analizi (Scanning & Enumeration)
Tespit edilen servisler üzerinde, bilinen (CVE) veya mantıksal zafiyetlerin aranması sürecidir.
- **Zafiyet Tarayıcıları:** Nessus, OpenVAS veya özelleştirilmiş `scanner.py` gibi araçlarla otomatik taramalar gerçekleştirilir.
- **Manuel Doğrulama:** Otomatik araçların ürettiği "False Positive" sonuçları ayıklanır ve derinlemesine manuel analizler yapılarak zafiyetin gerçekliği teyit edilir.

## 4. İstismar (Exploitation)
Doğrulanmış zafiyetlerin kullanılarak, sömürülme aşamasıdır. Bu aşamada temel amaç, sisteme ilk girişi (Initial Access) sağlamaktır.
- **Hassas Müdahale:** Sistem stabilitesini bozmadan, sadece zafiyeti kanıtlayacak düzeyde exploit kodları çalıştırılır.
- **Payload Yönetimi:** Hedef sistemde çalıştırılacak olan kodun (reverse shell vb.) tespiti zorlaştıran (Obfuscation) tekniklerle hazırlanması.

## 5. Yetki Yükseltme ve Kalıcılık (Post-Exploitation)
Sisteme giriş yaptıktan sonra, düşük yetkili kullanıcıdan yüksek yetkili (Root/Administrator) kullanıcıya geçiş yapma ve erişimi koruma sürecidir.
- **Privilege Escalation:** İşletim sistemi çekirdek zafiyetleri veya yanlış yapılandırılmış servisler üzerinden tam kontrol sağlanır.
- **Kalıcılık (Persistence):** Eğitim amaçlı senaryolarda, sistem reboot edildiğinde bile erişimin devam etmesi için kullanılan yasal tekniklerin simülasyonu yapılır.

## 6. Raporlama ve Temizlik (Reporting & Cleanup)
Operasyonun en kritik aşamasıdır. Keşfedilen tüm açıklar, risk puanları (CVSS) ve çözüm önerileri ile birlikte belgelenir.
- **Teknik Detaylar:** Yazılımcılar ve sistem adminleri için adım adım zafiyetin nasıl kapatılacağı anlatılır.
- **İzlerin Silinmesi:** Test sırasında oluşturulan geçici dosyalar, kullanıcılar ve log kayıtları temizlenerek sistem orijinal haline döndürülür.

---
> "Siber güvenlikte en iyi savunma, saldırganın nasıl düşündüğünü bilmektir."
