import pyttsx3 as py
import webbrowser
import speech_recognition as sr
import os
import datetime
import wikipedia
from bot import bott

r = sr.Recognizer()
engine = py.init('sapi5', debug = True)
# engine.setProperty('voice', voices[1].id) #Setting Female Voice
engine.setProperty('rate', 190) # Adjusting the rate of speech

def time_wish():
    hour = datetime.datetime.now().hour
    nickname = 'Sunny'

    if(hour >= 12 and hour < 18):
        speak(f'Good After noon {nickname}')
        

    elif(hour < 12 and hour >= 0):
        speak(f'Good Morning {nickname}')
        

    else:
        speak(f'Good Evening {nickname}')
        

def welcome(engine):
    time_wish()
    speak('I am Your Assistant, how can i help you')
    

def listen():
    welcome(engine)
    while(1):
        text_input = input("Ask a question: ")
        if ('tell me' or 'information' or 'inform')in text_input:
            '''-------------WIKIPEDIA--------------'''
            speak('Searching in Wikipedia')
            text_input = text_input.replace('wikipedia','')
            info = wikipedia.summary(text_input, sentences=3)
            speak('According To Wikipedia' + info)
            

        elif 'google' in text_input:
            webbrowser.open('www.google.com')

        elif 'time' in text_input:
            time1 = datetime.datetime.now().strftime("%H:%M:%S")
            speak('The time is: '+ time1)
            

        elif 'date' in text_input:
            date = datetime.datetime.now().date().strftime("%d-%b-%Y")
            speak('Todays date is ' + date)
            

        elif('headlines' or 'news') in text_input:
            # '''-------------FOR NEWS--------------'''
            speak('colleting the news')
            import requests
            titles = []
            top_10 = 0
            authors = []
            url = ('http://newsapi.org/v2/top-headlines?country=us&apikey=4d3cb66bcd1c4e6a937168d85cefcb00')
            response = requests.get(url)
            newsjson = response.json()
            articles = newsjson['articles']
            for article in articles:
                if(top_10 != 10):
                    titles.append(article['title'])
                    authors.append(article['author'])
                    top_10 += 1
                else:
                    break
            i = 1
            for title, author in zip(titles,authors):
                speak(f'News number {i} is   {title}   by   {author}')
                
                i += 1
                if i == 6:
                    speak('Thank You')
                    

        elif('chat' or 'talk' or 'say something') in text_input:
            bott()

        elif('notepad' or 'editor') in text_input:
            os.system('notepad')

        elif('which day' or 'day') in text_input:
            print("--------------------------------------------")
            print("Write any date get its day")
            print("--------------------------------------------")
            print()
            daydecider = 0
            month_code = {1:1, 2:4, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
            day_code = {0:"Saturday", 1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thrusday", 6:"Friday"}
            print("Date example for 4 jan 1999, write as 04/01/1999")
            date1 = input("Enter your Date in dd/mm/yyyy format: ")
            if(len(date1) > 10):
                print("Invalid Date")
                exit()
            day,month,year = int(date1.split("/")[0]),int(date1.split("/")[1]),date1.split("/")[2]

            leap_year_decider = int(year[2:4])
            first2yeardigit = int(year[0:2])
            sum = (leap_year_decider % 7) + (int(leap_year_decider / 4)) + (day % 7) + (month_code[month])
            if((first2yeardigit % 4) == 0):
                yearcode = 6
            elif((first2yeardigit % 4) == 1):
                yearcode = 4
            elif((first2yeardigit % 4) == 2):
                yearcode = 2
            else:
                yearcode = 0

            daydecider += (sum + yearcode)
            speak('Its ' + day_code[daydecider % 7])
            
            
        else:
            speak("Here is what i found on google")
            webbrowser.open(f'https://www.google.co.in/#q={text_input}')


def speak(str):
    engine.say(str)
    engine.runAndWait()
    
if __name__ == '__main__':
    listen()
