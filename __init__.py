# pyt/__init__.py

# --- Temel Fonksiyonlar ---
from .temel_fonksiyonlar import (
    yazdır, 
    girdi_al, 
    uzunluk_bul, 
    tür_bul, 
    değer_dönüştür,
    hepsi_doğru_mu, # <-- EKLENDİ
    herhangi_doğru_mu # <-- EKLENDİ
)

# --- Grafik Fonksiyonları (Turtle) ---
# pyt/grafik.py dosyasındaki tüm fonksiyonları dışa aktarıyoruz
from .grafik import (
    çizim_başlat, bekle, ileri_git, geri_git, 
    sağa_dön, sola_dön, renk_ayarla, kalınlık_ayarla,
    kalem_kaldır, kalem_indir,
    çember_çiz, noktaya_git, hızı_ayarla, pencere_temizle,
    başlangıca_git, nokta_koy, dolgu_başlat, dolgu_bitir, 
    dolgu_rengi_ayarla, kaplumbağa_gizle, kaplumbağa_göster
)

# --- Paket Meta Verileri ---
__version__ = "1.0.0" # <-- GÜNCEL VERSİYON

__all__ = [
    # Temel
    "yazdır", 
    "girdi_al",
    "uzunluk_bul",
    "tür_bul",
    "değer_dönüştür",
    "hepsi_doğru_mu", # <-- EKLENDİ
    "herhangi_doğru_mu", # <-- EKLENDİ
    # Grafik
    "çizim_başlat", "bekle", "ileri_git", "geri_git", 
    "sağa_dön", "sola_dön", "renk_ayarla", "kalınlık_ayarla",
    "kalem_kaldır", "kalem_indir", "çember_çiz", "noktaya_git", 
    "hızı_ayarla", "pencere_temizle", 
    "başlangıca_git", "nokta_koy", "dolgu_başlat", "dolgu_bitir", 
    "dolgu_rengi_ayarla", "kaplumbağa_gizle", "kaplumbağa_göster"
    # OS/Dosya İşlemleri (YENİ EKLEMELER)
    "mevcut_dizin", "dizin_oluştur", "dosya_sil", "dizin_listele",
]