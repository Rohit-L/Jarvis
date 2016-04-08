import pyglet
import os
import re
import random
import webbrowser

def speak(text):
    cmd = 'say -v "Samantha" "' + text + '"'
    print(cmd)
    os.system("say -v 'Samantha' '" + text + "'")

def play(file):
    pyglet.resource.media(file).play()

def asking_for_tomorrow_weather(text):
    return re.search(re.compile("(.+)weather tomorrow"), text) or re.search(re.compile("(.+)weather like tomorrow"), text)

def asking_for_current_weather(text):
    return re.search(re.compile("(.+)weather (.+)"), text)

def asking_for_open(text):
    return re.search(re.compile("^open (.+)"), text)

def asking_for_search(text):
    return re.search(re.compile("^search (.+)"), text)

def asking_for_joke(text):
    return re.search(re.compile("tell me a joke"), text)

def asking_for_song(text):
    return re.search(re.compile("play song (.+)"), text)

def open_app_or_website(text):
    term = re.search(re.compile("^open (.+)"), text).group(1)
    speak("Opening " + term)
    cmd = os.system("open -a '" + term + "'")
    if cmd == ERROR:
        os.system("open http://" + term + ".com")

def search(text):
    terms = re.search(re.compile("^search (.+)"), text).group(1).split()
    speak("Searching " + " ".join(terms))
    os.system("open http://google.com/search?q=" + "+".join(terms))

def tell_joke():
    jokes = ["How do you kill vegetarian vampires? With a steak to the heart.",
    "So this guy with a premature ejaculation problem comes out of nowhere.",
    "What kind of shoes do ninjas wear? Sneakers. Hahahaha",
    "How come bikes cannot stand on their own? Because they are two tired.",
    "Last night I almost had a threesome. but I only needed two more people",
    "When you get a bladder infection, urine trouble.",
    "You want to hear a pizza joke? Never mind, it is pretty cheesy."]
    speak(random.choice(jokes))

def play_youtube(text):
    terms = re.search(re.compile("play song (.+)"), text).group(1).split()
    speak("Playing " + " ".join(terms) + " on youtube.")
    terms.append("youtube")
    controller = webbrowser.get()
    controller.open("http://google.com/search?q=" + "+".join(terms) + "&btnI")
