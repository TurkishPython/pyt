# setup.py

# Bu dosya, temel olarak setuptools'un "setup" fonksiyonunu çağırır.
# setuptools, modern yapılandırma için pyproject.toml dosyasındaki bilgileri kullanacaktır.
# Bu, eski araçlarla uyumluluk sağlamak için bir yedektir.

from setuptools import setup # type: ignore

if __name__ == "__main__":
    # setup() fonksiyonunu çağırıyoruz. 
    # setuptools bunu görünce, metadata için pyproject.toml'a bakacaktır.
    setup()
    