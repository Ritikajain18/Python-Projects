import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for Today...lets begin")
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=070ac55b0f9249be950d43d58aaf3b7d"
    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts=news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on to the next news....listen carefully!!!")
    speak("Thanks for Listening")