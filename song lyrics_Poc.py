while True:
    song_name = int(input('enter you choice: '))
   

    if song_name == 1:
        f= open('1st song.txt','r')
        print(f.read())
        f.close()
    elif song_name == 2:
        f= open('2nd song.txt','r')
        print(f.read())
        f.close()
    elif song_name == 3:
        f= open('3rd song.txt','r')
        print(f.read())
        f.close()
    elif song_name == 4:
        f= open('4th song.txt','r')
        print(f.read())
        f.close()

     
    else:
        print('Invalid option\make correct choice')
    x=input('press * to choose again')

    if x!="*":
        break
