import os
import tkinter as tk
from tkinter import messagebox
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

def gorev_ekle():
    gorev = entry_gorev.get()
    if gorev.strip():
        gorevler = gorevleri_yukle()
        gorevler.append([gorev, 'X'])
        gorevleri_kaydet(gorevler)
        entry_gorev.delete(0, tk.END)
        gorevleri_guncelle()
        messagebox.showinfo("Başarılı", f"'{gorev}' eklendi!")
    else:
        messagebox.showwarning("Uyarı", "Boş görev eklenemez!")

def gorevleri_guncelle():
    listbox_gorevler.delete(0, tk.END)
    gorevler = gorevleri_yukle()
    for i, (gorev, durum) in enumerate(gorevler, 1):
        listbox_gorevler.insert(tk.END, f"{i}. [{durum}] {gorev}")

def gorev_tamamla():
    secili_index = listbox_gorevler.curselection()
    if secili_index:
        index = secili_index[0]
        gorevler = gorevleri_yukle()
        gorevler[index][1] = '✓'
        gorevleri_kaydet(gorevler)
        gorevleri_guncelle()
        messagebox.showinfo("Başarılı", f"'{gorevler[index][0]}' tamamlandı!")
    else:
        messagebox.showwarning("Uyarı", "Tamamlanacak bir görev seçin!")

def gorev_sil():
    secili_index = listbox_gorevler.curselection()
    if secili_index:
        index = secili_index[0]
        gorevler = gorevleri_yukle()
        silinen = gorevler.pop(index)
        gorevleri_kaydet(gorevler)
        gorevleri_guncelle()
        messagebox.showinfo("Başarılı", f"'{silinen[0]}' silindi!")
    else:
        messagebox.showwarning("Uyarı", "Silinecek bir görev seçin!")

def cikis():
    root.destroy()

# ui - tkinter
root = tk.Tk()
root.title("Yapılacaklar Listesi")
root.geometry("650x750")
root.configure(bg="#F8E8EE")

label_baslik = tk.Label(root, text=" Yapılacaklar Listesi ", font=("Helvetica", 18, "bold"), bg="#F8E8EE", fg="#9B59B6")
label_baslik.pack(pady=20)

frame_gorev = tk.Frame(root, bg="#F8E8EE")
frame_gorev.pack(pady=10)

entry_gorev = tk.Entry(frame_gorev, width=40, font=("Helvetica", 12), bg="#FDE2E4", fg="#6C3483", borderwidth=2)
entry_gorev.pack(side=tk.LEFT, padx=5)

btn_ekle = tk.Button(frame_gorev, text="Ekle", command=gorev_ekle, font=("Helvetica", 12), bg="#D291BC", fg="white", borderwidth=2)
btn_ekle.pack(side=tk.RIGHT)

listbox_gorevler = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#FDE2E4", fg="#6C3483", selectbackground="#D291BC", selectforeground="white", borderwidth=2)
listbox_gorevler.pack(pady=10)

btn_tamamla = tk.Button(root, text="Görevi Tamamla", command=gorev_tamamla, font=("Helvetica", 12), bg="#9B59B6", fg="white", borderwidth=2)
btn_tamamla.pack(pady=5)

btn_sil = tk.Button(root, text="Görevi Sil", command=gorev_sil, font=("Helvetica", 12), bg="#D291BC", fg="white", borderwidth=2)
btn_sil.pack(pady=5)

btn_cikis = tk.Button(root, text="Çıkış", command=cikis, font=("Helvetica", 12), bg="#6C3483", fg="white", borderwidth=2)
btn_cikis.pack(pady=10)

gorevleri_guncelle()
root.mainloop()
