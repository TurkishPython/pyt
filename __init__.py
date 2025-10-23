# pyt/__init__.py

# --- Temel Fonksiyonlar ---
from .temel_fonksiyonlar import yazdır, girdi_al, uzunluk_bul, tür_bul, değer_dönüştür 

# --- Grafik Fonksiyonları (Turtle) ---
from .grafik import (
    çizim_başlat, bekle, ileri_git, geri_git, 
    sağa_dön, sola_dön, renk_ayarla, kalınlık_ayarla,
    kalem_kaldır, kalem_indir,
    çember_çiz, noktaya_git, hızı_ayarla, pencere_temizle,
    başlangıca_git, nokta_koy, dolgu_başlat, dolgu_bitir, 
    dolgu_rengi_ayarla, kaplumbağa_gizle, kaplumbağa_göster
)

# --- Paket Meta Verileri ---
__version__ = "0.9.1" # <-- GÜNCEL VERSİYON

__all__ = [
    # Temel
    "yazdır", 
    "girdi_al",
    "uzunluk_bul",
    "tür_bul",
    "değer_dönüştür",
    # Grafik
    "çizim_başlat", "bekle", "ileri_git", "geri_git", 
    "sağa_dön", "sola_dön", "renk_ayarla", "kalınlık_ayarla",
    "kalem_kaldır", "kalem_indir", "çember_çiz", "noktaya_git", 
    "hızı_ayarla", "pencere_temizle", 
    "başlangıca_git", "nokta_koy", "dolgu_başlat", "dolgu_bitir", 
    "dolgu_rengi_ayarla", "kaplumbağa_gizle", "kaplumbağa_göster"
]