#Kullanıcı isimlerinin girilmesini iste.Kullanıcılardan sırayla zar atmalarını iste.
#İki kere zar attır.Kullanıcı enter'a basınca atsın ve atılan zarın sayısını yazdır.
#İşlem bitince zarların toplamına göre kazananın adını yazdır.
import random 
oyuncu1=input("Oyuncu 1 ismi: ")
oyuncu2=input("Oyuncu 2 ismi: ")

print(f"\n--- Zar Oyunu Başlıyor: {oyuncu1} vs {oyuncu2} ---\n")
input(f"{oyuncu1},ilk zarını atmak için Enter'a bas...")
zar1_oyuncu1=random.randint(1,6)
input(f"{oyuncu1},ikinci zarını atmak için Enter'a bas...\n")
zar2_oyuncu1=random.randint(1,6)

print("*********************************************\n")
input(f"{oyuncu2},ilk zarını atmak için Enter'a bas...")
zar1_oyuncu2=random.randint(1,6)
input(f"{oyuncu2},ikinci zarını atmak için Enter'a bas...\n")
zar2_oyuncu2=random.randint(1,6)

toplam_oyuncu1=zar1_oyuncu1+zar2_oyuncu2
print(f"-> {oyuncu1} toplam puanı: {toplam_oyuncu1}")

toplam_oyuncu2=zar1_oyuncu2+zar2_oyuncu2
print(f"->{oyuncu2} toplam puanı:{toplam_oyuncu2}\n")

print("== SONUCLAR ==")

if(toplam_oyuncu1<toplam_oyuncu2):
  print("Oyuncu 2 kazandı!")
elif(toplam_oyuncu1>toplam_oyuncu2):
  print("Oyuncu 1 kazandı!")
else:
  print("Kazanan yok...")
