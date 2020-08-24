import os

# os.system()
# Terminal veya uçbirim de gerçekleşmesi 
# istenen komutları çalıştırmak için 
# kullanılır.

# kullanımı 
# os.system("<konsol komutu>")
# aşağıda örnek bir kullanım mevcuttur.
os.system("ls -l")
# Bu örnekte dosyanın çalıştırıldığı klasördeki
# klasör ve dosya bilgilerini gösterir.

# Bu nerde kullanılabilir. Örneğin bir projede 
# bir kütüphanenin importerror hatası aldığını
# ve bu hatanının önlenmesi için bir yükleme 
# komutu yazılabilir.

try:
    from flask import Flask
except ImportError as e:
    os.system("pip3 install flask")

# Dipnot : Bu fonksiyon sadece Linux ve 
# Windows tarafından kullanılabilir
