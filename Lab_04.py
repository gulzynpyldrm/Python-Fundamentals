
# For Loop
# For loop geçmeden önce incelememiz gerek bir kaç tane yadımcı operatör ve fonksiyon bulunmaktadır. Bunlar "in" & "not in" ayrıca range() fonksiyonudur.

# "in" operatörü bir liste içerisinde aranan ifade geçiyorsa True geçmiyorsa False döner. Şunu unutmayalım string ifadelerde karakter dizileridir yani bir string ifadeye "in" operatörünü kullanabiliriz.

# "not in" operatörü ise "in" operatörünün tam tersi mantıkta çalışır aranan ifade geçmiyorsa True geçiyorsa False döner.

# name = 'Mike Tyson'

# print('b' in name)
# print('m' in name)
# print('M' in name)

# print('M' not in name)
# print('b' not in name)


# range() fonksiyonu for loop ile sıklıkla kullanılan bir yapıdır.
# range(100) fonsiyonu içerisine burada olduğu gibi 100 değerini verirsek bize 0-99 arasında bir tam sayı listesi döner.
# unutmayın range içerisine bir argüman verildiğinde verilen argümanı "n" kabul edersek "n-1" kadar çalışır. Ayrıca yine aynı senaryoda range default olarak sıfırdan başladı. Biz aksini söylemediğimiz sürece range default olarak hep sıfırdan başlayacaktır.
# for i in range(10):
	# print(i) burada print() fonksiyonu değerleri alt alta yazmaktadır. bunu yan yana yazdırmanın yolunu bulun
	
# range() fonksiyonuna 2 argüman verirsek örneğin 5 ile 10. 5 ten başlayarak 10 kadar bir sayı listesi döner
# range() fonksiyonuna 2 argüman verildiğinde birinci argüman başlangıç değerini ikinci argüman ise bitiş değerini temsil eder.
# for i in range(5, 10):
# 	print(i)

# range() 3 argüman verirsek. 1. argüman başlangıç, ikinci argüman bitiş, üçüncü argüman ise adım miktarını temsil eder
# for i in range(1, 21, 2):
# 	print(i)

# 1-100 arasındaki çift ve tek sayıların toplamını
# ciftlerin_toplami = 0
# teklerin_toplami = 0
# for i in range(1, 101):  # while loop olduğu gibi adım miktarını biz arttırmıyoruz aksini söylemediğimiz sürece 1 olarak yani dafult bir kabul edip çalışır
# 	if i % 2 == 0:
# 		ciftlerin_toplami += i
# 	else:
# 		teklerin_toplami += i
#
# print(f'Ciftlerin Toplamı: {ciftlerin_toplami}\nTeklerin Toplamı: {teklerin_toplami}')


# Kullanıcıdan başlangıç bitiş ve adım miktalarını alalım. BU şartlara bağlı kalarak her bir adımda ki sayının kareni alarak ekrana yazlaım
# çıktıyı şu formatta istiyorum 1. adımda ki sonuç: 2



