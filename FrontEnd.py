from tkinter import *
import tkinter as tk
from typing import List 
from tkinter import messagebox 

ogr_bilgileri = {"23122860048" : " 192803050 , Ahmet Can ÖZTÜRKMEN , Gaziantep , 2001 , Yazılım Mühendisliği "}


ogr_data= open('ogr_sifre.txt', 'r')
ogr_parola = ogr_data.read()
ogr_parola = ogr_parola.replace("/n","")
ogr_data.close()

ogr_parola = ogr_parola.split()



sorumlu_data= open('sorumlu_sifre.txt', 'r')
sorumlu_parola = sorumlu_data.read()
sorumlu_parola = sorumlu_parola.replace("/n","")
sorumlu_data.close()

sorumlu_parola = sorumlu_parola.split()


admin_data= open('admin_sifre.txt', 'r')
admin_parola = admin_data.read()
admin_parola = admin_parola.replace("/n","")
admin_data.close()

admin_parola = admin_parola.split()




def ogr_islem():
    ogr_pencere = Tk()
 
    ogr_pencere.title("Öğrenci İşlemleri")
    ogr_pencere.geometry("600x600")

    uygulama2 = Frame(ogr_pencere)
    uygulama2.grid()
    var = messagebox.showinfo("Uyarı" , "Öğrenci İşlemerine Hoşgeldiniz Yapmak İstediğiniz işlemi Seçiniz")
    button5 = Button(uygulama2, text = " Test çöz  " , width=40,height=5, command=exit)
    button5.grid(padx=165, pady=45)

    button6 = Button(uygulama2, text = " Öğrenci Bilgileri  " , width=40,height=5, command=bilgi_sorgu)
    button6.grid(padx=165, pady=45)

    button7 = Button(uygulama2, text = " Öğrenci Sınav Raporu   " , width=40,height=5, command=exit)
    button7.grid(padx=165, pady=45)
    ogr_pencere.mainloop()

def sorumlu_islem():
    sorumlu_pencere = Tk()
 
    sorumlu_pencere.title("Sınav Sorumlusu İşlemleri")
    sorumlu_pencere.geometry("600x600")

    uygulama2 = Frame(sorumlu_pencere)
    uygulama2.grid()
    var = messagebox.showinfo("Uyarı" , "Sınav Sorumlusu İşlemerine Hoşgeldiniz Yapmak İstediğiniz işlemi Seçiniz")
    button5 = Button(uygulama2, text = " Test Hazırla  " , width=40,height=5, command=exit)
    button5.grid(padx=165, pady=45)

    button6 = Button(uygulama2, text = " Sorumlu Bilgileri  " , width=40,height=5, command=exit)
    button6.grid(padx=165, pady=45)
    button7 = Button(uygulama2, text = " Öğrenci Bilgileri Sorgula   " , width=40,height=5, command=exit)
    button7.grid(padx=165, pady=45)

    sorumlu_pencere.mainloop()

def admin_islem():
    admin_pencere = Tk()
 
    admin_pencere.title("admin İşlemleri")
    admin_pencere.geometry("600x600")

    uygulama2 = Frame(admin_pencere)
    uygulama2.grid()
    var = messagebox.showinfo("Uyarı" , "Admin İşlemerine Hoşgeldiniz Yapmak İstediğiniz işlemi Seçiniz")
    button5 = Button(uygulama2, text = " Sınav Sorumlusu Ekle  " , width=40,height=5, command=exit)
    button5.grid(padx=165, pady=45)

    button6 = Button(uygulama2, text = " Sınav Sorumlusu Çıkar  " , width=40,height=5, command=exit)
    button6.grid(padx=165, pady=45)

    button7 = Button(uygulama2, text = " Öğrenci Bilgileri Sorgula   " , width=40,height=5, command=exit)
    button7.grid(padx=165, pady=45)

    admin_pencere.mainloop()

def ögrenci_giris():
    giris_ekranı = Tk()

    giris_ekranı.title("Öğrenci Arayüzü ")
    giris_ekranı.geometry("400x300")

    uygulama2 = Frame(giris_ekranı)
    uygulama2.grid()

    L1 = Label(uygulama2 , text = "Tcnizi girin ")
    L1.grid(padx=140 , pady=10)

    E1 = Entry(uygulama2 , bd=2)
    E1.grid(padx=140 , pady=3)
    
    def deger_al():        
        TC=E1.get()       
        print(TC)
        for i in range(len(ogr_parola)):
            if (TC == ogr_parola[i]):
                print("Başarılı")
                ogr_islem()
                break
                
                
                
            else:
                pass        
        
        
      
           
    button4 = Button(uygulama2, text = " Onayla " , width=15,height=2, command=deger_al)
    button4.grid()
      
    giris_ekranı.mainloop()
    
def sorumlu_giris():
    giris_ekranı = Tk()

    giris_ekranı.title("Sorumlu Arayüzü ")
    giris_ekranı.geometry("400x300")

    uygulama2 = Frame(giris_ekranı)
    uygulama2.grid()

    L1 = Label(uygulama2 , text = "Tcnizi girin ")
    L1.grid(padx=140 , pady=10)

    E1 = Entry(uygulama2 , bd=2)
    E1.grid(padx=140 , pady=3)
    
    def deger_al():        
        TC=E1.get()       
        print(TC)
        for i in range(len(sorumlu_parola)):
            if (TC == sorumlu_parola[i]):
                print("Başarılı")
                sorumlu_islem()
                break
                
                
                
            else:
                pass        
        
        
      
           
    button4 = Button(uygulama2, text = " Onayla " , width=15,height=2, command=deger_al)
    button4.grid()
      
    giris_ekranı.mainloop()

def admin_giris():
    giris_ekranı = Tk()

    giris_ekranı.title("Admin Arayüzü ")
    giris_ekranı.geometry("400x300")

    uygulama2 = Frame(giris_ekranı)
    uygulama2.grid()

    L1 = Label(uygulama2 , text = "Tcnizi girin ")
    L1.grid(padx=140 , pady=10)

    E1 = Entry(uygulama2 , bd=2)
    E1.grid(padx=140 , pady=3)
    
    def deger_al():        
        TC=E1.get()       
        print(TC)
        for i in range(len(admin_parola)):
            if (TC == admin_parola[i]):
                print("Başarılı")
                admin_islem()
                break
                
                
                
            else:
                pass        
        
        
      
           
    button4 = Button(uygulama2, text = " Onayla " , width=15,height=2, command=deger_al)
    button4.grid()
      
    giris_ekranı.mainloop()

def ana_menu():
    pencere = Tk()
 
    pencere.title("Ana Menü ")
    pencere.geometry("600x600")
 
    uygulama = Frame(pencere)
    uygulama.grid()


 

    button1 = Button(uygulama, text = " Öğrenci İşlemleri  " , width=40,height=5, command=ögrenci_giris)
    button1.grid(padx=165, pady=45)

    button2 = Button(uygulama, text = " Sınav Sorumlusu İşlemleri  " , width=40,height=5, command=sorumlu_giris)
    button2.grid(padx=165, pady=45)

    button3 = Button(uygulama, text = " Admin İşlemleri  " , width=40,height=5, command=admin_giris)
    button3.grid(padx=165, pady=45)
    pencere.mainloop()  


def bilgi_sorgu():
    giris_ekranı = Tk()

    giris_ekranı.title("Öğrenci Bilgi  Arayüzü ")
    giris_ekranı.geometry("400x300")

    uygulama2 = Frame(giris_ekranı)
    uygulama2.grid()

    L1 = Label(uygulama2 , text = "Tcnizi girin ")
    L1.grid(padx=140 , pady=10)

    E1 = Entry(uygulama2 , bd=2)
    E1.grid(padx=140 , pady=3)
    
    def bilgi_sorgu():        
        TC=E1.get()       
        print(TC)
        for i in range(len(ogr_bilgileri)):
            if (TC == ogr_bilgileri[i]):
                print(ogr_bilgileri[i])                
                break
                
                
                
            else:
                pass

    button4 = Button(uygulama2, text = " Onayla " , width=15,height=2, command=bilgi_sorgu)
    button4.grid()
      
    giris_ekranı.mainloop()            



ana_menu()





