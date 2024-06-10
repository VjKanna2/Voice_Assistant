#importing packages
import sys
import webbrowser
import pyautogui
import speech_recognition as sr
import os
import webbrowser as wb
import datetime
import wikipedia
import pyttsx3
import time
import random
import ctypes
import distutils

ctypes.windll.kernel32.SetConsoleTitleW("Virtual Assistant")
os.system('cls')

#engines
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 0.8)

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def wish(text):
    engine.say(text)
    engine.runAndWait()

#greet user
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        wish('Good Morning BOSS, How can I help you?')
    elif hour >= 12 and hour < 16:
        wish('Good Afternoon BOSS, How can I help you?')
    elif hour >= 16 and hour < 19:
        wish('Good Evening BOSS, How can I help you?')
    else:
        wish('Hello BOSS, How can I help you?')

#input
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        r.energy_threshold = 800
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.2
        try:
            text1 = r.recognize_google(audio)
            text = text1.lower()
            print('You: ' + text)
        except:
            return ""
        return text

def sleep():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        r.energy_threshold = 500
        try:
            text1 = r.recognize_google(audio)
            text = text1.lower()
            print('You: ' + text)
        except:
            return "none"
        return text

#logic
text = ''
question = ''
type_sentence = ''
running = True
time.sleep(5)
wishme()

#random responses
def varied_response(responses):
    response = random.choice(responses)
    speak(response)

#query processing
while running:
    text = takecommand()
    question = text
    query4 = ''
    query3 = ''
    query1 = ''
    query5 = ''
    query2 = ''
    page1 = ''
    page2 = ''
    wakeup_txt = ''

    #HOW ARE YOU :)
    if 'good evening' in text or 'good morning' in text or 'good afternoon' in text:
        speak('How may I help you sir?')
    elif 'hey' in text or 'hai' in text or 'hello' in text:
        speak(text+'Sir, How are you?')
    elif "i am fine what about you" in text or "i am fine thank you what about you" in text or "yeah i am doing good what about you" in text or "i am fine and you" in text:
        speak("Yeah I'm Good. How can I help you?")
    elif 'how are you' in text:
        varied_response(["I'm Good, And You", "I'm great, how about you?"])
    elif "i am fine" in text or "i am doing good" in text or "i am doing great" in text or "yeah good" in text or "yeah fine" in text:
        speak("Great, How can I help you?")
    elif 'hey friday' in text or 'hai friday' in text or 'friday' in text:
        speak("Yes Sir, How Can I help you?")

    #ABOUT FRIDAY *
    elif 'your name' in text or 'what is your name' in text:
        varied_response(['My name is FRIDAY!', "I'm friday"])
    elif 'who created you' in text or 'who invented you' in text:
        varied_response(['Vijay', "By Vijay", "I was created by Vijay"])
    elif 'introduce yourself' in text or 'who are you' in text or'tell me something about yourself' in text or 'tell me about yourself'in text:
        speak("I am Friday. I'm the personal assistant of Vijay. Also I'm Still in development state")
    elif 'tell me something about vijay' in text or 'tell something about vijay' in text or 'who is vijay'in text or 'tell me about vijay' in text:
        speak('Vijay, a graduate from S R M University. he was created me as a project for a subject in his 7th semester')
    elif 'thank you' in text or 'thanks' in text:
        speak('You are welcome! enything else sir?')
    
    #services
    elif 'search' in text and 'in wikipedia' in text or 'search about' in text and 'in wikipedia' in text or 'wikipedia' in text:
        query1 = text.replace('wikipedia', '')
        query3 = query1.replace('about', '')
        query4 = query3.replace('in', '')
        query5 = query4.replace('for', '')
        query2 = query5.replace('search', '')
        query6 = query2
        speak('do you want me to narrate or open webpage sir?')
        answer = takecommand()
        if 'narrate' in answer or 'yes' in answer or 'yeah' in answer:
            results = wikipedia.summary(query6, sentences=1, auto_suggest=False)
            speak('according to wikipedia ' + results)
        elif 'no' in answer or 'website' in answer or 'webpage' in answer:
            page1 = wikipedia.page(query2, auto_suggest=False)
            print(page1)
            page2 = page1.url
            print(page2)
            speak('redirecting to webpage')
            webbrowser.get().open_new_tab(page2)
            print(page2)
    elif 'search' in text and 'in google' in text:
        query1 = text.replace('in google', '')
        query2 = query1.replace('search', '')
        speak('searching ' + query2 + ' in google')
        wb.get().open_new_tab('www.google.com/search?gx&q=' + query2)
    elif 'search' in text and 'in youtube' in text or 'play' in text and 'in youtube' in text:
        query1 = text.replace('in youtube', '')
        query2 = query1.replace('search for', '')
        speak('searching ' + query2 + ' in youtube')
        wb.get().open_new_tab('https://www.youtube.com/results?search_query=' + query2)
    elif 'search' in text:
        abc1 = text.replace('search', '')
        abc2 = abc1.replace('about', '')
        abc3 = abc2.replace('for', '')
        speak('do you want me to search in google, wikipedia or youtube sir?')
        answer3 = takecommand()
        if 'google' in answer3:
            speak('searching for ' + abc3 + ' in google')
            wb.get().open_new_tab('www.google.com/search?gx&q=' + abc3)

        elif 'wikipedia' in answer3:
            speak('do you want me to narrate or open webpage sir?')
            answer2 = takecommand()
            if 'narrate' in answer2 or 'direct' in answer2:
                results = wikipedia.summary(abc3, sentences=1, auto_suggest=False)
                speak('according to wikipedia ' + results)
            elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                page1 = wikipedia.page(abc3, auto_suggest=False)
                print(page1)
                page2 = page1.url
                print(page2)
                speak('redirecting to webpage')
                webbrowser.get().open_new_tab(page2)
                print(page2)
        elif 'youtube' in answer3:
            speak('searching for ' + abc3 + 'in youtube')
            wb.get().open_new_tab('https://www.youtube.com/results?search_query=' + abc3)

    elif text == '':
        speak('sorry sir. can you say that again?')

    elif 'roll a dice' in text or 'spin a dice' in text:
        r = random.randint(1, 6)
        dice = str(r)
        speak('you got ' + dice)
    
    elif text == 'quit' or text == 'ok bye' or text == 'exit' or text == 'end' or text == 'bye' :
        speak('Bye sir. Have A Great Time')
        running = False
        sys.exit()

    #opening and closing
    elif 'open instagram' in text:
        speak('ok. opening instagram')
        wb.get().open_new_tab('https://instagram.com')
    elif 'open youtube' in text:
        speak('ok. opening youtube')
        wb.get().open_new_tab('https://www.youtube.com')
    elif 'open facebook' in text:
        speak('ok. opening facebook')
        wb.get().open_new_tab('https://www.facebook.com')
    elif text == 'sing a song' or text == 'sing me a song' or 'sing a song' in text:
        speak(
            'I am not a good singer but I hope you will like this. Naa Ready than varava, Anna naa erangi varava, thel koduku singatha seendathappa, evan thaduthun en route maarathappa.')
    elif 'open chrome' in text or 'open google chrome' in text:
        speak('ok. opening google chrome')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk')
    elif 'yes' in text:
        speak('how can I help you sir?')
    elif 'open spotify' in text:
        speak('ok. opening spotify ')
        os.system('spotify')
    elif 'shut down the computer' in text or 'shutdown the computer' in text or 'shot down the computer' in text or "shut down my PC" in text or "turn of my PC" in text or "turn of my computer" in text:
        speak('ok shutting down the computer')
        os.system('shutdown /s /f')
        running = False
        sys.exit()
    elif 'close' in text and 'chrome' in text or text == 'close google chrome' or 'close google chrome' in text:
        speak('ok. closing google chrome')
        os.system('TASKKILL /F /IM chrome.exe')
    elif 'open access' in text or 'open axis' in text or 'open excess' in text:
        speak('ok. opening access')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Access.lnk')
    elif 'open photoshop' in text:
        speak('ok. opening adobe photoshop 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Photoshop 2021.lnk')
    elif 'open telegram' in text:
        speak('ok. opening telegram')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Telegram Desktop.lnk')
    elif 'open whatsapp' in text:
        speak('ok. opening whatsapp')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Whatsapp.lnk')
    elif 'open media encoder' in text:
        speak('ok. opening Adobe media encoder 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Media Encoder 2021.lnk')
    elif 'open premiere pro' in text:
        speak('ok. opening adobe premiere pro 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Premiere Pro 2021.lnk')
    elif 'open bluestacks' in text:
        speak('Ok. opening bluestacks 5')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/BlueStacks 5.lnk')
    elif 'open excel' in text:
        speak('Ok. opening Excel')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel.lnk')
    elif 'open free download manager' in text:
        speak('ok. opening free download manager')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Free Download Manager.lnk')
    elif 'open edge' in text:
        speak('ok. opening edge')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Edge.lnk')
    elif 'open screen recorder' in text or 'open recorder' in text:
        speak('ok. opening obs studio')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OBS Studio (64bit).lnk')
    elif 'open one drive' in text:
        speak('ok. opening one drive')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneDrive for Business.lnk')
    elif 'open one note' in text:
        speak('ok. opening one note')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk')
    elif 'open outlook' in text:
        speak('ok. opening outlook')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook.lnk')
    elif 'open powerpoint' in text:
        speak('ok. opening powerpoint')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PowerPoint.lnk')
    elif 'open publisher' in text:
        speak('ok. opening publisher')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Publisher.lnk')
    elif 'open skype' in text:
        speak('ok. opening skype')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Skype for Business.lnk')
    elif 'open visual studio installer' in text:
        speak('ok. opening visual studio installer')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Visual Studio Installer.lnk')
    elif 'open word' in text:
        speak('ok. opening word')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk')
        speak('do you want me to type sir?')
        typin = takecommand()
        if 'yes' in typin:
            pyautogui.press('enter')
            speak('sir you can start. say stop typing if I have to stop')
            while not 'stop typing' in type_sentence:
                type_sentence = takecommand()
                if type_sentence != 'stop typing' and type_sentence != 'press enter':
                    pyautogui.write(type_sentence + '. ')
                elif type_sentence == 'press enter':
                    pyautogui.press('enter')
            speak('stopped typing')
        elif 'no' in typin:
            speak('ok sir')
    elif 'open pycharm' in text:
        speak('ok. opening pycharm')
        os.startfile(
            'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrains/PyCharm Community Edition 2021.1.3.lnk')
    elif 'stop typing' in text:
        speak('sir I already stopped typing')
    elif 'time' in text:
        h = datetime.datetime.now().strftime("%H,%M,%S")
        speak(f"sir, the time is{h}")
    elif 'open zoom' in text:
        speak('ok. opening zoom')
        os.startfile('C:/Users/nbhel/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom/Zoom.lnk')
    elif 'close access' in text or 'close axis' in text or 'close excess' in text:
        speak('ok. closing access')
        os.system('TASKKILL /F /IM MSACCESS.exe')
    elif 'close after effects' in text:
        speak('ok. closing adobe after effects 2021')
        os.system('TASKKILL /F /IM AfterFX.exe')
    elif 'close illustrator' in text:
        speak('ok. closing adobe illustrator 2021')
        os.system('TASKKILL /F /IM AIRobin.exe')
    elif 'close spotify' in text:
        speak('ok. closing spotify')
        os.system('TASKKILL /F /IM Spotify.exe')
    elif 'close photoshop' in text:
        speak('ok. closing adobe photoshop 2021')
        os.system('TASKKILL /F /IM Photoshop.exe')
    elif 'close pycharm' in text or 'close python' in text:
        speak('ok. closing pycharm')
        os.system('TASKKILL /F /IM pycharm64.exe')
    elif 'close bluestacks' in text:
        speak('ok. closing bluestacks')
        os.system('TASKKILL /F /IM HD-Player.exe')
    elif 'close excel' in text:
        speak('ok. closing excel')
        os.system('TASKKILL /F /IM EXCEL.EXE')
    elif 'close youtube' in text:
        speak('ok. closing youtube')
        pyautogui.hotkey('ctrl', 'w')
    elif 'close facebook' in text:
        speak('ok. closing facebook')
        pyautogui.hotkey('ctrl', 'w')
    elif 'close task manager' in text:
        speak('ok. closing task manager')
        os.system('TASKKILL /F /IM Taskmgr.exe')
    elif 'close free download manager' in text:
        speak('ok. closing free download manager')
        os.system('TASKKILL /F /IM fdm.exe')
    elif 'close edge' in text:
        speak('ok. closing microsoft edge')
        os.system('TASKKILL /F /IM msedge.exe')
    elif 'close recorder' in text:
        speak('ok. closing obs studio')
        os.system('TASKKILL /F /IM obs64.exe')
    elif 'close powerpoint' in text:
        speak('ok. closing powerpoint')
        os.system('TASKKILL /F /IM POWERPNT.EXE')
    elif 'close word' in text:
        speak('ok. closing word')
        os.system('TASKKILL /F /IM winword.exe')
    elif 'repeat' in text:
        speak('ok sir. say stop repeating if i have to stop')
        repeating = ''
        while repeating != 'stop repeating':
            repeating = takecommand()
            if repeating != 'stop repeating':
                speak(repeating)
            elif repeating == 'stop repeating':
                speak('ok sir. repeating stopped.')
    elif 'sleep' in text:
        speak('ok sir goodnight')
        sl_cr = ''
        while not 'wake up' in sl_cr:
            sl_cr = sleep()
            if sl_cr == 'quit':
                speak('bye bye sir. have a great day')
        speak('hello again sir')
    elif 'show' in text and 'mirror' in text or 'open camera' in text:
        speak('ok. opening camera')
        os.system('start microsoft.windows.camera:')
    elif 'close' in text and 'camera' in text:
        speak('ok. closing camera')
        pyautogui.hotkey('alt', 'f4')
    elif 'search' in text and 'in youtube' in text:
        search_text1 = text.replace('search', '')
        search_text2 = search_text1.replace('in youtube', '')
        speak('searching for ' + search_text2 + ' in youtube')
        webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' + search_text2)
    elif 'play' in text and 'music' in text or 'playlist' in text:
        speak('ok sir enjoy your music')
        os.system('spotify.exe')
        time.sleep(1)
        pyautogui.click(button='left')
        pyautogui.press('space')
        pyautogui.hotkey('alt', 'f4')
        while not 'wake up' in wakeup_txt:
            wakeup_txt = sleep()
            if wakeup_txt == 'quit':
                speak('bye bye sir. have a great day')
                running = False
                sys.exit()
            elif 'pause' in wakeup_txt or 'play' in wakeup_txt:
                os.system('spotify')
                time.sleep(1)
                pyautogui.press('space')
                pyautogui.hotkey('alt', 'f4')
            elif 'close spotify' in wakeup_txt:
                os.system('TASKKILL /F /IM Spotify.exe')
        speak('hello again sir')
    elif 'open wikipedia' in text:
        speak('ok. opening wikipedia')
        webbrowser.get().open_new_tab('https://www.wikipedia.org')
    else:
        speak('sorry sir that is not assigned. do you want to search for ' + text + '?')
        confirmation = takecommand()
        if 'yes' in confirmation:
            speak('do you want me to search in google, wikipedia or youtube sir?')
            answer4 = takecommand()
            if 'google' in answer4:
                speak('searching for ' + text + ' in google')
                wb.get().open_new_tab('www.google.com/search?gx&q=' + text)

            elif 'wikipedia' in answer4:
                speak('do you want me to narrate or open webpage sir?')
                answer2 = takecommand()
                if 'narrate' in answer2 or 'direct' in answer2:
                    results = wikipedia.summary(text, sentences=1, auto_suggest=False)
                    speak('according to wikipedia ' + results)
                elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                    page1 = wikipedia.page(text, auto_suggest=False)
                    print(page1)
                    page2 = page1.url
                    print(page2)
                    speak('redirecting to webpage')
                    webbrowser.get().open_new_tab(page2)
                    print(page2)
            elif 'youtube' in answer4:
                speak('searching for ' + text + 'in youtube')
                wb.get().open_new_tab('https://www.youtube.com/results?search_query=' + text)
        else:
            speak('ok. anything else sir?')
        