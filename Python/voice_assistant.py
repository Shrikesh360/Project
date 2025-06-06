
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import os
import smtplib

# Initialize pyttsx3
engine = pyttsx3.init()


def speak(text):
    """Converts text to speech"""
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    """Takes microphone input and returns string output"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
        return query.lower()
    except Exception:
        print("Could not understand, please say that again.")
        return "None"


def wishMe():
    speak("Hello Shrikesh Gupta! How can I assist you?")


def sendEmail(to, content):
    """Send an email (configure your own email credentials)"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if query == "None":
            continue  # Skip if no valid command

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("The search term is too broad. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No results found on Wikipedia.")

        elif 'youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://youtube.com")

        elif 'facebook' in query:
            speak("Opening Facebook...")
            webbrowser.open("https://facebook.com")

        elif 'whatsapp' in query:
            speak("Opening WhatsApp...")
            webbrowser.open("https://web.whatsapp.com")

        elif 'linkedin' in query:
            speak("Opening LinkedIn...")
            webbrowser.open("https://www.linkedin.com")

        elif 'github' in query:
            speak("Opening GitHub...")
            webbrowser.open("https://github.com")

        elif 'google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'calculator' in query:
            speak("Opening Calculator...")
            os.system("calc")

        elif 'refresh' in query:
            speak("Refreshing the system...")
            os.system("ipconfig /flushdns")

        elif 'today live news' in query or 'news' in query:
            speak("Opening today's live news...")
            webbrowser.open("https://www.bbc.com/news")

        elif 'naukri' in query or 'naukri.com' in query:
            speak("Opening Naukri.com...")
            webbrowser.open("https://www.naukri.com")

        elif 'instagram' in query:
            speak("Opening Instagram...")
            webbrowser.open("https://instagram.com")

        elif 'pycharm' in query:
            speak("Opening PyCharm...")
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe")

        elif 'ms excel' in query:
            speak("Opening Microsoft Excel...")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

        elif 'ms word' in query:
            speak("Opening Microsoft Word...")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif 'ms powerpoint' in query:
            speak("Opening Microsoft PowerPoint...")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

        elif 'mysql' in query:
            speak("Opening MySQL...")
            os.startfile("C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe")

        elif 'shutdown' in query:
            speak("Shutting down the system in 5 seconds.")
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            speak("Restarting the system in 5 seconds.")
            os.system("shutdown /r /t 5")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry, I couldn't send the email.")

        elif 'open gmail' in query:
            speak("Opening Gmail...")
            webbrowser.open("https://mail.google.com")

        elif 'open chatgpt' in query or 'chat gpt' in query:
            speak("Opening ChatGPT...")
            webbrowser.open("https://chat.openai.com/")

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye Shrikesh! Have a nice day.")
            break

        else:
            speak("Sorry, I didn't understand that.")



