import speech_recognition as sr
import sys

from os import path

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"YOUR CREDENTIALS HERE"
BING_KEY = r"YOUR BING KEY HERE"
IBM_USERNAME = r"IBM BLUEMIX USERNAME"
IBM_PASSWORD = r"IBM BLUEMIX PASSWORD"

if __name__ == '__main__':
    AUDIO_FILE = sys.argv[1]
    assert path.isfile(AUDIO_FILE), "'{}' is not a valid file".format(AUDIO_FILE)

    print("Reading audio file '{}'".format(AUDIO_FILE))
    with sr.AudioFile(AUDIO_FILE) as source:
        r = sr.Recognizer()
        audio = r.record(source) 
        
        print("Processing audio for Bing")
        try:
            text = r.recognize_bing(audio, key=BING_KEY, language='pt-BR')
            print("Microsoft Bing Voice Recognition thinks you said:\n" + text)
        except sr.UnknownValueError:
            print("Microsoft Bing Voice Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

        try:
            text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='pt-BR')
            print("Google Cloud Speech thinks you said:\n" + text)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))

        # recognize speech using IBM Speech to Text
        try:
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='pt-BR')
            print("IBM Speech to Text thinks you said:\n" + text)
        except sr.UnknownValueError:
            print("IBM Speech to Text could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from IBM Speech to Text service; {0}".format(e))
