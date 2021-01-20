# Gn App , Music Runner , In Python language

from time import strftime, localtime
from os import system

t = input("Time : ")

print("App is running !\n")

while True:
    if strftime('%H : %M : %S', localtime()) == t:
        print(f"Wake up body ! it's {t} !")
        system('mpg123 ~/Gn/Music/*.mp3')
    else:
        pass
