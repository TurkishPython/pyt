# python_turkish/python_turkish.py (v1.1.0 - Geriye Dönük Uyumlu Kısa İsimler)

import turtle
import os

# --- RENK ÇEVİRİ SÖZLÜĞÜ ---
RENK_ÇEVİRİ_SÖZLÜĞÜ = {
    "kırmızı": "red", "mavi": "blue", "yeşil": "green", "sarı": "yellow",
    "siyah": "black", "beyaz": "white", "mor": "purple", "turuncu": "orange",
    "kahverengi": "brown", "gri": "gray", "açıkmavi": "cyan", "koyu": "darkgreen",
    "pembe": "pink", "açıkpembe": "lightpink", "derinpembe": "deeppink",    
    "sıcaksarıpembe": "hotpink", "kızılpembe": "crimson", "salmon": "salmon"           
}

# --- TEMEL I/O, VERİ TİPİ VE MANTIKSAL KONTROL FONKSİYONLARI ---

# Yeni Kısa İsimler (V1.1.0)
def yaz(*args, **kwargs):
    """ print() fonksiyonunun Türkçe karşılığıdır. """
    return print(*args, sep=kwargs.get('ayırıcı', ' '), end=kwargs.get('sonlandırıcı', '\n'))

def girdi(mesaj=""):
    """ input() fonksiyonunun Türkçe karşılığıdır. """
    return input(mesaj)

def uzunluk(nesne):
    """ len() fonksiyonunun Türkçe karşılığıdır. """
    return len(nesne)

def tür(nesne):
    """ type() fonksiyonunun Türkçe karşılığıdır. """
    return type(nesne)

def hepsi(koleksiyon):
    """ all() fonksiyonunun Türkçe karşılığıdır. """
    return all(koleksiyon)

def herhangi(koleksiyon):
    """ any() fonksiyonunun Türkçe karşılığıdır. """
    return any(koleksiyon)

def değer_dönüştür(nesne, hedef_tip):
    """ Veri tipini dönüştürür. """
    try:
        if hedef_tip == int: return int(nesne)
        elif hedef_tip == float: return float(nesne)
        elif hedef_tip == str: return str(nesne)
        elif hedef_tip == bool: return bool(nesne)
        else: yazdır(f"Hata: Desteklenmeyen tip ({hedef_tip.__name__}) belirtildi."); return None
    except ValueError:
        yazdır(f"Hata: '{nesne}' değeri {hedef_tip.__name__} tipine dönüştürülemedi."); return None

# --- GERİYE DÖNÜK UYUMLULUK (Eski İsimler) ---

def yazdır(*args, **kwargs):
    """ Eski isim: Yeni 'yaz' fonksiyonunu çağırır. """
    return yaz(*args, **kwargs)

def girdi_al(*args, **kwargs):
    """ Eski isim: Yeni 'girdi' fonksiyonunu çağırır. """
    return girdi(*args, **kwargs)

def uzunluk_bul(nesne):
    """ Eski isim: Yeni 'uzunluk' fonksiyonunu çağırır. """
    return uzunluk(nesne)

def tür_bul(nesne):
    """ Eski isim: Yeni 'tür' fonksiyonunu çağırır. """
    return tür(nesne)

def hepsi_doğru_mu(koleksiyon):
    """ Eski isim: Yeni 'hepsi' fonksiyonunu çağırır. """
    return hepsi(koleksiyon)

def herhangi_doğru_mu(koleksiyon):
    """ Eski isim: Yeni 'herhangi' fonksiyonunu çağırır. """
    return herhangi(koleksiyon)


# --- OS / DOSYA FONKSİYONLARI ---

# Yeni Kısa İsimler (V1.1.0)
def konum():
    """ os.getcwd() fonksiyonunun Türkçe karşılığıdır. """
    return os.getcwd()

def oluştur(yol):
    """ os.makedirs() fonksiyonunun Türkçe karşılığıdır. """
    try:
        os.makedirs(yol, exist_ok=True); yaz(f"Dizin başarıyla oluşturuldu: '{yol}'"); return True
    except Exception as e:
        yaz(f"Hata: Dizin oluşturulamadı: {e}"); return False

def sil(yol):
    """ os.remove() fonksiyonunun Türkçe karşılığıdır. """
    try:
        os.remove(yol); yaz(f"Dosya başarıyla silindi: '{yol}'"); return True
    except FileNotFoundError:
        yaz(f"Hata: Silinmek istenen dosya bulunamadı: '{yol}'"); return False
    except Exception as e:
        yaz(f"Hata: Dosya silinemedi: {e}"); return False

def listele(yol="."):
    """ os.listdir() fonksiyonunun Türkçe karşılığıdır. """
    try:
        return os.listdir(yol)
    except Exception as e:
        yaz(f"Hata: Dizin listelenemedi: {e}"); return []

# Geriye Dönük Uyumluluk (Eski İsimler)
def mevcut_dizin():
    return konum()
def dizin_oluştur(*args, **kwargs):
    return oluştur(*args, **kwargs)
def dosya_sil(*args, **kwargs):
    return sil(*args, **kwargs)
def dizin_listele(*args, **kwargs):
    return listele(*args, **kwargs)


# --- GRAFİK (TURTLE) FONKSİYONLARI ---

def _renk_çevir(renk):
    """ Dahili yardımcı fonksiyon. """
    renk_kucuk = renk.lower().replace(" ", "")
    return RENK_ÇEVİRİ_SÖZLÜĞÜ.get(renk_kucuk, renk)

# Yeni Kısa İsimler (V1.1.0)
def ileri(adım):
    """ Kısa: turtle.forward() """
    return turtle.forward(adım)
def geri(adım):
    """ Kısa: turtle.backward() """
    return turtle.backward(adım)
def sağa(derece):
    """ Kısa: turtle.right() """
    return turtle.right(derece)
def sola(derece):
    """ Kısa: turtle.left() """
    return turtle.left(derece)
def kalınlık(kalınlık):
    """ Kısa: turtle.pensize() """
    return turtle.pensize(kalınlık)
def kaldır():
    """ Kısa: turtle.penup() """
    return turtle.penup()
def indir():
    """ Kısa: turtle.pendown() """
    return turtle.pendown()
def hız(hız):
    """ Kısa: turtle.speed() """
    return turtle.speed(hız)
def temizle():
    """ Kısa: turtle.clear() """
    return turtle.clear()


# Geriye Dönük Uyumlu İsimler
def ileri_git(*args, **kwargs):
    return ileri(*args, **kwargs)
def geri_git(*args, **kwargs):
    return geri(*args, **kwargs)
def sağa_dön(*args, **kwargs):
    return sağa(*args, **kwargs)
def sola_dön(*args, **kwargs):
    return sola(*args, **kwargs)
def kalınlık_ayarla(*args, **kwargs):
    return kalınlık(*args, **kwargs)
def kalem_kaldır():
    return kaldır()
def kalem_indir():
    return indir()
def hızı_ayarla(*args, **kwargs):
    return hız(*args, **kwargs)
def pencere_temizle():
    return temizle()


# Kısaltılmayan Diğer Fonksiyonlar
def çizim_başlat(başlık="Türkçe Turtle Çizimi"):
    turtle.title(başlık)
def bekle():
    turtle.done()
def noktaya_git(x, y):
    turtle.goto(x, y)
def başlangıca_git():
    turtle.home()
def renk_ayarla(renk):
    try:
        turtle.color(_renk_çevir(renk))
    except Exception:
        yaz(f"UYARI: '{renk}' rengi geçerli değil.")
def çember_çiz(yarıçap, basamak=None):
    if basamak is None:
        turtle.circle(yarıçap)
    else:
        turtle.circle(yarıçap, steps=basamak)
def nokta_koy(büyüklük=None, renk=None):
    renk_ingilizce = _renk_çevir(renk) if renk else None
    turtle.dot(büyüklük, renk_ingilizce)
def dolgu_başlat():
    turtle.begin_fill()
def dolgu_bitir():
    turtle.end_fill()
def dolgu_rengi_ayarla(renk):
    try:
        turtle.fillcolor(_renk_çevir(renk))
    except Exception:
        yaz(f"UYARI: '{renk}' dolgu rengi geçerli değil.")
def kaplumbağa_gizle():
    turtle.hideturtle()
def kaplumbağa_göster():
    turtle.showturtle()