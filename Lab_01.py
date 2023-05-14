
# Değişken (Variable)
# Yazılım dillerinde değişkenleri kutulara benzetebiliriz. Nasıl ki gündelik hayatımızda kutularda eşyalar saklayabiliyorsak yazılımda değişkenler içerisinde anlık olarak değerler saklayabiliriz.

# Diğer programlama dillerinde değişken tanımlarken ilk önce değişkenin tipi sonra adını ve sonrada üzerine değer atarız. Burada şu hususa dikkat etmeliyiz. Değişkenimizi tanımlarken (declare) bir değişken tipine onu bağladık. Yani uygulama çalıştığı sürece "x" değişkeninin tipi "int". Burada ki önemli nokta artık "x" değişkenine string bir değer atayamam.
# int x = 10

# Pythonda değişken tanımlarken herhangi bir tip belirtmiyoruz.
# x = 10
# Bir tip belirtmediğimiz için değişkenimiz anlık olarak içerisine atılan değerin tipine bürünmektedir.
# x = "Marilyn Monreo"

# first_name = "Zeynep Yılmaz"
#
# print(first_name)
# Burada print() bulit-in fonkssiyonu aracılığı ile değişken üzerinde tutulan ifadeyi ekrana yazdırdık.

# first_name = 10
# Yukarıda ki satırda first_name değişkeni içerisine 10 değerini atadık. gördüğünüz gibi istediğimiz değeri değişken içerisine atayabiliyoruz. Bu özellik C, C++, C#, Java, PHP gibi programlama dillerinde bulunmamaktadır.
# print(first_name)
# print() algoritmada kullandığımız output olarak düşünebilirsiniz.

# region Example - 1
# Kullanıcıdan alınan 2 adet sayı üzerinden temel 4 işlem yapan uygulama
# Kullanıcıdan input alırken python içerisinde built-in olarak bulunan input() fonksiyonunu kullanıyoruz. Daha sonra kullanıcıyı doğru yönlendirmek için içerisne bir mesaj yazıyoruz. Lakin şunu unutmayalım kullanıcıdan her değer aldığımızda bize gelen valunun tipi string. Artikmatiksel işlem yapmak istediğdmizde bize gelen değeri int değişken tipine dönüştürmemiz gerekmektedir.
# sayi_1 = int(input("Lütfen bir sayı giriniz: "))
# sayi_2 = int(input("Lütfen bir sayı giriniz: "))
#
# toplam = sayi_1 + sayi_2
# cikarma = sayi_1 - sayi_2
# carpma = sayi_1 * sayi_2
# bolme = sayi_1 / sayi_2
#
# print(f'Sonuç: {toplam}')
# print(f'Çikarma işleminin sonucu: {cikarma}')
# print('{} x {} = {}'.format(sayi_1, sayi_2, carpma))
# print(f'{sayi_1} / {sayi_2} = {bolme}')
# endregion


# region Example - 2
"""
Kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulamayı yazınız
"""
# kenar = int(input("Lütfen kenar giriniz: "))
# # Yukarıda kullanıcıdan alınan input int() fonksiyonu aracılığıyla int tipine dönüştürdük çünkü kullanıcıdan gelen değeri aritmatiksel işleme sokacağım.
# cevre = kenar * 4
# alan = kenar * kenar
#
# print(f'Cevre: {cevre}')
# print(f'Alan: {alan}')
# endregion


# region Example - 3
# Kullanıcıdan alınan kısa ve uzun kenar bilgilerine göre bir dikdörtgenin alanını ve çevresini hesaplayın
# x = int(input("Kısa kenar: "))
# y = int(input("Uzun kenar: "))
#
# print(f'Alan: {x * y}')
# print(f'Cevre: {2 * (x + y)}')
# enderegion

# region Example - 4
# Üçgenin alanını hesaplayalım
# taban = float(input("Taban değeri giriniz: "))
# yukseklik = float(input("Yukseklik değeri giriniz: "))
#
# print(f'Alan: {taban * yukseklik / 2}')
# endregion

















