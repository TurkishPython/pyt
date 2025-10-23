# pyt/grafik.py

import turtle

# --- RENK ÇEVİRİ SÖZLÜĞÜ (Türkçe -> İngilizce) ---
RENK_ÇEVİRİ_SÖZLÜĞÜ = {
    "kırmızı": "red", "mavi": "blue", "yeşil": "green", "sarı": "yellow",
    "siyah": "black", "beyaz": "white", "mor": "purple", "turuncu": "orange",
    "kahverengi": "brown", "gri": "gray", "açıkmavi": "cyan", "koyu": "darkgreen",
    
    # Pembe Tonları (Yeni Eklenenler)
    "pembe": "pink",             
    "açıkpembe": "lightpink",    
    "derinpembe": "deeppink",    
    "sıcaksarıpembe": "hotpink", 
    "kızılpembe": "crimson",     
    "salmon": "salmon"           
}

# --- TEMEL PENCERE KONTROLÜ ---

def çizim_başlat(başlık="Türkçe Turtle Çizimi"):
    """
    Turtle çizim penceresini başlatır ve başlığı ayarlar.
    """
    turtle.title(başlık)
    
def bekle():
    """
    Kullanıcı pencereyi kapatana kadar çizimin ekranda kalmasını sağlar. (turtle.done())
    """
    turtle.done()

def pencere_temizle():
    """
    Çizim penceresindeki tüm çizimleri siler ancak kaplumbağayı hareket ettirmez. (turtle.clear)
    """
    turtle.clear()
    
# --- HAREKET VE KONUM ---

def ileri_git(adım):
    """
    Kaplumbağayı belirtilen adım kadar ileri hareket ettirir. (turtle.forward)
    """
    turtle.forward(adım)

def geri_git(adım):
    """
    Kaplumbağayı belirtilen adım kadar geri hareket ettirir. (turtle.backward)
    """
    turtle.backward(adım)

def sağa_dön(derece):
    """
    Kaplumbağanın yönünü belirtilen derece kadar sağa (saat yönüne) çevirir. (turtle.right)
    """
    turtle.right(derece)

def sola_dön(derece):
    """
    Kaplumbağanın yönünü belirtilen derece kadar sola (saat yönünün tersine) çevirir. (turtle.left)
    """
    turtle.left(derece)

def noktaya_git(x, y):
    """
    Kaplumbağayı koordinat sisteminde (x, y) noktasına hareket ettirir. (turtle.goto)
    """
    turtle.goto(x, y)
    
def başlangıca_git():
    """
    Kaplumbağayı (0, 0) başlangıç noktasına döndürür ve çizimi temizler. (turtle.home)
    """
    turtle.home()
    
# --- ÇİZİM KALEMİ VE ŞEKİL ---

def renk_ayarla(renk):
    """
    Kalemin çizim rengini ayarlar. Türkçe isimleri otomatik olarak İngilizce'ye çevirir. (turtle.color)
    """
    renk_kucuk = renk.lower().replace(" ", "")
    renk_ingilizce = RENK_ÇEVİRİ_SÖZLÜĞÜ.get(renk_kucuk, renk)

    try:
        turtle.color(renk_ingilizce)
    except Exception:
        print(f"UYARI: '{renk}' rengi geçerli bir Türkçe isim veya Hex kodu değildir.")

def kalınlık_ayarla(kalınlık):
    """
    Kalemin kalınlığını ayarlar. (turtle.pensize)
    """
    turtle.pensize(kalınlık)

def kalem_kaldır():
    """
    Kaplumbağa hareket ettiğinde çizim yapmasını durdurur. (turtle.penup)
    """
    turtle.penup()
    
def kalem_indir():
    """
    Kaplumbağa hareket ettiğinde tekrar çizim yapmaya başlar. (turtle.pendown)
    """
    turtle.pendown()

def çember_çiz(yarıçap, basamak=None):
    """
    Belirtilen yarıçapta bir çember çizer. (turtle.circle)
    """
    if basamak is None:
        turtle.circle(yarıçap)
    else:
        turtle.circle(yarıçap, steps=basamak)

def nokta_koy(büyüklük=None, renk=None):
    """
    Kaplumbağanın mevcut konumuna nokta koyar. (turtle.dot)
    """
    if renk:
        renk_kucuk = renk.lower().replace(" ", "")
        renk_ingilizce = RENK_ÇEVİRİ_SÖZLÜĞÜ.get(renk_kucuk, renk)
    else:
        renk_ingilizce = None
        
    if büyüklük and renk_ingilizce:
        turtle.dot(büyüklük, renk_ingilizce)
    elif büyüklük:
        turtle.dot(büyüklük)
    elif renk_ingilizce:
        turtle.dot(None, renk_ingilizce)
    else:
        turtle.dot()

# --- DOLGU İŞLEMLERİ ---

def dolgu_başlat():
    """
    Şekil doldurma işlemini başlatır. (turtle.begin_fill)
    """
    turtle.begin_fill()

def dolgu_bitir():
    """
    Şekil doldurma işlemini sonlandırır ve şekli mevcut dolgu rengiyle doldurur. (turtle.end_fill)
    """
    turtle.end_fill()
    
def dolgu_rengi_ayarla(renk):
    """
    Doldurulacak şeklin rengini ayarlar. Türkçe isimleri çevirir. (turtle.fillcolor)
    """
    renk_kucuk = renk.lower().replace(" ", "")
    renk_ingilizce = RENK_ÇEVİRİ_SÖZLÜĞÜ.get(renk_kucuk, renk)
    
    try:
        turtle.fillcolor(renk_ingilizce)
    except Exception:
        print(f"UYARI: '{renk}' dolgu rengi geçerli değil.")

# --- KAPLUMBAĞA GÖRÜNÜMÜ ---

def kaplumbağa_gizle():
    """
    Kaplumbağa imlecini gizler. (turtle.hideturtle)
    """
    turtle.hideturtle()
    
def kaplumbağa_göster():
    """
    Kaplumbağa imlecini gösterir. (turtle.showturtle)
    """
    turtle.showturtle()

def hızı_ayarla(hız):
    """
    Kaplumbağanın çizim hızını ayarlar. (turtle.speed)
    """
    turtle.speed(hız)