print("""********************************
İşlem Listesi

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
****************************************
""")
while True:
    islem = input("İşlem seçiniz.(Çıkış için 'q' ya basabilirsiniz.): ")
    if islem == 'q':
        print("Çıkıyor...")
        exit("çıkış")
        
    elif islem == "1":
        print("**Toplama İşlemi**")
        sayi1 = int(input("1. Sayıyı Giriniz: "))
        sayi2 = int(input("2. sayıyı Giriniz: "))
        print("{} + {} = {}".format (sayi1, sayi2, sayi1+sayi2))
    
    elif islem == "2":
        print("**Çıkarma İşlemi**")
        sayi1 = float (input("1.Sayıyı Giriniz: "))
        sayi2 = float(input("2.Sayıyı Giriniz: "))
        print("{} - {} = {}".format(sayi1, sayi2,sayi1-sayi2))
        
    elif islem == "3":
        print("**Çarpma İşlami")
        sayi1 = float(input("1.Sayıyı Giriniz: "))
        sayi2 = float(input("2.Sayıyı Giriniz: "))
        print("{}  *   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))
        
    elif islem == "4":
        print("**Bölme İşlemi**")
        try:
            sayi1 = int(input("1.Sayıyı Giriniz: "))
            sayi2 = int(input("2.Sayıyı Giriniz: "))
            print("{}  /   {}    =  {:.2f}".format(sayi1, sayi2, sayi1/sayi2))
        
        except ZeroDivisionError:
            print("yılar 0'a bölünemez!")
        
        except ValueError:
            print("Lütfen sadece sayı giriniz!")
            
    else:
        print("Geçersiz İşlem...")