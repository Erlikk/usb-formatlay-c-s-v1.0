import os
import sys
def diskleri_listele():
    os.system("df -h")

while True:
    print("***********************")
    print("Usb formatlayıcısı v1.0")
    print("***********************")
    print("Diskleri Listele = 1")
    print("Diski formatla   = 2")
    print("Çıkmak için = q")

    islem = input("İşlemi seçiniz:")

    if islem == "1":
        diskleri_listele()

    elif islem == "2":
        print("******************************")
        disk = input("Formatlamak istediğiniz diskin yolunu giriniz:")
        print("******************************")
        print("FAT  = 1              MSDOS = 2")
        print("NFTS = 3              BFS   = 4")
        format_bicimi = input("Format biçimini gir:")
        if format_bicimi == "1":
            x = "mkfs.fat " + disk
            xz = x + " -I"
            os.system(xz)
            print("İşlem bitti...")
        elif format_bicimi == "2":
            y = "mkfs.msdos " + disk
            yz = y + " -I"
            os.system(yz)
            print("işlem bitti...")

        elif format_bicimi == "3":
            z = "mkfs.nfts " + disk
            zz = z + " -I"
            os.system(zz)
            print("İşlem bitti...")

        elif format_bicimi == "4":
            a = "mkfs.bfs " + disk
            az = a + " -I"
            os.system(az)
            print("İşlem bitti")
        else:
            print("Böyle bir format biçimi bulunmamaktadır...")

    elif islem == "q":
        print("Çıkış yapıldı...")
        break

    else:
        print("yanlış işlem...")






