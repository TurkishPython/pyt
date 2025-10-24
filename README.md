# python-turkish: Türkçe Python Geliştirme Paketi (v1.0.1)

## README.md Güncellemesi

`python-turkish`, Python öğrenimini ve kullanımını Türkçe konuşanlar için sadeleştirmeyi amaçlayan, temel fonksiyonları ve sık kullanılan modül komutlarını Türkçeleştiren **kararlı** bir pakettir.

Proje, kullanıcıları standartlardan saptırmak yerine, yabancı dil bariyerini aşarak **kavramları ana dilde öğrenme** sürecini hızlandıran bir **başlangıç köprüsü** görevi görür.

### 🌟 V1.0.1 ile Öne Çıkan Ana Özellikler

Bu sürümde, paketin işlevselliği temel komutların ötesine taşınmış ve gerçek dünya uygulamaları için OS (İşletim Sistemi) entegrasyonu eklenmiştir.

| Kategori | Türkçe Karşılığı | Orijinal Komut |
| :---: | :---: | :---: |
| **Temel I/O** | `yazdır()`, `girdi_al()` | `print()`, `input()` |
| **Veri Kontrol** | `uzunluk_bul()`, `tür_bul()` | `len()`, `type()` |
| **Mantıksal** | `hepsi_doğru_mu()`, `herhangi_doğru_mu()` | `all()`, `any()` |
| **Veri Dönüşüm** | `değer_dönüştür()` | `int()`, `float()`, `str()` |
| **OS/Dosya İşl.** | `dizin_oluştur()`, `dosya_sil()` | `os.makedirs()`, `os.remove()` |
| **OS/Dizin** | `mevcut_dizin()`, `dizin_listele()` | `os.getcwd()`, `os.listdir()` |
| **Grafik (Turtle)** | `ileri_git()`, `çember_çiz()`, `renk_ayarla()` | `forward()`, `circle()`, `color()` |

---

## 🇹🇷 Kurulum ve Kullanım

### Kurulum

Paketi kurmak için `pip` kullanabilirsiniz:

```bash
pip install python-turkish