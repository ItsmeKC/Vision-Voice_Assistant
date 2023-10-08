import ctypes #ctypes are like bridge in python to communicate with other languages like c,c++
import shutil #shutil is used to manage files or directory (copy, move, rename, delete files or folders)
import smtplib 
import openai #accessing ai models like gpt
import speech_recognition as sr #for vocal communication with the computer
import pyttsx3 #text into speech (python text to speech version 3)
import datetime #current date and time
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
from gtts import gTTS
import wolframalpha
import json
import requests
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon !")

	else:
		speak("Good Evening !")

	assname =("Vision")
	speak("I am your Assistant")
	speak(assname)

def username():
	speak("What should I call you?")
	uname = takeCommand()
	speak("Welcome")
	speak(uname)
	
	
	print("Welcome ", uname)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        speak("Recognizing...")
        print("Recognizing...")
        statement = r.recognize_google(audio, language ='en-in')
        print(f"User said: {statement}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        speak("I'm sorry, I'm unable to Recognize your voice.")
        return ""
    return statement

def set_reminder():
    speak("What should I remind you about?")
    reminder_text = takeCommand()
    if reminder_text:
        speak("When should I remind you? Please specify the time.")
        time_text = takeCommand()
        try:
            reminder_time = datetime.datetime.strptime(time_text, "%H:%M")
            current_time = datetime.datetime.now()
            if reminder_time < current_time:
                speak("I can't set a reminder for the past.")
            else:
                time_difference = (reminder_time - current_time).total_seconds()
                time.sleep(time_difference)
                speak(f"Reminder: {reminder_text}")
        except ValueError:
            speak("Sorry, I didn't understand the time format. Please specify the time as HH:MM.")

def send_email(to_email, subject, body):
    # Replace with your email and password
    sender_email = 'your_email_id'
    sender_password = 'your_password'
    try:
        # Initialize SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to your email account
        server.login(sender_email, sender_password)
        
        # Compose the email
        message = f'Subject: {subject}\n\n{body}'   

        # Send the email
        server.sendmail(sender_email, to_email, message)
        
        # Close the SMTP server
        server.quit()
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    

speak("Loading your AI personal assistant Vision")



if __name__=='__main__':

    clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
    clear()
    wishMe()
    username()


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Vision is shutting down,Good bye')
            print('your personal assistant Vision is shutting down,Good bye')
            break

        if "set reminder" in statement:
            set_reminder()

        if "send email" in statement:
            speak("To whom would you like to send the email?")
            print("To whom would you like to send the email?")
            to_email = input("Recipient's Email: ")
            speak("What's the subject of the email?")
            print("What's the subject of the email?")
            subject = input("Subject: ")
            speak("What should the email say?")
            print("What should the email say?")
            body = input("Email Body: ")
            if send_email(to_email, subject, body):
                speak("Email sent successfully.")
                print("Email sent successfully.")

            else:
                speak("Sorry, there was an error sending the email.")
                print("Sorry, there was an error sending the email.")


        if 'wikipedia' in statement:
            speak('Opening Wikipedia...')
            print('Opening Wikipedia...')
            webbrowser.open("https://www.wikipedia.org/")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening Youtube...")
            time.sleep(1)
            print("Youtube is open now")

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Opening Google...")
            time.sleep(1)
            print("Google chrome is open now")

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Opening Google Mail...")
            time.sleep(1)
            print("Gmail is open now")


        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
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
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Vision version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow, predict time, take a photo, search wikipedia, predict weather' 
                  'in different cities, get top headline news from times of india and several other commands.')
            
            print('I am Vision version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and  several other commands.')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Karan")
            print("I was built by Karan")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Opening Stackoverflow...")
            print("Here is stackoverflow")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            print('Here are some headlines from the Times of India,Happy reading')
            time.sleep(1)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")
        
        elif 'joke' in statement:
              speak(pyjokes.get_joke())

        elif 'how are you' in statement or "how r u" in  statement:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            
        elif 'fine' in statement or "good" in statement:
            speak("It's good to know that your fine")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(1)

        elif 'exit' in statement or "stop" in statement:
            speak("Thanks for giving me your time")
            print("Thanks for giving me your time")
            exit()

        elif "where is" in statement:
            statement = statement.replace("where is", "")
            location = statement
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")


        elif 'change background' in statement:
            ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"",
													0)
            speak("Background changed successfully")
            print("Background changed successfully")

        elif 'lock window' in statement:
            print("locking the device")
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            
        elif 'shutdown system' in statement:
            print("Sure! Hold On a Sec ! Your system is on its way to shut down")
            speak("Sure! Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in statement:
            print('Restarting this device...')
            speak('Restarting this device')
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in statement or "sleep" in statement:
            print("Hibernating")
            speak("Hibernating")
            subprocess.call("shutdown / h")

time.sleep(1)