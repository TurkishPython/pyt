
from temel_fonksiyonlar import yazdır
from grafik import (
    çizim_başlat, bekle, ileri_git, sağa_dön, sola_dön, 
    renk_ayarla, kalınlık_ayarla, kalem_kaldır, kalem_indir,
    çember_çiz, noktaya_git, hızı_ayarla, pencere_temizle,
    başlangıca_git, nokta_koy, dolgu_başlat, dolgu_bitir, 
    dolgu_rengi_ayarla, kaplumbağa_gizle, kaplumbağa_göster
)

yazdır("----------------------------------------")
yazdır("PYT 0.9.1 Grafik Modülü Tüm Fonksiyonlar Testi")

# --- 1. AYARLAR VE BAŞLATMA ---
çizim_başlat("Türkçe Grafik Testi - Dolgulu Hilal")
pencere_temizle()
hızı_ayarla(0) # En hızlı (anında çizim)
kaplumbağa_gizle() # Kaplumbağayı gizle

# --- 2. ZEMİN (DOLGU TESTİ) ---
dolgu_rengi_ayarla("kırmızı")
renk_ayarla("kırmızı") # Çizgi rengi
kalınlık_ayarla(3)

# Bayrak dikdörtgeni için başlangıç noktasına git
kalem_kaldır()
noktaya_git(-200, -150)
kalem_indir()

# Kırmızı dolguyu başlat
dolgu_başlat()
for _ in range(2):
    ileri_git(400)
    sola_dön(90)
    ileri_git(300)
    sola_dön(90)
dolgu_bitir()

# --- 3. BÜYÜK BEYAZ ÇEMBER (HİLALİN BÜYÜK KISMI) ---
dolgu_rengi_ayarla("beyaz")
kalem_kaldır()
noktaya_git(-100, 0) # Hilal merkezine git
kalem_indir()
dolgu_başlat()
çember_çiz(100)
dolgu_bitir()

# --- 4. KÜÇÜK KIRMIZI ÇEMBER (HİLAL ŞEKLİNİ OLUŞTURMA) ---
# Beyaz çemberin üstüne kırmızı çember çizerek hilal şeklini oluşturuyoruz.
dolgu_rengi_ayarla("kırmızı")
kalem_kaldır()
noktaya_git(-75, 0) # Kırmızı çemberin merkezine git
kalem_indir()
dolgu_başlat()
çember_çiz(80) # Beyazdan daha küçük kırmızı çember
dolgu_bitir()

# --- 5. EKSTRA TESTLER ---

# Pembe Tonu ve Nokta Koyma Testi
kalem_kaldır()
noktaya_git(150, 100)
kaplumbağa_göster()
renk_ayarla("derinpembe")
nokta_koy(20, "sıcaksarıpembe")

# Başlangıca Dönme Testi
başlangıca_git()
hızı_ayarla(5) # Hızı normale çevir

yazdır("Tüm grafik fonksiyonları kullanıldı. Çizim tamamlandı.")
bekle() 
yazdır("----------------------------------------")