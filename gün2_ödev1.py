
isim = input("Lütfen isminizi giriniz: ")
soy_isim = input("Lütfen soy isminizi giriniz: ")

liste = []



# Aldığı isim soy isim ile listeye öğrenci ekleyen
def append_liste(isim,soy_isim):
    liste.append(isim+" "+soy_isim)

append_liste(isim,soy_isim)
print(liste)



# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def remove_liste(isim,soy_isim):
    liste.remove(isim+" "+soy_isim)

remove_liste(isim,soy_isim)
print(liste)



# Listeye birden fazla öğrenci eklemeyi mümkün kılan
def add_more():
    while True:
        isim = input("Lütfen isminizi giriniz (ekleme tamamsa eğer 0 a basın!!!): ")
        
        if isim == "0":
            break
        
        soy_isim = input("Lütfen soy isminizi giriniz: ")
        append_liste(isim,soy_isim)

add_more()
print(liste)



# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

isim = input("Lütfen isminizi giriniz: ")
soy_isim = input("Lütfen soy isminizi giriniz: ")
liste.append(isim+" "+soy_isim)

def student_num(isim,soy_isim):
    for j in range(len(liste)):
        if liste[j] == isim+" "+soy_isim:
            return j

num = student_num(isim,soy_isim)
print(f"Öğrenci numarası: {num+1}") # indisler 0 dan başladığı için +1 ekledim.



# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def remove_moore():
    for i in liste:
        print(liste)
        
        isim = input("Silmek istediğiniz kişinin ismini giriniz(çıkış yapmak için 0 giriniz!!!): ")
        if isim == "0":
            break
        soy_isim = input("Silmek istediğiniz kişinin soy ismini giriniz: ")
        
        liste.remove(isim+" "+soy_isim)

remove_moore()
print(liste)