import speech_recognition as sr
import os
from utilities import *
from weather import *
import time

ERROR = 256

# For Speech Recognition
recorder = sr.Recognizer()
microphone = sr.Microphone()

weather = Weather()
print(weather.get_current_forcast())
print(weather.get_tomorrow_forcast())


# speak("Ro hit. Do you want to get lunch tomorrow?")
# time.sleep(3.5)
# speak("Hey, Pruh nay. Do you want to get lunch tomorrow?")
# time.sleep(2.5)
# speak("Brennen. Do you want to get lunch tomorrow?")
# time.sleep(2.5)
#
# speak("Yo, Uneesh.")
# time.sleep(1.5)
# speak("Go fuck yourself.")
try:
    # Configuring Speech
    with microphone as source: recorder.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(recorder.energy_threshold))
    recorder.non_speaking_duration = 0.3
    recorder.pause_threshold = 0.4

    while True:
        print("Say something!")
        with microphone as source: audio = recorder.listen(source)
        print("Got it! Now to recognize it...")
        try:
            text = recorder.text(audio).lower()
            print(u"You said {}".format(text).encode("utf-8"))

            if asking_for_joke(text):
                tell_joke()
                continue
            if asking_for_open(text):
                open_app_or_website(text)
                continue
            if asking_for_tomorrow_weather(text):
                speak(weather.get_tomorrow_forcast())
                continue
            if asking_for_current_weather(text):
                speak(weather.get_current_forcast())
                continue
            if asking_for_search(text):
                search(text)
                continue
            if asking_for_song(text):
                play_youtube(text)
            if re.search(re.compile("Goodbye Jarvis"), text):
                speak("Goodbye")
                break

            if re.search(re.compile("ssh16b"), text):
                os.system("osascript -e 'tell application \"Terminal\" to activate' -e 'tell application \"System Events\" to tell process \"Terminal\" to keystroke \"n\" using command down' -e 'tell application \"Terminal\" to do script \"ssh16b\" in selected tab of the front window'")

            check = re.search(re.compile("^haha(.+)"), text)
            if check:
                speak("haaahahahaahahahahhahahaaaaaaaaaaa")
            check = re.search(re.compile("laugh"), text)
            if check:
                speak("teheheeeheeeheeeheeheeheeeheeee")
        except sr.UnknownValueError:
            print("Oops! Didnt catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
