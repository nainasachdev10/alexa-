import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hi i am your alexa , what can i do for you")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('the current time is' + time)
    elif 'who is' in command:
        person = command.replace ('who is', '')
        per_info = wikipedia.summary(person , 1)
        print(per_info)
        talk(per_info)
    elif 'who was' in command:
        person = command.replace ('who was', '')
        per_info = wikipedia.summary(person , 1)
        print(per_info)
        talk(per_info)
    elif 'where' in command:
        place = command.replace('where', '')
        place_info = wikipedia.summary(place , 2)
        print(place_info)
        talk(place_info)
    elif 'wikipedia' in command:
        wiki = command.replace('wikipedia', '')
        wiki_info = wikipedia.summary(wiki , 2)
        print(wiki_info)
        talk(wiki_info)
    elif 'information of' in command:
        wiki = command.replace('information of', '')
        wiki_info = wikipedia.summary(wiki , 2)
        print(wiki_info)
        talk(wiki_info)
    elif 'i love you' in command:
        talk('tauba , tauba , tauba , saara mood kharaab kar diya')
    elif 'will you marry me' in command:
        talk('oh, i really wish i could , but i dont want to')
    elif 'are you single' in command:
        talk('no, i am in a very serious and loving relationship with mister wifi')
    elif 'how are you' in command:
        talk('i am good , thank you for asking')
    elif 'hello' in command:
        talk('hey')
    elif 'thank you' in command:
        talk('your welcome . i am glad that i was helpful')
    elif 'i am bored' in command:
        talk('do you want to listen something funny, , , if yes , then ask me to tell you a joke')
    elif ' i miss you' in command:
        talk('aww , , , , , , i miss you even more')

    elif 'repeat after me' in command:
        repeatt = command.replace('repeat after me' , ' ')
        talk(repeatt)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        talk('please say the command again')


while True:
    run_alexa()