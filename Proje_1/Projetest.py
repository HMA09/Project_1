def hmmenu():
    print("╔═════════════════════╗")
    print("║ HESAP MAKİNESİ      ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-Çarpma           ║")
    print("║  4-Bölme            ║")
    print("║  5-Üs Alma          ║")
    print("║  6-Dörtgen Alanı    ║")
    print("║  7-Dörtgen Çevresi  ║")
    print("║                     ║")
    print("║    Seçimini yap     ║")
    print("╚═════════════════════╝")

    s=input("Seçiminizi Yapınız:")
    
    if s == "1":
        print("TOPLAMA")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Toplam:", s1+s2)
    if s == "2":
        print("ÇIKARMA")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Fark:", s1-s2)
    if s == "3":
        print("ÇARPMA")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Çarpım:", s1*s2)
    if s == "4":
        print("BÖLME")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Bölüm:", s1/s2)
    if s == "5":
        print("ÜS ALMA")
        s1 = int(input("Üs Alınacak Sayıyı Giriniz:"))
        s2 = int(input("Üs Sayıyı Giriniz:"))
        print("Sonuç:", s1**s2)
    if s == "6":
        print("DÖRTGEN ALANI")
        s1 = int(input("Kısa Kenarını Giriniz:"))
        s2 = int(input("Uzun Kenarını Giriniz:"))
        print("Alan:", s1*s2)
    if s == "7":
        print("DÖRTGEN ÇEVRESİ")
        s1 = int(input("Kısa Kenarını Giriniz:"))
        s2 = int(input("Uzun Kenarını Giriniz:"))
        print("Çevresi:", (s1+s2)*2)
        
def sklmenu():

    print("╔═════════════════════╗")
    print("║ ŞEKİL ÇİZDİRME      ║")
    print("║                     ║")
    print("║  1-Sağa Ok          ║")
    print("║  2-Sola Ok          ║")
    print("║  3-Kare             ║")
    print("║  4-Dikdörtgen       ║")
    print("║  5-Üçgen            ║")
    print("║  6-Geometrik Şekil  ║")
    print("║  7-Ortaya Karışık   ║")
    print("║                     ║")
    print("║    Seçimini yap     ║")
    print("╚═════════════════════╝")

    s=input("Seçiminizi Yapınız:")


    if s == "1":
        print("Sağa Ok")
        import turtle
        turtle.forward(100)
        input()
    if s == "2":
        print("Sola Ok")
        import turtle
        turtle.right(180)
        turtle.forward(100)
        input()
    if s == "3":
        print("Kare")
        import turtle
        for a in range (4):
            turtle.forward(100)
            turtle.right(90)
        input()
    if s == "4":
        print("Dikdörtgen")
        import turtle
        for a in range (2):
            turtle.forward(150)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
        input()
    if s == "5":
        print("Üçgen")
        import turtle
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        input()
    if s == "6":
        print("Geometrik Şekil")
        import turtle
        turtle.speed(10)
        for a in range (24):
            for a in range (4):
                turtle.forward(100)
                turtle.right(90)
            turtle.right(15)
        input()
    if s == "7":
        print("Square Spiral")
        import turtle
        turtle.speed(10)
        t = turtle.Pen()
        for x in range(100):
            t.forward(x)
            t.left(91)
        input()

def oyunmenu():

    print("╔════════════════════════╗")
    print("║       OYUNLAR          ║")
    print("║1-KAPLUMBAĞA YARIŞI     ║")
    print("║2-DİĞER                 ║")
    print("║3-                      ║")
    print("║    Seçimini Yap        ║")
    print("╚════════════════════════╝")

    s=input("Seçiminizi Yapınız:")

    if s == "1":

        import turtle
        import random

        t = turtle.Turtle()
        t.up()
        t.goto(-100, 100)
        t.down()
        t.speed(0)

        # yarış pisti
        for i in range(15):
            t.write(i)
            t.right(90)
            t.forward(200)
            t.left(180)
            t.forward(200)
            t.right(90)
            t.forward(20)

        # kablumbağaları oluşturma
        birinci = turtle.Turtle()
        birinci.shape("turtle")
        birinci.color("red")
        birinci.up()
        birinci.goto(-120, 70)
        birinci.down()

        ikinci = turtle.Turtle()
        ikinci.shape("turtle")
        ikinci.color("blue")
        ikinci.up()
        ikinci.goto(-120, 40)
        ikinci.down()

        ucuncu = turtle.Turtle()
        ucuncu.shape("turtle")
        ucuncu.color("yellow")
        ucuncu.up()
        ucuncu.goto(-120, 10)
        ucuncu.down()

        # taraftarlar
        x = random.randint(1, 10)
        for i in range(x):
            taraftar = turtle.Turtle()
            k = random.randint(0, 255) / 255.0  # Renk değerlerini normalize et
            y = random.randint(0, 255) / 255.0
            m = random.randint(0, 255) / 255.0
            taraftar.shape("turtle")
            taraftar.color(k, y, m)
            taraftar.up()
            taraftar.goto(-90 + 25 * i, -120)
            taraftar.down()
            taraftar.left(90)

        x_birinci = 0
        x_ikinci = 0
        x_ucuncu = 0

        kazanan = input("Hangi kablumbağa kazanacak:")
        yazi = turtle.Turtle()
        yazi.up()
        yazi.goto(-120, 120)
        yazi.write(kazanan + " kablumbağanın kazanacağını düşünüyorsunuz ")

        while True:
            if x_birinci > 305 or x_ikinci > 305 or x_ucuncu > 305:
                break

            birinci_adim = random.randint(1, 5)
            x_birinci = x_birinci + birinci_adim
            birinci.forward(birinci_adim)

            ikinci_adim = random.randint(1, 5)
            x_ikinci = x_ikinci + ikinci_adim
            ikinci.forward(ikinci_adim)

            ucuncu_adim = random.randint(1, 5)
            x_ucuncu = x_ucuncu + ucuncu_adim
            ucuncu.forward(ucuncu_adim)

        if x_birinci > 305:
            t.write("Kırmızı Kazandı!")
        elif x_ikinci > 305:
            t.write("Mavi Kazandı!")
        elif x_ucuncu > 305:
            t.write("Sarı Kazandı!")

        input()

    if s == "2":
        print("Henüz hazır değil")


print("╔════════════════════════╗")
print("║   PYTHON ÇALIŞMALARI   ║")
print("║1-HESAP MAKİNESİ        ║")
print("║2-OYUNLAR               ║")
print("║3-ŞEKİL ÇİZDİRME        ║")
print("║4-TAKVİM                ║")
print("║5-RİTMİK SAYMA          ║")
print("║6-NOT HESAPLAMA         ║")
print("║7-ÇARPIM TABLOSU        ║")
print("║8-BMI HESAPLAMA         ║")
print("║9-DÖVÜZ UYGULAMASI      ║")
print("║10-SICAKLIK ÇEVİRME     ║")
print("║11-ÇIKIŞ (e)            ║")
print("║    Seçimini Yap        ║")
print("╚════════════════════════╝")

secim= input("Seçiminizi Yapınız:")
if secim== "1" : hmmenu()
if secim== "2" : oyunmenu()
if secim== "3" : sklmenu()
if secim== "4" : print("Henüz Hazır değil")
if secim== "5" : print("Henüz Hazır değil")
if secim== "6" : print("Henüz Hazır değil")
if secim== "7" : print("Henüz Hazır değil")
if secim== "8" : print("Henüz Hazır değil")
if secim== "9" : print("Henüz Hazır değil")
if secim== "10" : print("Henüz Hazır değil")
if secim== "11" : print("Henüz Hazır değil")
