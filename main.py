def main():
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import pywhatkit as kit
    from AppOpener import run
    import time
    import requests
    import smtplib

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Hello I am Risul a bot made by Vishist, to begin please type your name")
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
        # input(print("CLICK ENTER TO START"))
        with sr.Microphone() as source:
            print("..........LISTENING...........")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print(".......Recognizing........")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception:
            print("Sorry, couldn't catch that please repeat")
            query = "NONE"
        return query

    greet_user()

    def robot():
        if __name__ == "__main__":

            if True:
                query = take_user_cmd().lower()

                if "open notepad" in query:
                    speak("opening notepad")
                    run("notepad")
                elif "open spotify" in query:
                    speak("opening spotify")
                    run("Spotify")
                elif "open MS  word" in query:
                    speak("opening word")
                    run("word")
                elif "open whatsapp" in query:
                    speak("opening whatsapp")
                    run("WhatsApp")
                elif "open netflix" in query:
                    speak("opening netflix")
                    run("Netflix")
                elif "play on youtube" in query:
                    speak("What do you want to play on youtube?")
                    req = take_user_cmd().lower()
                    kit.playonyt(req)
                elif "search on google" in query:
                    speak("What do you want to search sir?")
                    req = take_user_cmd().lower()
                    kit.search(req)
                elif "what's the date" in query:
                    speak(datetime.date.today())
                elif "what's the time" in query:
                    speak(time.strftime("%H:%M:%S", time.localtime()))
                elif "open file explorer" in query:
                    speak("opening file explorer")
                    run("file explorer")
                elif "open calculater" in query:
                    speak("opening calculater")
                    run("calculator")
                elif "open camera" in query:
                    speak("opening camera")
                    run("camera")
                elif "open settings" in query:
                    speak("opening settings")
                    run("settings")
                elif "open vlc" in query:
                    speak("opening vlc")
                    run("vlc media player")
                elif "open chrome" in query:
                    speak("opening chrome")
                    run("google chrome")
                elif "send a message" in query:
                    speak("sure, please type the number with the country code to whom I have to message")
                    number = (input("Enter the Number here"))
                    speak("now enter the message you want to send")
                    msg = input("Enter the message here")
                    kit.sendwhatmsg_instantly(number, msg)
                elif "tell me a joke" in query:
                    def joke():
                        headers = {'Accept': 'application/json'}
                        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
                        return res["joke"]

                    jokee = joke()
                    speak(jokee)
                    print(jokee)
                elif "give me an advice" in query:
                    def advice():
                        res = requests.get("https://api.adviceslip.com/advice").json()
                        return res["slip"]["advice"]

                    advicee = advice()
                    speak(advicee)
                    print(advicee)
                # elif "send an email" in query:
                #     li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]
                #     for dest in li:
                #         s = smtplib.SMTP('smtp.gmail.com', 587)
                #         s.starttls()
                #         s.login("sender_email_id", "sender_email_id_password")
                #         message = "Message_you_need_to_send"
                #         s.sendmail("sender_email_id", dest, message)
                #         s.quit()


                else:
                    speak("sorry, that is currently out of my reach")

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
