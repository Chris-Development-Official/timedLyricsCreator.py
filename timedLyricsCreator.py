import sys,os,inspect
import time
import vlc
import music_tag

thisdir = os.getcwd()

def formatTime(x):
    x = int(x)
    #milliseconds
    ms = x%1000
    x=x//1000
    #seconds
    s=x%60
    #minutes
    m=x//60
    result = '['+str(m).zfill(2)+':'+str(s).zfill(2)+'.'+str(ms).zfill(3)+']'
    return result

print("TimedLyricsCreator")
print("_____________________________")
print("")
print("Running in: " + thisdir)
print("")

count=1
for filename in os.listdir(thisdir):
    if filename.endswith(".mp3"):
        path = os.path.join(thisdir,filename)
        print(path)
        
        f = music_tag.load_file(path)
        lyrics = str(f['lyrics'])
        print("")
        print(str(count)+".")
        try:
            while 1:
                x = input("Start playing '" + filename + "'? y/n  ")
                if x=="y":
                    lyricsList = lyrics.split("\n")
                    newLyrics="[00:00.000]\n"
                    i=1
                    for i in range(4):
                        time.sleep(1)
                        if i==1:
                            print("Ready?")
                        elif i==2:
                            print("Set...")
                        elif i==3:
                            print("Go!")
                    
                    os.environ["VLC_VERBOSE"] = str("-1")
                    self.vlc_player = vlc.MediaPlayer("--verbose -1")
                    media_player = vlc.MediaPlayer()                      
                    media = vlc.Media(filename)
                    media_player.set_media(media)
                    media_player.play()

                    lineCount = 0
                    print("___________First Line:"+lyricsList[0])
                    while 1:
                        y=input()
                        if y=="":    
                            if str(media_player.get_state())=="State.Playing":
                                
                                try:
                                    c_time = formatTime(media_player.get_time())         
                                    lyricsList[lineCount] = c_time + lyricsList[lineCount]
                                    print(lyricsList[lineCount])

                                    try:
                                        print("___________Next Line:"+lyricsList[lineCount+1])
                                    except:                             
                                        print("___________Was Last Line.")
                                                     
                                    lineCount = lineCount+1
                                
                                except:
                                    print("Wait until song ends and then press 'Enter'...")
                                             
                            elif str(media_player.get_state()) =="State.Ended":
                                for line in lyricsList:
                                    newLyrics = newLyrics + line + "\n"
                                    
                                print("Lyrics")
                                print("")
                                print(newLyrics)
                                print("")
                                try:
                                    f['lyrics'] = newLyrics
                                    f.save()
                                    
                                    print("Injected lyrics succefully!")
                                except ValueError:
                                    print("paok" + str(ValueError))

                                raise "break"
                        elif y=="r":
                            media_player.stop()
                            print("Lyrics syncronization aborted by user.")
                            print("")
                            break
                elif x=="n":
                    #print("Dont play")
                    raise "break"
        except Exception as e:
            #print(e)
            pass
            
        count = count+1      
        
print("")
print("_______________________________")
print("Operation completed successfully")

while 1:
    input()

