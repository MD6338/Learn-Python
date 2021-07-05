# this software will pronounce the things you will tyoe

import pyttsx3
friend = pyttsx3.init()
saying = " I am a pronouncing software that will pronounce everything Try --  @, #, $, %, ^, a, s, d, f , 1 , 2 ,   3  ,"
print(saying)
run = True


while run:

    Speech = input("Say Something     :   ")
    friend.say(Speech)
    friend.runAndWait()
    if (Speech == 'Stop' or run == 'stop'):
        run = False
