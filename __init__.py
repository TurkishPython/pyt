# python_turkish/__init__.py

# Tüm fonksiyonları tek bir modülden (python_turkish.py) içe aktarıyoruz
from .python_turkish import *

# Paketin son versiyonu
__version__ = "1.1.0" # <-- GÜNCEL V1.1.0

__all__ = [
    # Temel I/O ve Veri (Kısa ve Uzun İsimler)
    "yaz", "yazdır", "girdi", "girdi_al", "uzunluk", "uzunluk_bul", 
    "tür", "tür_bul", "değer_dönüştür", "hepsi", "hepsi_doğru_mu", 
    "herhangi", "herhangi_doğru_mu",
    
    # OS / Dosya (Kısa ve Uzun İsimler)
    "konum", "mevcut_dizin", "oluştur", "dizin_oluştur", 
    "sil", "dosya_sil", "listele", "dizin_listele",

    # Grafik (Kısa ve Uzun İsimler)
    "çizim_başlat", "bekle", "pencere_temizle", 
    "ileri", "ileri_git", "geri", "geri_git", 
    "sağa", "sağa_dön", "sola", "sola_dön", 
    "renk_ayarla", "kalınlık", "kalınlık_ayarla", 
    "kaldır", "kalem_kaldır", "indir", "kalem_indir",
    "çember_çiz", "noktaya_git", "hız", "hızı_ayarla", 
    "başlangıca_git", "nokta_koy", "dolgu_başlat", "dolgu_bitir", 
    "dolgu_rengi_ayarla", "kaplumbağa_gizle", "kaplumbağa_göster"
]