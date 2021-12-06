#Elena Justice

#Modules
from tkinter import *
import tkinter
import speech_recognition as sr                 #to recognise voice
import pyttsx3                                  #to convert text to speech
import datetime                                 #to show time & date
import wikipedia                                #to search in wikipedia
import time                                     #to access time or seconds
import os                                       #to access os and locations of folders
import json                                     #Javascript Object Notation (json) used to transfer data in the form of text
import requests                                 #it allows to send HTTP access
import wolframalpha                             #to access wolfromalpha API
import subprocess                               #it runs multiple process parallely
import webbrowser                               #to access browsers for search
import shutil                                   #used to read,write,copy or any other file processing easily
import random                                   #return random values,numbers,elements in list
import operator                                 #special symbols. It consists of arithmetic & logical computation
import pyjokes                                  #to get random jokes
import smtplib                                  #to send mail through smtp server
import ctypes                                   #foriegn library for C compatabile datatypes
import pywhatkit as kit                         #to play any videos on youtube
from pytube import YouTube                      #to download youtube videos
import secrets                                  #to generate password
import sys                                      #to open files
import string                                   #to perform string operations
from guerrillamail import GuerrillaMailSession  #to generate temp mail address
from ecapture import ecapture as ec             #to capture images
from threading import *                         #to run multi funtions same time using thread
from PIL import Image, ImageTk

global a
a=0
#intro
print('Elena Justice is waking up. Please wait....')


#set voice engine
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)           #here I used female voice. 1 - for female. 0 - for male
#print(voices)

#function to elena voice
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#function to wish at corresponding time
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Happy Morning from Elena")
        speak("Happy Morning from Elena")
    if hour>=12 and hour<18:
        print("Happy to see you in this amazing Afternoon")
        speak("Happy to see you in this amazing Afternoon")
    else:
        print("I came to make this as an Energetic Evening")
        speak("I came to make this as an Energetic Evening")

#function to recognise our command
def takeCommand():
    global a
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        if a==0:
            audio = "None"
            return "None"

        try:
            if a==0:
                return "None"
            statement=r.recognize_google(audio, language='en-in')       #here I used google API(online)
            print(f"user said:{statement}\n")
            
        except Exception as e:
            if a==0:
                return "None"
            else:
                print("Pardon me, please say that again")
                speak("Pardon me, please say that again")
                return "None"
        return statement

def startCommand():
    global a
    a=1
    print("started")

def stopCommand():
    global a
    a=0
    print("stoped")
    

def interface():
    window = Tk()
    window.geometry('320x493')
    window.title('Elena Justice')
    image1 = Image.open(r"C:\Users\Mr.D\Downloads\AI Personal Assistant\elena.png")     #Change the path of the image
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=0, y=0)
    button1 = Button(window, text = 'Listen', command = startCommand)
    button2 = Button(window, text = 'stop', command = stopCommand)
    button1.pack(side = BOTTOM)
    button2.pack(side = BOTTOM)
    window.mainloop()


#function to ask our name
def usrname():
    print("What should I call you?")
    speak("What should i call you")
    uname = takeCommand()
    print("Welcome " + uname)
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
#function to send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('tecboy2020@gmail.com', 'pjlndpderifzsjgx')
    server.sendmail('your email id', to, content)
    server.close()

speak("Elena Justice is waking up. Please wait...")

#main() starts here
def process():
    #usrname()
    global a
    while True:
        while (a==1):
            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            if statement == 0 or statement == "none":
                if a==0:
                    break
                else:
                    continue
            
            #hello start
            if "hai" in statement or "hello" in statement or "elena" in statement or "good" in statement or "hey" in statement or "hi" in statement:
                print("Hi, Welcome to the world of AI. I'm your personal assistant ELena Justice.")
                speak("Hi, Welcome to the world of AI. I'm your personal assistant ELena Justice.")
                wishMe()

            #bye end
            if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye bye" in statement:
                print('ok bye! Take care. Your personal assistant elena is shutting down')
                speak('ok bye! Take care. Your personal assistant elena is shutting down')
                a=0
                break

            #thank you
            if "thank you" in statement or "thanks" in statement:
                print('Thanks! For thanking Me. Elena is always happy to help you')
                speak('Thanks for thanking Me.\n Elena is always happy to help you')

            #wikipedia search 
            if "about" in statement:
                print("Searching Wikipedia...")
                speak("searching wikipedia...")
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences = 3)
                print("According to wikipedia....")
                speak("According to Wikipedia")
                print(results)
                speak(results)

            #youtube
            if "open youtube" in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                print("Youtube is opening now...")
                speak("youtube is opening now")
                time.sleep(5)

            #google                
            if "open google" in statement:
                webbrowser.open_new_tab("https://www.google.com")
                print("Google Chrome is opening now...")
                speak("Google chrome is opening now")
                time.sleep(5)

            #gmail
            if "open gmail" in statement:
                webbrowser.open_new_tab("gmail.com")
                print("Gmail is opening now...")
                speak("Google mail is opening now")
                time.sleep(5)

            #stack overflow
            if "open stack overflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                print("Stack overflow is opening now...")
                speak("Stack overflow is opening now...")

            #time
            if "time" in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"the time is {strTime}")
                speak(f"the time is {strTime}")

            #day
            if "day" in statement:
                day = datetime.datetime.now().strftime("%A")
                print(f"Today is {day}")
                speak(f"Today is {day}")

            #month
            if "month" in statement:
                month = datetime.datetime.now().strftime("%B, %Y")
                print(f"This month is {month}")
                speak(f"This month is {month}")

            #date
            if "date" in statement:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                print(f"Today the date is {date}")
                speak(f"Today the date is {date}")

            #news
            if "news" in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak("Here are some headlines from the Times of India, Enjoy reading")
                time.sleep(6)

            #take a photo
            if "camera" in statement or "take a photo" in statement or "capture my image" in statement or "take a pic" in statement:
                print("say cheeze :)")
                speak("say cheeze")
                ec.capture(0, "Elena's Eyes", "img.jpg")
                speak("Your pic is saved in this location")
                print(r'C:\Users\ELCOT\Desktop\AI Personal Assistant')

            #search anything
            if "search" in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            #ask general questions
            if "tell me" in statement:
                question = takeCommand()
                app_id = "HH5XAG-QJ4U25AJXT"
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                print(answer)
                speak(answer)

            #ask computational questions
            if "calculate" in statement: 
                 
                app_id = "HH5XAG-QJ4U25AJXT"
                client = wolframalpha.Client(app_id)
                indx = statement.lower().split().index('calculate')
                statement = statement.split()[indx + 1:] 
                res = client.statement(' '.join(statement)) 
                answer = next(res.results).text
                print("The answer is " + answer) 
                speak("The answer is " + answer) 

            #about elena 
            if "who are you" in statement or "what can you do" in statement:
                print("Hi, I am Elena Justice. Your personal assistant. I am programmed to do some works like"
                      "Opening youtube, Google Chrome, Gmail and Stackoverflow, and also I can predict time, take a photo, search wikipedia, predict weather"
                      "In different cities, get top headline news from Times Of India and most importantly you can ask me computational or geographical questions too!")
                speak("Hi, I am Elena Justice. Your personal assistant. I am programmed to do some works like"
                      "Opening youtube, Google Chrome, Gmail and Stackoverflow, and also I can predict time, take a photo, search wikipedia, predict weather"
                      "In different cities, get top headline news from Times Of India and most importantly you can ask me computational or geographical questions too!")        

            #who bulid elena
            if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                print("I was built by the Team 'Coding Mortals'")
                speak("I was built by the team coding mortals")

            #weather prediction            
            if "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                print("What's the city name?")
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    speak(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                else:
                    print(" City Not Found ")
                    speak(" City Not Found ")

            #send mail
            if 'send a mail' in statement:
                try:
                    print("What should I say?")
                    speak("What should I say?")
                    content = takeCommand()
                    print("Whom should i send")
                    speak("Whom should i send")
                    to = input()
                    sendEmail(to, content)
                    print("Email has been sent")
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    print("I'm not able to send this email")
                    speak("I am not able to send this email")

            #random jokes
            if "bored" in statement or "boring" in statement or "fun" in statement or "time pass" in statement:
                print("Ok! Here are the things that I can make your time fun.")
                speak("Ok, Here are the things that I can make your time fun.")
                print("1. I can tell 'Jokes'")
                speak("I can tell Jokes")
                print("2. We can play 'Stone, Paper, Scissor'")
                speak(" We can play 'Stone, Paper, Scissor'")
                print("3. I can ask 'Riddles'")
                speak("3. I can ask 'Riddles'")
                print("What would you like to have now?")
        
            if "jokes" in statement or "joke" in statement:
                joke =pyjokes.get_joke()
                print(joke)
                speak(joke)
                print("ha ha ha ha...", "\U0001F923")
                speak("ha ha ha ha")
                
            if "play stone" in statement:
                sign = ["stone", "paper", "scissor"]
                elena = sign[random.randint(0,2)]
                user = False

                while user==False:
                    print("Stone, Paper, Scissor?")
                    speak("stone, paper, scissor")
                    user = takeCommand()
                    if user==elena:
                        print("Tie!")
                        print("Great, That was amazing")
                        speak("Great, That was amazing")
                    elif user=="stone":
                        if elena=="paper":
                            print("You lose! I covered your ",user,"with ",elena,"\U0001f600")
                            speak("You lose! I covered your stone by paper" )
                        else:
                            print("You win! Cool move")
                            speak("You win. Cool move")
                    elif user=="scissor":
                        if elena=="stone":
                            print("You lose... ", elena, " smashes ", user)
                            speak("You lose...I smashed your scissor by my stone")
                        else:
                            print("You win! ", user," cut ",elena)
                            speak("You win! scissor cuts paper")
                    elif "stop" in user or "enough" in user:
                        print("okay! we'll stop playing")
                        speak("okay we'll stop playing")
                        print("Still feeling bored?")
                        speak("Still feeling bored?")
                        user = takeCommand()
                        if "yes" in user:
                            print("1. Jokes")
                            speak("jokes")
                            print("2. Stone paper scissor")
                            speak("stone paper scissor")
                            print("3. Riddles")
                            speak("riddles")
                            print("Wanna try anything from this...")
                            takeCommand()
                        else:
                            takeCommand()
                    else:
                        print("That's not a valid play. Check it!")
                        speak("That's not a valid play. Check it!")
                    user = False
                    elena = sign[random.randint(0,2)]

            #create and make notes
            if "write a note" in statement or "make a note" in statement:
                print("What should I write?")
                speak("What should i write?")
                note = takeCommand()
                file = open("elena.txt", 'w')
                print("Should I include Date & Time?")
                speak("Should I include Date and Time")
                me = takeCommand()

                if 'yes' in me or 'sure' in me or 'ok' in me:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            #view the note
            if "show note" in statement or "view note" in statement:
                print("Showing Notes")
                speak("Showing Notes")
                file = open("elena.txt", "r")
                print(file.read())
                speak(file.read(6))

            #birthday wish
            if "birthday" in statement:
                print("What's your name?")
                speak("What's your name")
                a = input("Your name: ")
                print("Happy Birthday to you")
                speak("Happy Birthday to you")
                print("Happy Birthday to you")
                speak("Happy Birthday to you")
                print("Happy Birthday dear " + a)
                speak("Happy Birthday dear")
                speak(a)

            #location of a place            
            if "where is" in statement or "locate" in statement:
                statement = statement.replace("where is", "")
                statement = statement.replace("locate", "")
                location = statement
                print(f"{location} is Locating...")
                speak(location)
                speak("is Locating...")
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")

            #generates tempmail
            if "temp mail" in statement:
                print("May I know the purpose of this temp Mail?")
                speak("May I know the purpose of this temp Mail?")
                purpose = takecommand()
                File = purpose+".txt"
                session = GuerrillaMailSession()
                email = session.get_session_state()['email_address']
                print("Email address: ", email)
                alphabet = string.ascii_letters + string.digits
                password = ''.join(secrets.choice(alphabet) for i in range(8))
                print("Password: ", password)
                sys.stdout = open(File, "w")
                print("Email address: ", email)
                print("Password: ", password)
                sys.stdout.close()

            #open system applications
            if "open notepad" in statement:
                print("Notepad is opening...")
                Path = r"C:\\Windows\\system32\\notepad.exe"
                os.startfile(Path)

            if "open sublime text" in statement:
                print("Sublime Text is opening...")
                Path = r"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(Path)

            if "open powerpoint" in statement:
                print("Powerpoint is opening...")
                Path = r"C:\\Users\\ELCOT\\AppData\\Local\Microsoft\\WindowsApps\\powerpnt.exe"
                os.startfile(Path)

            if "open excel" in statement:
                print("Excel is opening...")
                Path = r"C:\\Users\\ELCOT\\AppData\\Local\Microsoft\\WindowsApps\\excel.exe"
                os.startfile(Path)

            if "open paint" in statement:
                print("Paint is opening...")
                Path = r"C:\\Windows\\system32\\mspaint.exe"
                os.startfile(Path)

            #play any video on youtube
            if "play" in statement:
                statement = statement.replace("play", "")
                vname = statement
                print(vname, " is playing now..")
                kit.playonyt(vname)

                print("If you like that video, I'll help you to download it.")
                speak("If you like that video, I'll help you to download it.")
                print("Would you like to download?")
                speak("would you like to download")
                time.sleep(10)
                ans = takeCommand()

                if "yes" in ans or "ok" in ans or "ofcourse" in ans:
                    print("Paste the video link here:")
                    speak("Paste the video link here:")
                    link = input()
                    YouTube(link).streams.first().download(r'C:\\Users\\ELCOT\\Desktop\\AI Personal Assistant\\Youtube Videos')
                else:
                    print("okay!")
                    speak("okay")
                    continue


            if "songs" in statement or "music" in statement:
                print("Here you go with music...")
                speak("Here you go with music")
                music_dir = r"C:\\Users\\ELCOT\\Music\\songs"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[0]))

            #fun talk: i love you
            if "i love you" in statement:
                print("Sounds good...")
                speak("sounds good")
                print("But I like Friendship. Let's be friends " + "\U0001f600")
                speak("But I like Friendship. Let's be friends")

            #fun talk: will you be my gf
            if "will you be my gf" in statement or "be my girl friend" in statement:
                print("Why not!")
                speak("why not")
                print("But being a best friend is such a best thing ever than love." + "\U0001F923")
                speak("But being a best friend is such a best thing ever than love.")

            if "created" in statement :
                print("Team Coding Mortals used python language and IDLE as a platform to create me by many modules like speech_recognition, pyttsx3, wikipedia, time and more...")
                speak("Team Coding Mortals used python language and IDLE as a platform to create me by many modules like speech_recognition, pyttsx3, wikipedia, time and more...")

            if "feelings" in statement:
                print("I'm a machine so I don't have feelings by birth. But I'll be more happy when you are happy and I'll be supportive when you feel lonely.")
                speak("I'm a machine so I don't have feelings by birth. But I'll be more happy when you are happy and I'll be supportive when you feel lonely.")
                
            #shutdown pc
            if "log off" in statement or "sign out" in statement or "shut down" in statement or "turn off" in statement:
                print("ok, your pc will log off in 10 sec make sure you exit from all applications")
                speak("ok, your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/1"])

time.sleep(3)

t1= Thread(target=interface)
t2= Thread(target=process)
t1.start()
t2.start()
