# python-turkish: Türkçe Python Geliştirme Paketi (v1.1.0)

`python-turkish`, Python öğrenimini Türkçeleştiren, temel fonksiyonları ve sık kullanılan modül komutlarını içeren **hızlı, kararlı ve sadeleştirilmiş** bir pakettir.

Bu paket, kullanıcıları standartlardan saptırmak yerine, yabancı dil bariyerini aşarak **kavramları ana dilde öğrenme** sürecini hızlandıran bir başlangıç köprüsü görevi görür.

### 🌟 V1.1.0 Yenilikleri: Hız, Akıcılık ve Sadeleştirme

Bu sürüm, topluluk geri bildirimleri doğrultusunda paket kullanımını **daha kısa ve akıcı** hale getirmiştir. Eski uzun komutlar (örneğin `yazdır` ve `uzunluk_bul`) **geriye dönük uyumluluk** için korunmuştur.

| Kategori | V1.1.0 KISA İSİM | V1.0.0 ESKİ İSİM | Orijinal Komut |
| :---: | :---: | :---: | :---: |
| **Temel I/O** | `yaz()` | `yazdır()` | `print()` |
| **Girdi** | `girdi()` | `girdi_al()` | `input()` |
| **Veri Kontrol** | `uzunluk()`, `tür()` | `uzunluk_bul()`, `tür_bul()` | `len()`, `type()` |
| **Mantıksal** | `hepsi()`, `herhangi()` | `hepsi_doğru_mu()`, `herhangi_doğru_mu()` | `all()`, `any()` |
| **OS/Dizin** | `konum()` | `mevcut_dizin()` | `os.getcwd()` |
| **OS/İşlem** | `oluştur()`, `sil()` | `dizin_oluştur()`, `dosya_sil()` | `os.makedirs()`, `os.remove()` |
| **Grafik (Örn.)** | `ileri()`, `hız()` | `ileri_git()`, `hızı_ayarla()` | `forward()`, `speed()` |

---

## 🇹🇷 Kurulum ve Kullanım

### Kurulum

Paketi kurmak için `pip` kullanabilirsiniz:

```bash
pip install python-turkish