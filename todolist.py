import os
TODO_FILE = "todo_list.txt"

def gorevleri_yukle():

    if not os.path.exists(TODO_FILE):
        return[]
    
    with open(TODO_FILE,"r", encoding="utf-8") as file:
        return[satır.strip().split(" | ") for satır in file.readlines()]
    

def gorevleri_kaydet(gorevler):
    with open(TODO_FILE,"w", encoding="utf-8") as file:
        for gorev, durum in gorevler:    
            file.write(f"{gorev} | {durum}\n")


def gorev_ekle(gorev):
    gorevler=gorevleri_yukle()
    gorevler.append([gorev," -"]) 
    gorevleri_kaydet(gorevler)
    print(f"'{gorev}' eklendi ve kaydedildi!") 

def gorevleri_listele():
    gorevler=gorevleri_yukle()
    if not gorevler:
        print("Gorev listesi boş.")

    else:
        print("***Yapılacaklar Listesi:***")
        for i,(gorev,durum) in enumerate(gorevler,1):
            print(f"{i}.[{durum}] {gorev}")


def gorev_tamamla(index):
    gorevler=gorevleri_yukle()
    if 0< index <=len(gorevler):
        gorevler[index-1][1]="ok"
        gorevleri_kaydet(gorevler)
        print(f"+'{gorevler[index-1][0]}'tamamlandı!")
    else:
        print("Geçersiz görev numarası!")    


def gorev_sil(index):
    gorevler=gorevleri_yukle()
    if 0< index <=len(gorevler):
        silinen=gorevler.pop(index-1)
        gorevleri_kaydet(gorevler)
        print(f"'{silinen[0]}' silindi!")
    else:
        print("Geçersiz görev numarası!")



while True:
    print("***Yapılacaklar Listesi Uygulaması***")
    print("1 Görev Ekle")
    print("2 Görevleri Listele")  
    print("3 Görevi Tamamla")  
    print("4 Görev Sil")  
    print("5 Çıkış")

    seçim= input("Ne yapmak istiyorsunuz?")


    if seçim=="1":
        gorev=input("Eklemek istediğiniz görevi yazın:")
        gorev_ekle(gorev)
    elif seçim=="2":
        gorevleri_listele()
    elif seçim=="3":
        gorevleri_listele()
        index=int(input("Tamamlanan görev numarasını girin:"))
        gorev_tamamla(index)

    elif seçim=="4":
        gorevleri_listele()
        index=int(input("Silmek istediğiniz görev numarasını girin: "))
        gorev_sil(index)

    elif seçim=="5":
        print("Çıkış yapıldı.Görevleriniz kaydedildi!")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin...")
                                 






















