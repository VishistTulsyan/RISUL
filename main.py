def main():  # I know main function isn't required in py
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import pywhatkit as kit
    from AppOpener import run
    import time
    import requests
    import smtplib
    import wikipedia
    import googlesearch

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Hello I am Risul an AI powered virtual assistant, to get started, please type your name")
    user = input("type your name")

    def greet_user():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak(f"GOOD MORNING {user}")
        elif hour > 12 and hour < 17:
            speak(f"GOOD AFTERNOON {user}")
        else:
            speak(f"GOOD EVENING {user}")

    def take_user_cmd():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("..........LISTENING...........")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print(".......Recognizing........")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception:
            print("Sorry, I didn't get that, I'd appreciate if you could try again  ")
            query = "NONE"
        return query

    greet_user()

    def robot():
        if __name__ == "__main__":

            if True:
                query = take_user_cmd().lower()

                if "notepad" in query:
                    try:
                        speak("opening notepad")
                        run("notepad")
                    except:
                        speak("Unknown error occurred")

                elif "spotify" in query:
                    try:
                        speak("opening spotify")
                        run("Spotify")
                    except:
                        speak("Unknown error occurred")

                elif "word" in query:
                    try:
                        speak("opening word")
                        run("word")
                    except:
                        speak("Unknown error occurred")

                elif "whatsapp" in query:
                    try:
                        speak("opening whatsapp")
                        run("WhatsApp")
                    except:
                        speak("Unknown error occurred")

                elif "netflix" in query:
                    try:
                        speak("opening netflix")
                        run("Netflix")
                    except:
                        speak("Unknown error occurred")


                elif "play on youtube" in query:
                    try:
                        speak("What do you want to play on youtube?")
                        req = take_user_cmd().lower()
                        kit.playonyt(req)
                    except:
                        speak("Unknown error occurred")

                elif "date" in query:
                    try:
                        speak(datetime.date.today())
                    except:
                        speak("Unknown error occurred")

                elif "time" in query:
                    try:
                        speak(time.strftime("%H:%M:%S", time.localtime()))
                    except:
                        speak("Unknown error occurred")

                elif "file explorer" in query:
                    try:
                        speak("opening file explorer")
                        run("file explorer")
                    except:
                        speak("Unknown error occurred")

                elif "calculater" in query:
                    try:
                        speak("opening calculater")
                        run("calculator")
                    except:
                        speak("Unknown error occurred")

                elif "camera" in query:
                    try:
                        speak("opening camera")
                        run("camera")
                    except:
                        speak("Unknown error occurred")

                elif "settings" in query:
                    try:
                        speak("opening settings")
                        run("settings")
                    except:
                        speak("Unknown error occurred")

                elif "vlc" in query:
                    try:
                        speak("opening vlc")
                        run("vlc media player")
                    except:
                        speak("Unknown error occurred")

                elif "chrome" in query:
                    try:
                        speak("opening chrome")
                        run("google chrome")
                    except:
                        speak("Unknown error occurred")

                elif "message" in query:
                    try:
                        speak(
                            "Sure, please type the number with the country code to whom I have to message")
                        number = (input("Enter the Number here"))
                        speak("now enter the message you want to send")
                        msg = input("Enter the message here")
                        kit.sendwhatmsg_instantly(number, msg)
                    except:
                        speak("Unknown error occurred")

                elif "joke" in query:
                    try:
                        def joke():
                            headers = {'Accept': 'application/json'}
                            res = requests.get(
                                "https://icanhazdadjoke.com/", headers=headers).json()
                            return res["joke"]

                        jokee = joke()
                        speak(jokee)
                        print(jokee)
                    except:
                        speak("Unknown error occurred")

                elif "advice" in query:
                    try:
                        def advice():
                            res = requests.get(
                                "https://api.adviceslip.com/advice").json()
                            return res["slip"]["advice"]

                        advicee = advice()
                        speak(advicee)
                        print(advicee)
                    except:
                        speak("Unknown error occurred")

                elif " email" in query:
                    try:
                        senderEmailId = input("Please type your email address  ")
                        senderPassword = input("Please type the password  ")
                        receiver = input("Enter receivers email address  ")
                        li = [senderEmailId, receiver]
                        for des in li:
                            s = smtplib.SMTP('smtp.gmail.com', 587)
                            s.starttls()
                            s.login(senderEmailId, senderPassword)
                            message = "Message_you_need_to_send"
                            s.sendmail("sender_email_id", des, message)
                            s.quit()
                    except:
                        speak("Unknown error occurred")

                else:
                    try:
                        speak("I found this on the web")
                        wikipedia.summary(query, sentences=5)

                    except:
                        num_page = str(3)
                        search_results = googlesearch.search(query, num_page)
                        for result in search_results:
                            print(result.description)
                            speak(result.description)

    robot()

    while True:
        speak("Would you like to run this tool again? \n")

        query = take_user_cmd().lower()

        if query == "yes" or query == "yep" or query == "yup" or query == "sure":
            speak("very well, say again what you want me to do")
            robot()
        elif query == "no" or query == "not now" or query == "nope" or query == "nah":
            speak("Cool thanks for using the programme")
            hour = datetime.datetime.now().hour
            if hour >= 22 and hour < 6:
                speak(f"Good NIGHT{user}")
            else:
                speak(f"have a good day{user}")
            break
        else:
            speak(print("That maybe beyond my abilities at the moment"))


main()
