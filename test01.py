import speech_recognition as sr
import pyttsx3
import requests
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes
import math
import random
import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk
import os,subprocess
import webbrowser
# subprocess.call("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
# url = 'https://pythonexamples.org'
# webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
# url='http://youtube.com/'
# webbrowser.get('chrome').open_new_tab(url)
# # webbrowser.open_new_tab(url)
# # subprocess.call(command)
command ="hello dear open commandprompt"

if ((('open cmd' in command) or ('open command prompt'  in command ) or ('open commandprompt'  in command) or ('run cmd' in command) or ('run command prompt'  in command) or ('run commandprompt'in command))):
        print("Yes working")
else:
    print("Error Occurs")
are_you_single=["No, I’m double.","Why? How many of me do you see?","Who told you to ask me that? The cops? The government?","I’m in a very romantic, committed relationship with alcohol.","Yes, I am single like Kraft American Cheese!","Yes. As you can see from my body frame and structure, I cannot be called double.","I don’t have an identical twin if that’s what you’re asking.","Why? Have you seen my doppelganger?","No, I have a twin brother/sister. That makes me double.","Well, prepare for trouble. And make it double!","Dude, I’m like...6. I’m calling the cops.","Are you a cop? Nope? Then stop with the interrogation!","Who sent you here? My enemies?","There’s a reason why I’m single. It’s called 'my face.'",
"Yes, and that’s because my friends never leave me alone.",
"If you want to apply as my boyfriend/girlfriend, send your cover letter and resume to my email address.",
"Let me get back to you after I cry in the corner.",
"No, I'm an album.",
"Actually, I’m a potato.",
"As single as a pringle.",
"Whoever cast a curse on my love life can chill now. I learned my lesson. I promise.",
"After I buried the body, you could say I’m single and ready to mingle now.",
"Hahahaha! What are you talking about? The trash goes out more than me, you know."]

with open("Contents/test.txt","r") as f1:
    data=f1.read().split("\n")
    # lines = open('file.txt').read().splitlines()
    # print(data)
for i in range(0,10):
    myline = random.choice(data)
    # print(myline)

url="https://en.wikipedia.org/wiki/"
data_dict={
    'item':'Sha Rukh Khan',
    "search":"submit"
}
resp=requests.post(url,data=data_dict)
# print(resp)
# print(resp.content)

lst=[3,5,6]
if (3 or 4) in lst:
    print("yes present")


"""
I am constantly torn between “I don’t need anyone in my life.” and “hey, can you please fall in love with me?”.","
I am a superhero, and superheroes don’t need relationships!","
Stranger danger!","
I’m mentally dating a bunch of attractive fictional characters.","
Have you not seen my husbando/waifu yet?","
Just so you know, I choose fries over guys.","
No, I’m dating an anime character.","
Ummm...well, I’m dating a hot celebrity and apparently, he/she doesn’t know that.","
Even darkness, my old friend, doesn’t want to be friends with me anymore.","
*cries and holds eye contact*","
Why? How much are going to pay me?","
I have someone but he’s/she’s from another nation. Yup, my imagiNATION!","
Aww...oh no, wait a minute! I have no one.","
Single? Me? Have you seen my 13 cats? Let me show them to you.","
No, no, and no. I’m in a relationship with food!","
No, my boyfriend/girlfriend standing right here. Can you not see him/her?","
The only relationship I can handle is one with my food.","
I have a loving and healthy relationship with pizza.","
If you want me to share my food, then I’m not sharing.","
*insert name of good-looking celebrity here* has yet to return my calls.","
funny-and-witty-replies-to-are-you-single","
Alexas_Fotos, CC0, via Pixabay","
Come closer and I’ll whisper it to you. *whispers in a soft, sensual voice* 'Wanna hook up later?'","
If you’re cute, I’ll think about it.","
Why? *raises hand in front of interrogator* Do you want to put a ring on it?","
Well, I’m going to stare at you until you marry me.","
Not anymore, now that you’re here.","
Not if you fall in love with me.","
If you just want to kiss me, then I’m all lips.","
I was. Until now. *wink*","
Come closer dear. I can’t hear you.","
Are you here to save me from my loneliness?","
Are you my prince charming?","
The other side of my bed is taken up by my phone, books, laptop, and TV remote control. No space for you, sorry.","
Let’s find out. *licks lips*","
Hold my hand and I’ll tell the answer.","
Please drop the formalities. Let’s get it on!","
I am, but I’m willing to be your double.","
You’ll know the answer once you touch my lips with your lips.","
Are you hitting on me? You really think you can get with this? Ha.","
Why? Do you want to get your hands on this hot merchandise?","
Let’s me show you the way to my heart.","
Say that again, but whisper it slowly to my ear instead.","
I am currently waiting for the perfect one. By any chance, are you the perfect one for me?","
Witty Comebacks to “Are You Single?”","
Let me spell it out for you dear, S-I-N-G-L-E!","
Philosophically speaking, aren’t we all single?","
No. As a matter of fact, I’m being screwed by the government every day.","
No, I’m taken...by time!","
Ahhh, you should ask my future self.","
I am single by person, infinite by intellect.","
I tried to clone myself once, but I failed miserably.","
Next question, please!","
No. I’m in a long-distance relationship with my boyfriend/girlfriend who lives in the future.","
My heart believes in quality, not quantity.","
I don’t fear commitment. I fear wasting my time.","
Not if you make me double.","
Well, I do need a sidekick right now. Would you like to sign up?","
It could be raining men yet I’d still be single.","
Sorry, I’m not hiring right now.","
Do you want to join the dark side?","
I get about as much attention as a white crayon.","
“Single” is not a status. It’s a word that represents an individual who’s strong enough to live and enjoy life without depending on other people.","
No, I am two.","
Nope, single is my cousin.","
Huh? Can’t you see my imaginary boyfriend/girlfriend?","
Let’s just say I hate people who are holding their hands in front of me.","
Yes. Unfortunately, I have not yet found anyone who matches my brilliance. I am just too beautiful and intelligent. It’s really tough, I know.","
Sorry, I’d like to keep my upcoming project a secret. Please speak to my publicist.","
I’ve committed myself to eventually dying alone. I have to start working towards that now, you know.","
Shhh! I’m focused on building my empire right now.","
I’m too hot to handle, baby.","
Oh yes, I am! As far as I’m concerned, I don’t remember cloning myself.","
If my pet dog counts, then I surely am not.","
funny-and-witty-replies-to-are-you-single","
Free-Photos, CC0, via Pixabay","
No, I’m leaving.","
We’re all going to die anyway, so why does it matter?","
Don’t ask.","
Say that one more time and I’m going to crush your heart with my own hands.","
Do I even have to explain it to you?","
Say that again, I dare you!","
I'm now in the process of unhearing what you just said.","
Yes, I’m quite allergic to bullsh*t.","
If you’re seeing two me, then you should get your eyes checked.","
Whatever! I’ll just date myself.","
My boyfriend/girlfriend is handsome/beautiful—looking all invisible and sh*t!","
I’m allergic to face people.","
I just met you. How am I supposed to know?","
Why are you acting like you don’t know?","
I can barely tolerate people as friends. How do you expect me to handle someone who’s more than just a friend?","
Are you blind?","
Back off!","
Two can play that game, you know.","
Let me show you the way out.","
Surprising Remarks to “Are You Single?”","
Sorry, I only like boys/girls that I have zero chance with.","
I feel like I’m waiting for something that is never going to happen.","
Yes, literally everyone who isn’t me hates me.","
To tell you the truth, a relationship doesn’t really fit my personal brand.","
Yes, and that’s because I don’t want to burst my happy, lazy bubble.","
Sorry, I’d rather live into old age with hundreds of cats by my side.","
I refuse to “settle.”","
Yes, but to be honest, I don't think so.","
Hmm...sounds like effort.","
Many people treat love as a game. But for me, I treat it is a precious gift for my one and only special person in the world.","
Are you flirting with me?","
You know nothing about the dark side of me.","
I’m not really interested in men right now. Or women. Or any person, really.","
You’re creeping me out!","
Yes, but a relationship would really cut into the time spend watching TV, lounging around, and drowning in misery.","
How about you ask yourself? Are you single?","
Yes, it is working.","
Yes, and only because you’re enjoying it.","
Do you know anyone who’s a 10? I’m a perfect 10!","
Yes, but have you seen my follower count on social media?","
Wait, is this you breaking up with me?","
I can’t get enough of myself. I don’t need another single.","
Ummm...I prefer doubles.","
I’m too tall and fabulous for anyone.","
Shout out to my imaginary boyfriend/girlfriend.","
No one is strong enough to handle ","

'''
listener =sr.Recognizer()
# for converting text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 120)
engine.setProperty('volume',1.0)

def talk(text):
    engine.say(text)
    # engine.say("K chha hajur khabar my speaking rate is ",str(rate))
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            talk("How may I assist you")
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command = command.lower()
            if 'maya' in command:
                command=command.replace('maya','')
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','') #removing play word from command
        talk("Playing Song")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+ time)
    elif 'who' in command:
        person = command.replace('who','')
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a boyfriend')
    elif 'are you single' in command:
        talk('Sorry I am in relationship with WIFI')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk("Please Say Clearly")
while True:
    run_alexa()

'''
"""