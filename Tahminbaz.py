import time
import random
import pygame 
import sys
from colorama import Fore, Style

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\EmirVAR\\Desktop\\‏\\Python\\Şarkı\\FonMuzigi.mp3")
sound_file1="C:\\Users\\EmirVAR\\Desktop\\‏\\Python\\Şarkı\\Cevap.mp3"
sound_file2="C:\\Users\\EmirVAR\\Desktop\\‏\\Python\\Şarkı\\Error.mp3"
sound_file3="C:\\Users\\EmirVAR\\Desktop\\‏\\Python\\Şarkı\\Kapanis.mp3"
sound1=pygame.mixer.Sound(sound_file1)
sound2=pygame.mixer.Sound(sound_file2)
sound3=pygame.mixer.Sound(sound_file3)
pygame.mixer.music.set_volume(0.1)
sound1.set_volume(1)
sound2.set_volume(1)
sound3.set_volume(0.7)

pygame.mixer.music.play(loops=-1)


print(Fore.YELLOW+"\nTahminbaz'a hoşgeldin")
time.sleep(0.5)
print(Fore.YELLOW+"Yükleniyor..."+Style.RESET_ALL)
time.sleep(1)

cevap=[Fore.BLUE+"Evet, kesinlikle.",
    "Kesinlikle öyle.",
    "Şüphesiz.",
    "Evet.",
    "Şimdi böyle gözüküyor.",
    "Evet, elbette.",
    "Olumlu.",
    "İşaretler eveti gösteriyor.",
    "Çok olasılıklı.",
    "Bulutlu, tekrar deneyin.",
    "Şimdi tahmin edemem.",
    "Şimdi söylemesem daha iyi.",
    "Konsantre ol ve tekrar sor.",
    "Bunu yapma ihtimali düşük.",
    "Hayır.",
    "Cevabım hayır.",
    "Kaynaklarım hayır diyor.",
    "Çok şüpheli.",
    "Kesinlikle.",
    "Şanslı bir şekilde evet.",
    "Kesin.",
    "Beklentiler olumlu.",
    "Durumlar iyiye gidiyor.",
    "Olumlu sonuçlar bekleniyor.",
    "Kesinlikle doğru.",
    "Tüm işaretler eveti gösteriyor.",
    "Evet, ama zaman alabilir."+Style.RESET_ALL]




def soru():
    input(Fore.MAGENTA+"Sormak istediğin evet-hayır sorusunu sor: "+Style.RESET_ALL)
    print(Fore.BLUE+"Tahminbaz düşünyor..."+Style.RESET_ALL)
    time.sleep(1.5)    
    cevap1=random.choice(cevap)
    print(cevap1+Style.RESET_ALL)
    sound1.play()

while True:
    a=input(Fore.MAGENTA+"\nSoru sormak ister misin(Evet/Hayır): "+Style.RESET_ALL).lower()
    time.sleep(1)
    if a=="evet":
        soru()

    elif a=="hayır":
        print("Zaman geçirdiğin için teşekkürler"+Style.RESET_ALL)
        sound3.play()
        time.sleep(2)
        sys.exit()

    else:
        print(Fore.RED+"Lütfen Evet yada Hayır kullan!!!!!!!!"+Style.RESET_ALL)
        sound2.play()






