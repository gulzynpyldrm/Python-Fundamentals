
# While Loop
# region Example - 1
# 0-100 arasında ki sayıları ekrana yazdıralım
# sayac = 0
# while sayac <= 100:
# 	print(sayac)
# 	sayac = sayac + 1
# endregion


# region Example - 2
# 1-101 arasındaki çif ve tek sayıların miktarını ekrana yazalım
# sayac = 1  # sayac bir çünkü soruda 1 ile 101 arasında ki sayılar istenmiş sayaç bu aralıkta ki sayıları tek tek ziyaret edecek
# # Aşağıda ki iki değişken her çift yada tek sayı yakaladığımda arttırılacak.
# cift_sayilar = 0
# tek_sayilar = 0
# while sayac < 101:
# 	if sayac % 2 == 0:
# 		cift_sayilar += 1
# 	else:
# 		tek_sayilar += 1
#
# 	sayac += 1  # sayac = sayac + 1
#
# print(f'1 - 101 arasında, {cift_sayilar} kadar çift sayı, {tek_sayilar} kadar tek sayı bulunmaktadır.')
# endregion


# region Example - 3
# 1- 1000 arasındaki çift ve teksayıların toplamını ekrana yazın
# sayac = 1
# cift_sayilarin_toplami = 0
# tek_sayilarin_toplami = 0
# while sayac <= 1000:
# 	if sayac % 2 == 0:
# 		cift_sayilarin_toplami += sayac  # cift_sayilarin_toplami = cift_sayilarin_toplami + sayac
# 	else:
# 		tek_sayilarin_toplami += sayac
# 	sayac += 1
#
# print(f'Çift Sayıların Toplamı: {cift_sayilarin_toplami}\nTek Sayıların Toplamı: {tek_sayilarin_toplami}')
# endregion


# region Example - 4
# Kullanıcıdan bir işlem türü olalım ('+', '-', vb) ve 2 adet sayı üzerinden kullanıcının istediği işlemi gerçekleştirelim. Kullanıcı klavyeden e harfi gönderirse uygulamayı durduralım. Kullanıcı isterse sonsuza kadar işlem yapabilsin.
# process_type_list = ['+', '-', '*', '/', 'e']
# while True:
# 	process = input('İşlem türü giriniz: ')
# 	if process in process_type_list:
# 		# in operatörü ile bir liste içerisinde item varsa True yoksa False döner. Yani burada kullanıcının girdiği işlem bizim işlem türü listemizde varsa True yoksa False dönecek
# 		if process == 'e':
# 			print('Uygulama kapatılıyor...!')
# 			break
# 		else:
# 			sayi_1 = int(input('Sayı giriniz: '))
# 			sayi_2 = int(input('Sayı giriniz: '))
#
# 			if process == '+':
# 				print(f'Sonuç: {sayi_1 + sayi_2}')
# 			elif process == '-':
# 				print(f'Sonuç: {sayi_1 - sayi_2}')
# 			elif process == '*':
# 				print(f'Sonuç: {sayi_1 * sayi_2}')
# 			elif process == '/':
# 				print(f'Sonuç: {sayi_1 / sayi_2}')
# 	else:
# 		print('Lütfen doğru bir işlem türü giriniz..!')
# endregion


# region Example - 5
# Kullancıdan yıl bilgisi alacağız bu yıl bilgisi 1943 ile günümüz yılı arasında ise buldunuz depilse aradığınız yılı bulunmamaktadır şeklinde feedback veren uygulamayı yazın
# from datetime import datetime
# started_date = 1943
# search_date = int(input('Aradığını yılı girin: '))
# is_exist = False
# while started_date <= datetime.now().year:
# 	if started_date == search_date:
# 		print(f'Bulundu..!\nAradığınız yıl ==> {started_date}')
# 		is_exist = True
# 		break
#
# 	started_date += 1
#
# if not is_exist:
# 	print('Aradığınız tarih bulunmamaktadır..!')
# endregion


# region Example - 6
# Tek sayıların toplamını ama continue kullanarak 0-101
sayac = 0
sum = 0
while sayac <= 101:
	sayac += 1
	if sayac % 2 != 0:
		continue
	sum += sayac
	
print(sum)
# endregion









