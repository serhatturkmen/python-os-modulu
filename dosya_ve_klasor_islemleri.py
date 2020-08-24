import os

# os.getcwd()
# çalıştırılan dosyanın konumu(dosya yolu) geri döndürür.

os_getcwd = os.getcwd()
print(os_getcwd)

# os.chdir()
# Klasör Değiştir(Change Directory)
# bu komut verdiğiniz klasörün konumuna geçiş yapmanızı
# sağlar.

os.chdir(path="/home/serhat/Desktop")
print(os.getcwd())

# os.listdir()
# Bulunduğu klasördeki dosya ve klasörleri geriye liste
# olarak döndürür.

os.chdir(path="/home/serhat/Desktop/python-os-modulu")
os_listdir = os.listdir()
print(os_listdir)

# 2. bir yol olarak istersek listdir(path) şeklinde
# kullanabiliriz.

os_listdir = os.listdir(path="/home/serhat/Desktop/python-os-modulu")
print(os_listdir)

# birde sonuç listesini for döngüsüyle yazdırabilirsiniz.
# örneği biraz daha derinleştirip sadece .py uzantılı
# dosyaları yazdırmasını isteyelim

python_files = os.listdir(path="/home/serhat/Desktop/python-os-modulu")
for python_file in python_files:
    if python_file.endswith(".py"):
        print(python_file)

# os.mkdir()
# Not : Windows için geçerli değildir.
# Bulunduğu klasörde bir klasör oluşturmak için kullanılır.
# Bunu da iki yol ile yapabiliriz.

# ilk yol

#os.mkdir("/home/serhat/Desktop/python-os-modulu/YeniKlasor")

# Bu yolda path kısmına konum ve klasör adı yazıldı.

# 2. yol

#os.mkdir("NewFolder")

# Bu yol pek tercih edilen bir yol değildir. Çünkü projede 
# kullanırken chdir() komutu kullanılmışsa nerede 
# oluşturulduğunu bilmek zorlaşır.

# Tamam diyelim ki klasör oluştu. Ve bir nedenle 
# dosyayı tekrar çalıştırmak zorunda kaldınız.
# Klasör var olduğundan mkdir komutlarında hata
# alırsınız. Çünkü bu fonksiyon klasörün var olup
# olmadığına bakmaz sadece oluşturmaya çalışır.

# Peki biz bu hatayı nasıl çözeriz. İki yolu vardır.
# 1. Try - Excpetion bloklarıyla
# 2. os.path.exists(<FolderName>) fonksiyonuyla 

# 1. yoldan başlayalım
try:
    os.mkdir("NewFolder")
except FileExistsError as e:
    pass
# FileExistsError bu hata oluşturmak istenen
# klasörün var olduğunu geri döndüren bir hatadır.
# İstek halinde pass yerine print ile durum 
# mesajı yazdırılabilir.

# 2. yol os.path.exists() fonksiyonu
# Bu fonksiyon belirtilen konumda klasörün içinde
# aranılan değerin var olup olmadığını kontrol eder
# var ise geriye True yok ise geriye False değeri 
# döndürür.
if not os.path.exists(path="NewFolder"):
    os.mkdir("NewFolder")

# os.rename()
# konumu belirtilen dosya veya klasörün adını
# değiştirmek için kullanılır.

# önce klasör yoksa oluşturduk
if not os.path.exists(path="HelloWorld"):
    os.mkdir("HelloWorld")
# sonra da ismini değiştirdik
try:
    os.rename(src="HelloWorld", dst="MerhabaDunya")
except OSError as E:
    print("Klasör içeriği boş değil.")

# Dipnot : Eğer klasör içeriği boş değilse hata alınır.
# Ondan dolayı try - expection ile hatayı kontrol altına
# alıp hatasız çalışmasını sağlamış olduk.

# aynı işlemi dosya için yapalım
if not os.path.exists(path="first.txt"):
    open("first.txt","w")

# open() methodu dosya açmak için kullanılır.
# İçeriğine erişmek değiştirmek için kullanılır.
# Erişim seçenekleri vardır.

os.rename(src="first.txt", dst="second.txt")
# rename(<eski dosya adi>, <yeni dosya adi>)
# şeklinde parametreler alır.

# os.rmdir()
# İçi boş olan klasörleri silmek için kullanılır.

#os.rmdir("MerhabaDunya")

# Eğer içi boş değilse ya da silme işleminde
# hata çıkar. Bu hatanın çıkmasını engellemek
# için try-expection veya listdir() fonksiyonu
# ile döndürülen listenin değer sayısına
# bakılarak eğer 0 ise silinebilir değilse silinemez
# olduğunu ekrana yazdırılabilir.

try:
    os.rmdir("MerhabaDunya")
except OSError as e:
    print("Silinmesi istenen klasör içeriği boş değil.")

# os.stat()
# Konumu verilen bir dosyanın veya klasörün boyutu, 
# oluşturulma tarihi, değiştirilme tarihi gibi
# bilgileri döndürür.

# klasör için

#print(os.stat("HelloWorld"))
if os.path.exists("/home/serhat/Desktop/python-os-modulu/HelloWorld"):
    print(os.stat("HelloWorld"))
else:
    print("Klasör Bulunamadı.")


# dosya için
if os.path.exists("/home/serhat/Desktop/python-os-modulu/README.md"):
    print(os.stat("README.md"))
else:
    print("Dosya Bulunamadı.")

# os.walk()
# Bulunduğu klasörün içindeki klasörleri ve 
# dosyaları ve ayrıca klasörlerin içeriğini 
# ağaç yapısı mantığında listeleyip object
# olarak geri döndürür. Bu . Üç parametresi 
# vardır listedeki her bir birimi bunlar 
# kök-dizin, alt-dizin ve dosyalardır.

os_walk = os.walk("/home/serhat/Desktop/python-os-modulu")

for value in os_walk:
    print(value)

# os.path class ı
# Bu class ta 3 method öğreneceğiz.
# Bunlar exists(), isdir() ve isfile()

# os.path.exists()
# Dosya veya klasörün belirtilen konumda var olup
# olmadığını kontrol eder. Eğer var ise True yok
# ise False değeri döndürür.

print(os.path.exists("/home/serhat/Desktop"))
# True
print(os.path.exists("/home/serhat/Olmayan klasor"))
# False

print(os.path.exists("second.txt"))
# True
print(os.path.exists("yokboylebirdosya.txt"))
# False

# Farklı konumdaki dosyaları kontrol etmek için chdir()
# ile konum değiştirilir ve öyle sorgulanır.

# os.path.isdir()
# Bu komut verilen konumun klasör olup olmadığını
# kontrol eder. Klasör ise True değilse False değeri
# döndürür.

print(os.path.isdir("/home/serhat/Desktop/python-os-modulu"))
print(os.path.isdir("/home/serhat/Desktop/python-os-modulu/README.md"))

# os.path.isfile()
# Bu komut verilen konumun dosya olup olmadığını
# kontrol eder. Dosya ise True değilse False değeri
# döndürür.

print(os.path.isfile("/home/serhat/Desktop/python-os-modulu/README.md"))
print(os.path.isfile("/home/serhat/Desktop/python-os-modulu"))


# Dikkat dosya yollarını değiştirmelisiniz denemek için
# aksi takdirde hata almanız kaçınılmaz olur.
