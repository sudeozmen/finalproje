topkisi=0
numaralar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
liste=[]
class çalışan():
    ad="ahu"
    soyad="ulu"
    yas=23
    tür="yarı zamanlı"
    num="053285282"
print("hosgeldiniz\n")
tarih=input("tarihi giriniz\n")
film1=input("salon 1 de gösterime girecek film:\n")
film2=input("salon 2 de gösterime girecek film:\n")
film3=input("salon 3 de gösterime girecek film:\n")
film4=input("salon 4 de gösterime girecek film:\n")
film5=input("salon 5 de gösterime girecek film:\n")
salon={"salon1":film1,"salon2":film2,"salon3":film3,"salon4":film4,"salon5":film5}
print(tarih,"tarihinde gösterimdeki filmler:",salon)
film=input("gidilecek film:\n")
if film==film1:
   while 1:
      ogr=int(input("öğrenci bileti sayısı:\n"))
      tam=int(input("tam bilet sayısı:\n"))
      kisi=tam+ogr
      topkisi=+kisi
      if topkisi>=20:
          print("bu salonda yer kalmamıştır\n")
      isim=input("ad soyad:\n")
      tel=input("telefon numarası:\n")
      for i in range (0,kisi):
          koltuk = input("koltuk numarası(1 ile 20 arasında):\n")
          if koltuk in numaralar:
              liste=+koltuk
              if koltuk in liste:
                  print("bu numara alınmıştır başka bir numara seçiniz\n")
                  break
      def çarp(sayi1,sayi2):
          return sayi1*sayi2
      çarp(ogr,15)
      çarp(tam,20)
      def topla(sayi1,sayi2):
          return sayi1+sayi2
      topla(çarp(ogr,15),çarp(tam,20))
      fiyat=topla(çarp(ogr,15),çarp(tam,20))
      uye=int(input("üyeyse 1e değilse 0a basın\n"))
      if uye==0:
          print("fatura tutarı:\n",fiyat)
      elif uye==1:
          def indirim(sayi):
              return sayi-(sayi*5/100)
          indirim(fiyat)
          menuler = {"menu1": 20, "menu2": 25}
          print("aşağıda menüler ve fiyatları verilmiştir\n", menuler)
          menu=int(input("menü almak istemiyorsa 0a birinci menü için 1e ikinci menü için 2ye basın\n"))
          if menu==0:
              print("fatura tutarı:\n",indirim(fiyat))
          elif menu==1:
              yemek=int(20-(20*5/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
          elif menu==2:
              yemek=int(25-(25*4/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
      break
elif film==film2:
   while 1:
      ogr=int(input("öğrenci bileti sayısı:\n"))
      tam=int(input("tam bilet sayısı:\n"))
      kisi=tam+ogr
      topkisi=+kisi
      if topkisi>=20:
          print("bu salonda yer kalmamıştır\n")
      isim=input("ad soyad:\n")
      tel=input("telefon numarası:\n")
      for i in range (0,kisi):
          koltuk = input("koltuk numarası(1 ile 20 arasında):\n")
          if koltuk in numaralar:
              liste=+koltuk
              if koltuk in liste:
                  print("bu numara alınmıştır başka bir numara seçiniz\n")
                  break
      def çarp(sayi1,sayi2):
          return sayi1*sayi2
      çarp(ogr,15)
      çarp(tam,20)
      def topla(sayi1,sayi2):
          return sayi1+sayi2
      topla(çarp(ogr,15),çarp(tam,20))
      fiyat=topla(çarp(ogr,15),çarp(tam,20))
      uye=int(input("üyeyse 1e değilse 0a basın\n"))
      if uye==0:
          print("fatura tutarı:\n",fiyat)
      elif uye==1:
          def indirim(sayi):
              return sayi-(sayi*5/100)
          indirim(fiyat)
          menuler = {"menu1": 20, "menu2": 25}
          print("aşağıda menüler ve fiyatları verilmiştir\n", menuler)
          menu=int(input("menü almak istemiyorsa 0a birinci menü için 1e ikinci menü için 2ye basın\n"))
          if menu==0:
              print("fatura tutarı:\n",indirim(fiyat))
          elif menu==1:
              yemek=int(20-(20*5/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
          elif menu==2:
              yemek=int(25-(25*4/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
      break
elif film==film3:
   while 1:
      ogr=int(input("öğrenci bileti sayısı:\n"))
      tam=int(input("tam bilet sayısı:\n"))
      kisi=tam+ogr
      topkisi=+kisi
      if topkisi>=20:
          print("bu salonda yer kalmamıştır\n")
      isim=input("ad soyad:\n")
      tel=input("telefon numarası:\n")
      for i in range (0,kisi):
          koltuk = input("koltuk numarası(1 ile 20 arasında):\n")
          if koltuk in numaralar:
              liste=+koltuk
              if koltuk in liste:
                  print("bu numara alınmıştır başka bir numara seçiniz\n")
                  break
      def çarp(sayi1,sayi2):
          return sayi1*sayi2
      çarp(ogr,15)
      çarp(tam,20)
      def topla(sayi1,sayi2):
          return sayi1+sayi2
      topla(çarp(ogr,15),çarp(tam,20))
      fiyat=topla(çarp(ogr,15),çarp(tam,20))
      uye=int(input("üyeyse 1e değilse 0a basın\n"))
      if uye==0:
          print("fatura tutarı:\n",fiyat)
      elif uye==1:
          def indirim(sayi):
              return sayi-(sayi*5/100)
          indirim(fiyat)
          menuler = {"menu1": 20, "menu2": 25}
          print("aşağıda menüler ve fiyatları verilmiştir\n", menuler)
          menu=int(input("menü almak istemiyorsa 0a birinci menü için 1e ikinci menü için 2ye basın\n"))
          if menu==0:
              print("fatura tutarı:\n",indirim(fiyat))
          elif menu==1:
              yemek=int(20-(20*5/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
          elif menu==2:
              yemek=int(25-(25*4/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
      break
elif film==film4:
   while 1:
      ogr=int(input("öğrenci bileti sayısı:\n"))
      tam=int(input("tam bilet sayısı:\n"))
      kisi=tam+ogr
      topkisi=+kisi
      if topkisi>=20:
          print("bu salonda yer kalmamıştır\n")
      isim=input("ad soyad:\n")
      tel=input("telefon numarası:\n")
      for i in range (0,kisi):
          koltuk = input("koltuk numarası(1 ile 20 arasında):\n")
          if koltuk in numaralar:
              liste=+koltuk
              if koltuk in liste:
                  print("bu numara alınmıştır başka bir numara seçiniz\n")
                  break
      def çarp(sayi1,sayi2):
          return sayi1*sayi2
      çarp(ogr,15)
      çarp(tam,20)
      def topla(sayi1,sayi2):
          return sayi1+sayi2
      topla(çarp(ogr,15),çarp(tam,20))
      fiyat=topla(çarp(ogr,15),çarp(tam,20))
      uye=int(input("üyeyse 1e değilse 0a basın\n"))
      if uye==0:
          print("fatura tutarı:\n",fiyat)
      elif uye==1:
          def indirim(sayi):
              return sayi-(sayi*5/100)
          indirim(fiyat)
          menuler = {"menu1": 20, "menu2": 25}
          print("aşağıda menüler ve fiyatları verilmiştir\n", menuler)
          menu=int(input("menü almak istemiyorsa 0a birinci menü için 1e ikinci menü için 2ye basın\n"))
          if menu==0:
              print("fatura tutarı:\n",indirim(fiyat))
          elif menu==1:
              yemek=int(20-(20*5/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
          elif menu==2:
              yemek=int(25-(25*4/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
      break
elif film==film5:
   while 1:
      ogr=int(input("öğrenci bileti sayısı:\n"))
      tam=int(input("tam bilet sayısı:\n"))
      kisi=tam+ogr
      topkisi=+kisi
      if topkisi>=20:
          print("bu salonda yer kalmamıştır\n")
      isim=input("ad soyad:\n")
      tel=input("telefon numarası:\n")
      for i in range (0,kisi):
          koltuk = input("koltuk numarası(1 ile 20 arasında):\n")
          if koltuk in numaralar:
              liste=+koltuk
              if koltuk in liste:
                  print("bu numara alınmıştır başka bir numara seçiniz\n")
                  break
      def çarp(sayi1,sayi2):
          return sayi1*sayi2
      çarp(ogr,15)
      çarp(tam,20)
      def topla(sayi1,sayi2):
          return sayi1+sayi2
      topla(çarp(ogr,15),çarp(tam,20))
      fiyat=topla(çarp(ogr,15),çarp(tam,20))
      uye=int(input("üyeyse 1e değilse 0a basın\n"))
      if uye==0:
          tutar=fiyat
          print("fatura tutarı:\n",tutar)
      elif uye==1:
          def indirim(sayi):
              return sayi-(sayi*5/100)
          indirim(fiyat)
          menuler = {"menu1": 20, "menu2": 25}
          print("aşağıda menüler ve fiyatları verilmiştir\n", menuler)
          menu=int(input("menü almak istemiyorsa 0a birinci menü için 1e ikinci menü için 2ye basın\n"))
          if menu==0:
              tutar=indirim(fiyat)
              print("fatura tutarı:\n",tutar)
          elif menu==1:
              yemek=int(20-(20*5/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
          elif menu==2:
              yemek=int(25-(25*4/100))
              tutar=yemek+indirim(fiyat)
              print("fatura tutarı:\n",tutar)
      break
import os
print(os.getcwd())
fis=open("fatura.txt","w")
fis.write("tarih:",tarih,"\n")
fis.write("fişi kesen:",çalışan.ad,çalışan.soyad,"\n")
fis.write("film:",film,"\n")
fis.write("ad-soyad:",isim,"\n")
fis.write("fatura tutarınız:",tutar,"\n")
fis.close()







