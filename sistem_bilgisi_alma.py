# author : DOT

# os dosya fonksiyonlarını kullanabilmek
# için kütüphaneyi import etmemiz gerekiyor
# İpucu :: Bu kütüphane python kurulumuyla
# gelmektedir. Herhangi bir kurulum gerektirmez.
import os

# os.name
# Bu dosyanın çalıştığı işletim sistemini geri
# döndürür

resultname = os.name
print(resultname)

# Çıktıda 
# posix  -> Linux
# nt     -> Windows
# java   -> Macos
# şeklinde sonuçlar alıp karşılıkları yanına
# yazılmıştır.

# Peki bunun kolay yolu yok mu?
# Elbette python diliyse var :D

# os.uname()
# methodu ile system bilgilerini bir dizi 
# ile alabiliriz

print(os.uname())

# posix.uname_result(
#   sysname='Linux', 
#   nodename='serhat-PC', 
#   release='4.15.0-30deepin-generic', 
#   version='#31 SMP Fri Nov 30 04:29:02 UTC 2018', 
#   machine='x86_64'
# )

# Çıktısı bu şekilde olacaktır. Açıklamalarına
# bakalım

# -> sysname = İşletim Sistemi bilgisini verir.
# -> nodename = Sistemin aktif kulanıcı adını verir.
# -> release = İşletim sisteminin sürümünü verir.
# -> version = İşletim sisteminin versiyonunu ve 
# güncelleme tarihini verir.
# -> machine = İşletim sisteminin 32 bit mi 64 bit mi
# olduğunu verir.

# sadece birini yazdırmak veya değişkene atmak istersek
# ne yapmalıyız?

resultuname = os.uname()

uname_sysname = resultuname[0]
uname_nodename = resultuname[1]
uname_release = resultuname[2]
uname_version = resultuname[3]
uname_machine = resultuname[4]

# Değişkene atmayı gördük yazdırmaya gelelim.

print(uname_sysname)
print(uname_nodename)
print(uname_release)
print(uname_version)
print(uname_machine)

# Başka bir yolu daha var. Platform kütüphanesi
# ile sistem bilgilerini alabilirsiniz.

import platform

# platform.system()

# Hangi işletim sistemini kullandığını verir.
platform_system = platform.system()

print(platform_system)

# İşletim sisteminin hangi sürümünü kullandığını
# verir.
platform_release = platform.release()

print(platform.release())
