# python_turkish/python_turkish.py

import turtle
import os # <-- YENİ EKLEME

# --- RENK ÇEVİRİ SÖZLÜĞÜ (Global Tanımlama) ---
RENK_ÇEVİRİ_SÖZLÜĞÜ = {
    "kırmızı": "red", "mavi": "blue", "yeşil": "green", "sarı": "yellow",
    "siyah": "black", "beyaz": "white", "mor": "purple", "turuncu": "orange",
    "kahverengi": "brown", "gri": "gray", "açıkmavi": "cyan", "koyu": "darkgreen",
    
    # Pembe Tonları
    "pembe": "pink", "açıkpembe": "lightpink", "derinpembe": "deeppink",    
    "sıcaksarıpembe": "hotpink", "kızılpembe": "crimson", "salmon": "salmon"           
}

# --- TEMEL I/O, VERİ TİPİ VE MANTIKSAL KONTROL FONKSİYONLARI ---

def yazdır(*args, ayırıcı=" ", sonlandırıcı="\n"):
    """
    Python'ın yerleşik 'print' fonksiyonunun Türkçe karşılığı.
    """
    try:
        print(*args, sep=ayırıcı, end=sonlandırıcı)
    except Exception as e:
        print(f"Yazdırma işlemi sırasında bir hata oluştu: {e}")

def girdi_al(mesaj=""):
    """
    Python'ın yerleşik 'input' fonksiyonunun Türkçe karşılığı. 
    """
    try:
        return input(mesaj)
    except Exception as e:
        yazdır(f"Girdi alma işlemi sırasında bir hata oluştu: {e}")
        return ""

def uzunluk_bul(nesne):
    """
    Python'ın yerleşik 'len' fonksiyonunun Türkçe karşılığı.
    """
    try:
        return len(nesne)
    except Exception as e:
        yazdır(f"Hata: '{nesne}' nesnesinin uzunluğu bulunamıyor. {e}")
        return 0

def tür_bul(nesne):
    """
    Python'ın yerleşik 'type' fonksiyonunun Türkçe karşılığı.
    """
    return type(nesne)

def değer_dönüştür(nesne, hedef_tip):
    """
    Bir nesneyi belirtilen hedef tipe dönüştürür.
    """
    try:
        if hedef_tip == int:
            return int(nesne)
        elif hedef_tip == float:
            return float(nesne)
        elif hedef_tip == str:
            return str(nesne)
        elif hedef_tip == bool:
            return bool(nesne)
        else:
            yazdır(f"Hata: Desteklenmeyen hedef tip ({hedef_tip.__name__}) belirtildi.")
            return None
    except ValueError:
        yazdır(f"Hata: '{nesne}' değeri {hedef_tip.__name__} tipine dönüştürülemedi.")
        return None

def hepsi_doğru_mu(koleksiyon):
    """
    Python'ın yerleşik 'all' fonksiyonunun Türkçe karşılığı.
    """
    return all(koleksiyon)

def herhangi_doğru_mu(koleksiyon):
    """
    Python'ın yerleşik 'any' fonksiyonunun Türkçe karşılığı.
    """
    return any(koleksiyon)

# --- GRAFİK (TURTLE) FONKSİYONLARI ---

def _renk_çevir(renk):
    """ Dahili yardımcı fonksiyon: Türkçe rengi İngilizceye çevirir. """
    renk_kucuk = renk.lower().replace(" ", "")
    return RENK_ÇEVİRİ_SÖZLÜĞÜ.get(renk_kucuk, renk)

def çizim_başlat(başlık="Türkçe Turtle Çizimi"):
    """ Turtle çizim penceresini başlatır. """
    turtle.title(başlık)
    
def bekle():
    """ Kullanıcı pencereyi kapatana kadar çizimin ekranda kalmasını sağlar. """
    turtle.done()

def pencere_temizle():
    """ Çizim penceresindeki tüm çizimleri siler. """
    turtle.clear()
    
def ileri_git(adım):
    """ Kaplumbağayı belirtilen adım kadar ileri hareket ettirir. """
    turtle.forward(adım)

def geri_git(adım):
    """ Kaplumbağayı belirtilen adım kadar geri hareket ettirir. """
    turtle.backward(adım)

def sağa_dön(derece):
    """ Kaplumbağanın yönünü belirtilen derece kadar sağa çevirir. """
    turtle.right(derece)

def sola_dön(derece):
    """ Kaplumbağanın yönünü belirtilen derece kadar sola çevirir. """
    turtle.left(derece)

def noktaya_git(x, y):
    """ Kaplumbağayı (x, y) noktasına hareket ettirir. """
    turtle.goto(x, y)
    
def başlangıca_git():
    """ Kaplumbağayı (0, 0) başlangıç noktasına döndürür. """
    turtle.home()
    
def renk_ayarla(renk):
    """ Kalemin çizim rengini ayarlar. """
    try:
        turtle.color(_renk_çevir(renk))
    except Exception:
        yazdır(f"UYARI: '{renk}' rengi geçerli değil.")

def kalınlık_ayarla(kalınlık):
    """ Kalemin kalınlığını ayarlar. """
    turtle.pensize(kalınlık)

def kalem_kaldır():
    """ Çizim yapılmasını durdurur. """
    turtle.penup()
    
def kalem_indir():
    """ Tekrar çizim yapmaya başlar. """
    turtle.pendown()

def çember_çiz(yarıçap, basamak=None):
    """ Belirtilen yarıçapta bir çember çizer. """
    if basamak is None:
        turtle.circle(yarıçap)
    else:
        turtle.circle(yarıçap, steps=basamak)

def nokta_koy(büyüklük=None, renk=None):
    """ Kaplumbağanın mevcut konumuna nokta koyar. """
    renk_ingilizce = _renk_çevir(renk) if renk else None
    turtle.dot(büyüklük, renk_ingilizce)

def dolgu_başlat():
    """ Şekil doldurma işlemini başlatır. """
    turtle.begin_fill()

def dolgu_bitir():
    """ Şekil doldurma işlemini sonlandırır. """
    turtle.end_fill()
    
def dolgu_rengi_ayarla(renk):
    """ Doldurulacak şeklin rengini ayarlar. """
    try:
        turtle.fillcolor(_renk_çevir(renk))
    except Exception:
        yazdır(f"UYARI: '{renk}' dolgu rengi geçerli değil.")

def kaplumbağa_gizle():
    """ Kaplumbağa imlecini gizler. """
    turtle.hideturtle()
    
def kaplumbağa_göster():
    """ Kaplumbağa imlecini gösterir. """
    turtle.showturtle()

def hızı_ayarla(hız):
    """ Kaplumbağanın çizim hızını ayarlar. """
    turtle.speed(hız)

# --- İŞLETİM SİSTEMİ (OS) FONKSİYONLARI (v1.0.0) ---

def mevcut_dizin():
    """
    Python'ın yerleşik 'os.getcwd' fonksiyonunun Türkçe karşılığı.
    Çalışılan dizinin (klasörün) tam yolunu döndürür.
    """
    try:
        return os.getcwd()
    except Exception as e:
        yazdır(f"Hata: Mevcut dizin bulunamadı: {e}")
        return ""

def dizin_oluştur(yol):
    """
    Python'ın yerleşik 'os.makedirs' fonksiyonunun Türkçe karşılığı.
    Belirtilen yolda klasör (dizin) oluşturur (alt klasörleri de oluşturur).
    """
    try:
        os.makedirs(yol, exist_ok=True) # exist_ok=True, zaten varsa hata vermesini önler
        yazdır(f"Dizin başarıyla oluşturuldu: '{yol}'")
        return True
    except Exception as e:
        yazdır(f"Hata: Dizin oluşturulamadı: {e}")
        return False

def dosya_sil(yol):
    """
    Python'ın yerleşik 'os.remove' fonksiyonunun Türkçe karşılığı.
    Belirtilen yoldaki dosyayı siler.
    """
    try:
        os.remove(yol)
        yazdır(f"Dosya başarıyla silindi: '{yol}'")
        return True
    except FileNotFoundError:
        yazdır(f"Hata: Silinmek istenen dosya bulunamadı: '{yol}'")
        return False
    except Exception as e:
        yazdır(f"Hata: Dosya silinemedi: {e}")
        return False
    
def dizin_listele(yol="."):
    """
    Python'ın yerleşik 'os.listdir' fonksiyonunun Türkçe karşılığı.
    Belirtilen dizindeki (klasördeki) dosya ve klasörleri listeler.
    """
    try:
        return os.listdir(yol)
    except Exception as e:
        yazdır(f"Hata: Dizin listelenemedi: {e}")
        return []