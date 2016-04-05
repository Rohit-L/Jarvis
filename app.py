import speech_recognition as sr
import pyttsx
import os
import re

ERROR = 256

# For Speech Recognition
r = sr.Recognizer()
m = sr.Microphone()

# Text-To-Speech Engine
engine = pyttsx.init()
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', "com.apple.speech.synthesis.voice.samantha")

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    r.non_speaking_duration = 0.3
    r.pause_threshold = 0.4
    r.energy_threshold = 400
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # Google Speech Recognition
            value = r.recognize_google(audio)
            print(u"You said {}".format(value).encode("utf-8"))

            check = re.search(re.compile("^open (.+)"), value)
            if check:
                term = check.group(1)
                engine.say("Opening " + term)
                cmd = os.system("open -a '" + term + "'")
                if cmd == ERROR:
                    os.system("open http://" + term + ".com")
                engine.runAndWait()
                continue

            check = re.search(re.compile("^search (.+)"), value)
            if check:
                terms = check.group(1).split()
                engine.say("Searching " + " ".join(terms))
                os.system("open http://google.com/search?q=" + "+".join(terms))
                engine.runAndWait()
                continue

            check = re.search(re.compile("kill yourself"), value)
            if check:
                engine.say("Goodbye")
                engine.runAndWait()
                break

            if re.search(re.compile("run"), value):
                os.system("osascript -e 'tell application \"Terminal\" to activate' -e 'tell application \"System Events\" to tell process \"Terminal\" to keystroke \"n\" using command down' -e 'tell application \"Terminal\" to do script \"ssh16b\" in selected tab of the front window'")

            check = re.search(re.compile("^haha(.+)"), value)
            if check:
                engine.say("haaahahahaahahahahhahahaaaaaaaaaaa")

            engine.runAndWait()
        except sr.UnknownValueError:
            engine.say("I didn't get that")
            engine.say("try again")
            engine.runAndWait()
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
