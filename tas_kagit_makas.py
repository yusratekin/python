import random
Liste = ["Taş","Kağıt","Makas"]
pc = random.choice(Liste) #bilgisayarın liste içerinden rastgele seçimi
player = input('[Taş - Kağıt - Makas]') .capitalize()

print("Bilgisayar ",pc, "seçti")
print("Sen ",player, "seçtin")

if pc == player:
    print("Berabere")
if pc == "Kağıt" and player == "Taş":
    print("Kaybettin")
if pc == "Taş" and player == "Makas":
    print("Kaybettin")
if pc == "Makas" and player == "Kağıt":
    print("Kaybettin")
    

if pc == "Kağıt" and player == "Makas":
    print("Kazandın...")
if pc == "Taş" and player == "Kağıt":
    print("Kazandın...")
if pc == "Makas" and player == "Taş":
    print("Kazanadın....")
    
else:
    print("Liste dışı giriş yaptınız...!")
