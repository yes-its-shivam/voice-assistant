import os
import speech_recognition as sr
import webbrowser
import smtplib
import wikipedia
import pyttsx3
import datetime
import wolframalpha  

HUMANNAME = "SHIVAM"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("initializing EDITH.........." )

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<16:
        speak("you should eat and sleep sir")
    elif hour>=16 and hour<19:
        speak("good evening sir")
    else:
        speak("...good evening....sir")
    speak("i am your personal voice assistant , how may i help you? sir ")

def commandMeSir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        speak("listening...")
        audio = r.listen(source)

    try:
        print("understanding...")
        speak("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("sir please say that again..")
        speak("say please say that again")
    return query





wishMe()

while True:
    query = commandMeSir().lower()
    if 'wikipedia' in query.lower():
        speak('searching wikipedia for you sir')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)


    elif 'open youtube' in query.lower():
        speak("opening youtube")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        speak("opening google")
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open gmail' in query.lower():
        speak("opening gmail")
        url = "gmail.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open instagram' in query.lower():
        speak("opening instagram")
        url = "instagram.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open faceook' in query.lower():
        speak("opening facebook")
        url = "facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open twitter' in query.lower():
        speak("opening twitter")
        url = "twitter.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open stackoverflow' in query.lower():
        speak("opening stackoverflow")
        url = "stackoverflow.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")

    elif 'play music' in query or "play song" in query:
        speak("Here you go with music")
        music_dir = "C:\\Users\\admin\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[0]))

    elif 'do you know your name' in query or 'what is your name ' in query or 'your name please' in query or 'tell me your name' in query or 'tell me your name now assitant' in query or  'tell me your name now' in query:
        speak("yes sir my name is EDITH")

    elif 'tell me about yourself assistant' in query or 'brief me about urself' in query or 'tell me a little about yourself' in query or 'what do you know about yourself' in query:
        speak("yes mam")
        speak("my self EDITH , i am an A.I. voice assistant created by SHIVAM JINDAL. I can do a lot of tasks like sending emails or opening different websites like youtube , google , instagram etc., also i can play songs for you if you want,all you need is to command me mam")

    elif 'open wikipedia' in query.lower():
        speak("opening wikipedia")
        url = "stackoverflow.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open whatsapp web' in query.lower():
        speak("opening whatsapp web")
        url = "web.whatsapp.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open amazon' in query.lower():
        speak("opening amazon")
        url = "amazon.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open prime video' in query.lower():
        speak("opening amazon prime video")
        url = "primevideo.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open netflix' in query.lower():
        speak("opening netflix")
        url = "netflix.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open myntra' in query.lower():
        speak("opening myntra")
        url = "myntra.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open flipkart' in query.lower():
        speak("opening flipkart")
        url = "flipkart.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open amazon' in query.lower():
        speak("opening amazon")
        url = "amazon.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open hotstar' in query.lower():
        speak("opening hotstar")
        url = "hotstar.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open airtel extreme' in query.lower():
        speak("opening airtel extreme")
        url = "airtelxstream.in"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open photoshop" in query.lower():
        speak("opening photoshop")
        photoshopPath = 'C:\\Program Files\Adobe\\Adobe Photoshop 2020\\photoshop.exe'
        os.startfile(photoshopPath)

    elif "open paint" in query.lower():
        speak("opening paint")
        paintPath = 'C:\\Windows\\system32\\mspaint.exe'
        os.startfile(paintPath)

    elif "open videos" in query.lower():
        speak("opening system videos")
        videosPath = 'C:\\Users\\admin\\Videos'
        os.startfile(videosPath)

    elif "open pictures" in query.lower():
        speak("opening system pictures")
        picturesPath = 'C:\\Users\\admin\\Pictures'
        os.startfile(picturesPath)

    elif "open downloads" in query.lower():
        speak("opening system system")
        downloadsPath = 'C:\\Users\\admin\\Downloadss'
        os.startfile(downloadsPathsPath)

    elif "open 3D objects" in query.lower():
        speak("opening 3D objects")
        dobjectsPath = 'C:\\Users\\admin\\3D Objects'
        os.startfile(dobjectsPath)

    elif "open desktop" in query.lower():
        speak("opening desktop")
        desktopPath = 'C:\\Users\\admin\\Desktop'
        os.startfile(desktopPath)

    # elif "change name" in query.lower():
    #     speak("what would you like to call me sir")
    #     assistantname = commandMeSir()
    #     speak(f"okay sir now my name is {assistantname}")

    elif "who created you " in query or "what is the name of your creator" in query or "who made you" in query or "whom were you created by" in query:
        speak("his name is SHIVAM JINDAL")

    elif 'joke' in query.lower():
        speak(pyjokes.get_joke())

    elif "calculate" in query.lower():

        app_id = "82QEQX-YVXT6KE5EG"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif 'search' in query or 'play' in query:

        query = query.replace("search", "")
        query = query.replace("play", "")
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(query)

    elif "open ms power point presentation" in query.lower():
        speak("opening power point")
        msppt = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe'
        os.startfile(msppt)

    elif "open ms word" in query.lower():
        speak("opening word")
        wordpath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe'
        os.startfile(wordpath)

    elif "open ms excel" in query.lower():
        speak("opening excel")
        excelpath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.exe'
        os.startfile(excelpath)







