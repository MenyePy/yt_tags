import pyperclip
import random
import time

file = 'tags.txt'
general = ['gameplay', 'fun', 'top', 'funny', 'best moments', 'meme', 'impossible']
gameadj = ['gameplay ', 'new ', 'latest version ', 'updated ', 'funny ']

def convert(var):
    var2 = var.split(' ')
    return var2

def extraGameTags(game):
    ta1 = game + gameadj[0]
    ta2 = gameadj[1] + game
    ta3 = gameadj[2] + game
    ta4 = game + gameadj[3]
    ta5 = gameadj[4] + game
    ta = [ta1, ta2, ta3, ta4, ta5]
    return ta

def write(file, message):
    f = open(file, 'w')
    f.write(message)
    f.close

def append(file, message):
    f = open(file, 'a')
    f.write(message)
    f.close
    

def intro():
    print('Youtube tag generator 0.0.1 ALPHA')
    print('Gaming videos ONLY, more in future updates')
    print('Loading...')
    time.sleep(1)

def getInfo():
    global title, game, game_flags, other
    title = input('Please enter the video title')
    if title:
        game = input('What game are you playing?')
        game_flags = input('Please enter additional game info e.g online, abbreviations, e.t.c')
        other = input('Please enter any other things you need. If unavailable, skip.')
        makeTags(title, game, game_flags, other)
    else:
        print('Title required.')
        exit

def makeTags(title, game, game_flags, other):
    if title:
        global general
        tc = convert(title)
        gc = convert(game)
        g_fc = convert(game_flags)
        oc = convert(other)
        time.sleep(1)
        etc = extraGameTags(game)
        converted = tc + gc + g_fc + oc + etc + general
        print (converted)
        print ('Wiriting tags to ' + file)
        for i in converted:
            i2 = i + ', '
            append(file, i2)
        time.sleep(1)
        print('Done!')
        print('Copy from file  tags.txt and delete the file for future tags')
        time.sleep(1)
        return converted
    
    else:
        print('Error maketags: no title detected')

def main():
    intro()
    getInfo()

main()
    
