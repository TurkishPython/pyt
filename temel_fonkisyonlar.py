# pyt/temel_fonksiyonlar.py

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
    Kullanıcıdan bir girdi (metin) alır.
    """
    try:
        return input(mesaj)
    except EOFError:
        return ""
    except Exception as e:
        yazdır(f"Girdi alma işlemi sırasında bir hata oluştu: {e}")
        return ""

def uzunluk_bul(nesne):
    """
    Python'ın yerleşik 'len' fonksiyonunun Türkçe karşılığı.
    Bir koleksiyonun öğe sayısını döndürür.
    """
    try:
        return len(nesne)
    except TypeError as e:
        yazdır(f"Hata: '{nesne}' nesnesinin uzunluğu bulunamıyor. {e}")
        return 0
    except Exception as e:
        yazdır(f"Uzunluk bulma işlemi sırasında genel bir hata oluştu: {e}")
        return 0

def tür_bul(nesne):
    """
    Python'ın yerleşik 'type' fonksiyonunun Türkçe karşılığı.
    Verilen nesnenin türünü (tipini) döndürür.
    """
    return type(nesne)

def değer_dönüştür(nesne, hedef_tip):
    """
    Bir nesneyi belirtilen hedef tipe dönüştürür.
    
    :param nesne: Dönüştürülecek değişken veya değer (genellikle string).
    :param hedef_tip: Dönüştürülmek istenen tip (örneğin: int, float, str).
    :return: Dönüştürülmüş nesne veya None (hata durumunda).
    """
    try:
        if hedef_tip == int:
            return int(nesne)
        elif hedef_tip == float:
            return float(nesne)
        elif hedef_tip == str:
            return str(nesne)
        elif hedef_tip == bool:
            # Boş string hariç her şeyi True yapar.
            return bool(nesne)
        else:
            yazdır(f"Hata: Desteklenmeyen hedef tip ({hedef_tip.__name__}) belirtildi.")
            return None
    except ValueError:
        yazdır(f"Hata: '{nesne}' değeri {hedef_tip.__name__} tipine dönüştürülemedi.")
        return None
    except Exception as e:
        yazdır(f"Dönüştürme sırasında genel bir hata oluştu: {e}")
        return None