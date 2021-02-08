import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess
import os
import requests
from urllib.request import urlopen, Request
import time
from bs4 import BeautifulSoup
import cv2
from gtts import gTTS
from playsound import playsound
import random




saat = ["saat", "kaç", "saat kaç", "zaman", "saat kaç", "zamamnı söyle", "saati söyler misin","zamanı söyler misin"]
kapatma = ["görüşürüz", "baybay", "kapatabilirsin", "kapat", "kapalı mod"]
videoac = ["video açar mısın", "video aç", "YouTube'u aç", "Youtube aç", "Youtube"]
yayın = ["yayını", "yayın aç", "yayını aç", "Twitch'i", "Twitch", "yayın", "Twitch'i aç", "Twitch aç","yayını açar mısın", "yayın açar mısın", "Twitch'i açar mısın", "Twitch açar mısın"]
arama = ["Google'ı", "Google", "arama sayfası", "aramayı", "Google'ı aç", "Google aç", "aramayı aç", "arama aç","Google'ı açar mısın", "aramayı açar mısın", "arama açar mısın"]
çeviri = ["Translate'i", "Translate", "çeviriyi", "çeviri", "dil çevirisi", "Translate'i aç", "Translate aç","çeviriyi aç", "çeviri aç", "çeviriyi açar mısın", "çeviri açar mısın", "Translate'i açar mısın","Translate açar mısın"]
egzersiz = ["egzersizlerimi", "egzersizleri", "egzersizler", "spor", "sporumu", "egzersiz", "egzersizlerimi aç","egzersizleri aç", "egzersiz listemi aç", "spor listemi aç", "sporumu aç","spor listemi açar mısın", "egzersiz listemi açar mısın","egzersizlerim açar mısın","sindirimi açar mısın"]
havadurumu = ["hava durumu", "hava nasıl", "hava durumu nedir", "hava durumunu söyle", "hava durumunu aç","hava durumunu söyler misin"]
araştırma = ["Wikipedia'yı", "Wikipedia", "araştırma", "araştırmayı", "araştırmaya", "araştırma yap","Wikipedia'yı aç", "araştırma yapar mısın"]
senkimsin = ["sen kimsin", "kimsin", "nesin", "adın ne", "ismin ne", "amacın ne", "sen nesin"]
nasılsın = ["naber", "nasılsın", "ne yapıyorsun", "ne haber", "nasıl gidiyor"]
ara = ["internetten bak", "ara", "arama yapar mısın", "internetten bakar mısın"]
fotoğraflar = ["fotoğrafları aç", "fotoğraflarımı", "resimleri", "resimlerimi", "fotoğrafları açar mısın","resimlerimi açar mısın", "resimleri aç"]
canlıders = ["canlı dersini açar mısın","canlı dersin bir açar mısın","yalnız dersimi açar mısın","yandı dersimi açar mısın","canlı dersimi", "canlı derslerimi", "derslerimi", "dersimi", "canlı derslerimi aç","canlı dersimi aç", "dersimi aç", "canlı dersini aç", "canlı ders mi aç","canlı derslerimi açar mısın", "canlı dersimi açar mısın", "canlı derslerim açar mısın","canlı ders açar mısın", "canlı ders mi açar mısın", "canlı Dersim açar mısın","canlı ders 20 açar mısın", "yanlı Dersim açar mısın", "canlı Dersim açar mısın", "yanı dersimi açar mısın","Yalı dersimi açar mısın"]
müzik = ["müzik açar mısın","müziklerimi", "dinlediğim", "müzikleri", "müzikler", "müzik", "şarkı", "müzik aç", "müziklerimi aç","müzik listemi aç", "müzik listemi açar mısın", "müziklerimi açar mısın", "şarkılarımı açar mısın" "şarkı listemi açar mısın"]
sosyalmedya = ["Instagram", "Facebook", "Twitter", "sosyal medyayı", "sosyal medya", "medyadan", "sosyal medya aç", "sosyal medyamı aç"]
oyun = ["oyunumu", "oyunu", "oyun", "Call Of Duty", "oyunumu aç", "oyunumu açar mısın", "oyunu açar mısın"]
hesapmakinesi = ["hesap makinesi", "hesaplama", "hesaplayıcı", "çarpı", "bölü", "artı", "eksi","hesaplama yapar mısın"]
yazı = ["not", "çevir", "yaz", "yazı yaz", "yazıya çevir", "not al", "yazı yazar mısın","söylediklerimi yazıya çevirir misin", "not alır mısın"]
uygulamalar = ["uygulamalar", "ders uygulamalarını", "uygulama", "program", "Uygulamalar", "uygulamalarını","ders uygulamalarını aç", "ders uygulamamı aç", "ders uygulamalarını aç","ders uygulamalarımı açar mısın", "ders uygulamalarını açar mısın", ]
haber = ["haber", "haber sitesi", "haber aç", "haber sitesi aç", "haberleri aç", "haber sitelerini aç", "haber sitesini açar mısın", "haber sitelerini açar mısın"]
bedeneğitimi = ["beden eğitimi", "Beden eğitimi", "bedeneğitimi", "Bedeneğitimi"]
fizik = ["Fizik", "fizik"]
tarih = ["Tarih", "tarih"]
ingilizce = ["Ingilizce", "İngilizce", "ingilizce"]
matematik = ["Matematik", "matematik"]
kimya = ["Kimya", "kimya"]
coğrafya = ["Coğrafya", "coğrafya"]
biyoloji = ["Biyoloji", "biyoloji"]
müzikdersi = ["Müzik dersi", "müzik dersi"]
bilgisayar = ["Bilgisayar", "bilgisayar"]
edebiyat = ["edebiyat", "Edebiyat"]
din = ["Din", "din"]
felsefe = ["Felsefe", "felsefe"]
almanca = ["Almanca", "almanca"]
borsa = ["Borsa", "borsayı söyler misin", "borsa", "döviz kuru", "döviz", "borsaya söyler misin","Bu sayı söyler misin", "Morse söyler misin"]
euro = ["Euro", "euro"]
dolar = ["Dolar", "dolar", "donar"]
birim = ["Birim çevirir misin", "Birimi çevir", "birim çevirir misin", "birimi çevir"]
neşe = ["eğlendir beni", "moralim bozuk"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices.id')

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)




def Dile():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("İyi günler efendim")
    else:
        speak("İyi geceler efendim")

def Dile2():
    hour2 = datetime.datetime.now().hour
    if hour2 >= 7 and hour2 < 17:
        speak("İyi günler efendim")
    else:
        speak("İyi geceler efendim")
def Komutal():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum")
        audio = r.listen(source)

        try:
            durum = r.recognize_google(audio, language='tr-tr')
            print(f"user said:{durum}\n")

        except Exception as e:
            speak("Rica etsem tekrar söyler misiniz?")
            return "None"
        return durum

def hosgeldin():
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    face_cascade.load(r'A:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
    webcam = cv2.VideoCapture(0)
    while True:
        succsessfull_frame_read, frame = webcam.read()
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coordinates = face_cascade.detectMultiScale(grayscaled_img)
        speak("Geri geldiğinize sevindim efendim")
        Dile()




print("Jarvis açılıyor")
speak("Jarvis açılıyor")
Dile()

if __name__ == '__main__':

    while True:
        speak("Nasıl yardımcı olabilirim")
        durum = Komutal().lower()
        if durum == 0:
            continue

        if durum in kapatma:
            speak('Güle güle')
            print('güle güle efendim')
            Dile2()
            break

        elif durum in yayın:
            webbrowser.open_new_tab("https://www.twitch.tv")
            speak("İyi eğlenceler")
            time.sleep(2)

        elif durum in arama:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google ı açıyorum")
            time.sleep(5)

        elif "bekleme modu" in durum:
            speak("Bekliyorum efendim")
            hosgeldin()


        elif durum in borsa:
            speak("Hangisini öğrenmek istersiniz Euro ya da dolar")
            para = Komutal()
            if para in euro:
                pasteURL = "http://tr.investing.com/currencies/eur-try"
                data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
                parse = BeautifulSoup(data)
                for dolar in parse.find_all('span', id="last_last"):
                    liste = list(dolar)
                    print("Güncel Euro Kuru: " + str(liste))
                    speak("Euro kuru" + str(liste))
            elif para in dolar:
                pasteURL = "http://tr.investing.com/currencies/usd-try"
                data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
                parse = BeautifulSoup(data)
                for dolar in parse.find_all('span', id="last_last"):
                    liste = list(dolar)
                    print("Güncel Dolar Kuru: " + str(liste))
                    speak("Dolar  kuru" + str(liste))

        elif durum in canlıders:
                x = datetime.datetime.now()
                gun = x.strftime("%A")
                if gun=="Monday":
                    hour2 = datetime.datetime.now()
                    hour4 = hour2.strftime("%X")
                    if hour4 >= "08:55:00" and hour4 < "09:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/6604996519?pwd=WDlLZmk1SjhlclVwams0UHU0elFvQT09")
                        speak("Beden eğitimi dersiniz açılıyor")
                    elif hour4 >= "9:35:00" and hour4 < "10:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/6604996519?pwd=WDlLZmk1SjhlclVwams0UHU0elFvQT09")
                        speak("Beden eğitimi dersiniz açılıyor")
                    elif hour4 >= "10:15:00" and hour4 < "10:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/3938261304?pwd=TTFIV0xRajUxUkdyQVV3TXNKVm9wdz09")
                        speak("Fizik dersiniz açılıyor")
                    elif hour4 >= "10:55:00" and hour4 < "11:30:00":
                        webbrowser.open_new_tab("https://us05web.zoom.us/j/5921692574?pwd=T3ljUmxtVVR4SlNHck1oTERpaEVXZz09")
                        speak("Tarih dersiniz açılıyor")
                    elif hour4 >= "11:35:00" and hour4 < "12:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7442937560?pwd=dXFwQ08wVHBLZEV3VlpEeUdmK1BJQT09")
                        speak("İngilizce dersiniz açılıyor")
                    elif hour4 >= "12:15:00" and hour4 < "12:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7442937560?pwd=dXFwQ08wVHBLZEV3VlpEeUdmK1BJQT09")
                        speak("İngilizce dersiniz açılıyor")
                    elif hour4 >= "12:55:00" and hour4 < "13:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/5294029513?pwd=Y0NEQUNEdGQ1T3kwYzgvRXpFekhkdz09")
                        speak("matematik dersiniz açılıyor")
                    elif hour4 >= "13:35:00" and hour4 < "14:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/5294029513?pwd=Y0NEQUNEdGQ1T3kwYzgvRXpFekhkdz09")
                        speak("matematik dersiniz açılıyor")
                    else:
                        speak("Dersiniz yok")

                elif gun == "Tuesday":
                    x = datetime.datetime.now()
                    hour4 = x.strftime("%X")
                    if hour4 >= "08:55:00" and hour4 < "09:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7442937560?pwd=dXFwQ08wVHBLZEV3VlpEeUdmK1BJQT09")
                        speak("İngilizce dersiniz açılıyor")
                    elif hour4 >= "10:15:00" and hour4 < "10:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/9145281132?pwd=ZmRBbUlqczBMV0swTlFBSjBnWm9CQT09")
                        speak("Coğrafya dersiniz açılıyor")
                    elif hour4 >= "10:52:00" and hour4 < "11:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/3050648125?pwd=WGlhUjBVdTNieE5jeFQ1bVZxODh4UT09")
                        speak("Biyoloji dersiniz açılıyor")
                    elif hour4 >= "11:35:00" and hour4 < "12:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/8483285035?pwd=c01WV2J6dk9ZUDRJbkYyRkNnTzBEUT09")
                        speak("Müzik dersiniz açılıyor")
                    elif hour4 >= "12:15:00" and hour4 < "12:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/8483285035?pwd=c01WV2J6dk9ZUDRJbkYyRkNnTzBEUT09")
                        speak("Müzik dersiniz açılıyor")
                    elif hour4 >= "12:55:00" and hour4 < "13:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/9494801525?pwd=RjRWNkdldDRISUhOYzc3eStLWkRWdz09")
                        speak("Bilgisayar dersiniz açılıyor")
                    elif hour4 >= "13:35:00" and hour4 < "14:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/9494801525?pwd=RjRWNkdldDRISUhOYzc3eStLWkRWdz09")
                        speak("Bilgisayar dersiniz açılıyor")
                    else:
                        speak("Dersiniz yok")


                elif gun == "Wednesday":
                    hour2 = datetime.datetime.now()
                    hour4 = hour2.strftime("%X")
                    if hour4 >= "08:55:00" and hour4 < "09:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7050722776?pwd=WG1xUTllSzQwSmcrWUVSRDBzOFJkZz09")
                        speak("Edebiyat dersiniz açılıyor")
                    elif hour4 >= "09:35:00" and hour4 < "10:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7442937560?pwd=dXFwQ08wVHBLZEV3VlpEeUdmK1BJQT09")
                        speak("İngilizce dersiniz açılıyor")
                    elif hour4 >= "10:12:00" and hour4 < "10:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/3050648125?pwd=WGlhUjBVdTNieE5jeFQ1bVZxODh4UT09")
                        speak("Biyoloji dersiniz açılıyor")
                    elif hour4 >= "10:55:00" and hour4 < "11:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/5294029513?pwd=Y0NEQUNEdGQ1T3kwYzgvRXpFekhkdz09")
                        speak("Matematik dersiniz açılıyor")
                    elif hour4 >= "11:35:00" and hour4 < "12:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/5294029513?pwd=Y0NEQUNEdGQ1T3kwYzgvRXpFekhkdz09")
                        speak("Matematik dersiniz açılıyor")
                    elif hour4 >= "12:15:00" and hour4 < "12:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7442937560?pwd=dXFwQ08wVHBLZEV3VlpEeUdmK1BJQT09")
                        speak("İngilizce dersiniz açılıyor")
                    elif hour4 >= "12:55:00" and hour4 < "13:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/3938261304?pwd=TTFIV0xRajUxUkdyQVV3TXNKVm9wdz09")
                        speak("Fizik dersiniz açılıyor")
                    else:
                        speak("Dersiniz yok")

                elif gun == "Thursday":
                    hour2 = datetime.datetime.now()
                    hour4 = hour2.strftime("%X")
                    if hour4 >= "08:55:00" and hour4 < "09:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/4159534427?pwd=SzY4ZkE4YVFUWTlaWlJpTmkzUEZiUT09")
                        speak("Din dersiniz açılıyor")
                    elif hour4 >= "10:15:00" and hour4 < "10:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/3805586088?pwd=Y0F2SG9sOUdIdFlzVGFCWHVpR3BFZz09")
                        speak("Felsefe dersiniz açılıyor")
                    elif hour4 >= "10:55:00" and hour4 < "11:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7050722776?pwd=WG1xUTllSzQwSmcrWUVSRDBzOFJkZz09")
                        speak("Edebiyat dersiniz açılıyor")
                    elif hour4 >= "11:35:00" and hour4 < "12:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7050722776?pwd=WG1xUTllSzQwSmcrWUVSRDBzOFJkZz09")
                        speak("Edebiyat dersiniz açılıyor")
                    elif hour4 >= "12:15:00" and hour4 < "12:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7442937560?pwd=dXFwQ08wVHBLZEV3VlpEeUdmK1BJQT09")
                        speak("İngilizce dersiniz açılıyor")
                    elif hour4 >= "12:55:00" and hour4 < "13:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7035157301?pwd=alZJdDl6R2E2enhlKzFCNlYweXVJUT09")
                        speak("Almanca dersiniz açılıyor")
                    elif hour4 >= "13:35:00" and hour4 < "14:10:00":
                        webbrowser.open_new_tab("https://us05web.zoom.us/j/5921692574?pwd=T3ljUmxtVVR4SlNHck1oTERpaEVXZz09")
                        speak("Tarih dersiniz açılıyor")
                    else:
                        speak("Dersiniz yok")

                elif gun == "Friday":
                    hour2 = datetime.datetime.now()
                    hour4 = hour2.strftime("%X")
                    if hour4 >= "08:55:00" and hour4 < "09:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/9145281132?pwd=ZmRBbUlqczBMV0swTlFBSjBnWm9CQT09")
                        speak("Coğrafya dersiniz açılıyor")
                    elif hour4 >= "09:35:00" and hour4 < "10:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/3805586088?pwd=Y0F2SG9sOUdIdFlzVGFCWHVpR3BFZz09")
                        speak("Felsefe dersiniz açılıyor")
                    elif hour4 >= "10:15:00" and hour4 < "10:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/5294029513?pwd=Y0NEQUNEdGQ1T3kwYzgvRXpFekhkdz09")
                        speak("Matematik dersiniz açılıyor")
                    elif hour4 >= "10:55:00" and hour4 < "11:30:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/5294029513?pwd=Y0NEQUNEdGQ1T3kwYzgvRXpFekhkdz09")
                        speak("Matematik dersiniz açılıyor")
                    elif hour4 >= "11:35:00" and hour4 < "12:10:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7050722776?pwd=WG1xUTllSzQwSmcrWUVSRDBzOFJkZz09")
                        speak("Edebiyat dersiniz açılıyor")
                    elif hour4 >= "12:15:00" and hour4 < "12:50:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7050722776?pwd=WG1xUTllSzQwSmcrWUVSRDBzOFJkZz09")
                        speak("edebiyat dersiniz açılıyor")
                    elif hour4 >= "16:25:00" and hour4 < "17:00:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/4159534427?pwd=SzY4ZkE4YVFUWTlaWlJpTmkzUEZiUT09")
                        speak("din dersiniz açılıyor")
                    elif hour4 >= "17:05:00" and hour4 < "17:40:00":
                        webbrowser.open_new_tab("https://us04web.zoom.us/j/7035157301?pwd=alZJdDl6R2E2enhlKzFCNlYweXVJUT09")
                        speak("Almanca dersiniz açılıyor")
                    else:
                        speak("Dersiniz yok")
                elif gun=="Saturday":
                    speak("Bugün tatil")
                elif gun == "Sunday":
                    speak("Bugün tatil")

        elif durum in çeviri:
            webbrowser.open_new_tab("https://translate.google.com")
            speak("Çeviri açılıyor")
            time.sleep(5)

        elif durum in egzersiz:
            speak("Hangi bölgenizi çalıştırmak istiyorsunuz")
            bölge = Komutal()
            if "kol" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=fsqhIBsao8k&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=2&t=181s")
                speak("Kendinizi yormayın lütfen")
            elif "arka kol" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=rxdLG1X-2zU&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=3&t=717s")
                speak("Kendinizi yormayın lütfen")
            elif "göğüs" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=2JzwpMbAEUo")
                speak("Kendinizi yormayın lütfen")
            elif "sırt" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=NqPv3queECU&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=5")
                speak("Kendinizi yormayın lütfen")
            elif "karın" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=73yDE7c-ca8&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=6")
                speak("Kendinizi yormayın lütfen")
            elif "bacak" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=x3SlEFakS_Q&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=7")
                speak("Kendinizi yormayın lütfen")

        elif durum in havadurumu:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("Bulunduğunuz yerin adı nedir")
            city_name = Komutal()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]- 273.15
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Hava " +
                      str(current_temperature) +
                      "\n nem oranı yüzde " +
                      str(current_humidiy) +
                      "\n durumu  " +
                      str(weather_description))

            else:
                speak("şehir bulunamadı")

        elif durum in haber:
            speak("Haberleri açıyorum efendim")
            webbrowser.open_new_tab("https://www.sozcu.com.tr")

        elif durum in araştırma:
            speak("Ne araştırmak istiyorsunuz efendim")
            konu = Komutal()
            print(f"user said:{konu}\n")
            speak('Wikipediadan bakıyorum...')
            konu = konu.replace("wikipedia", "")
            results = wikipedia.summary(konu, sentences=3)
            speak("Wikipediaya göre"+results)
            print(results)


        elif durum in senkimsin:
            speak("Merhaba ben Jarvis. İlke'nin kendisine yaptığı fakat size de yardım edebilecek olan yapay zeka destekli sesli asistanım hala geliştirme aşamasındayım ama anca tek kişi beni bu kadar geliştirebiliyor")

        elif durum in nasılsın:
            speak("İyiyim. Ya siz?")
            his = Komutal()
            if "iyiyim" in his:
                speak("Duyduğuma memnunum")
            else:
                speak("Umarım daha iyi olursunuz")

        elif durum in ara:
            speak("Ne aramak istiyorsunuz")
            merak = Komutal()
            merak = merak.replace("ara", "")
            webbrowser.open_new_tab(merak)
            time.sleep(5)

        elif durum in videoac:
            speak("Ne aramak istiyorsunuz")
            merak = Komutal()
            merak = merak.replace("ara", "")
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+merak)
            time.sleep(5)

        elif durum in saat:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"saat {strTime}")

        elif durum in fotoğraflar:
            speak("which folder do you want to open")
            klasör = Komutal()
            if "benim küçüklüğüm" in klasör:
                os.startfile("A:\!!!!!\pictures\Benim Küçüklüğüm")
                speak("Eskiden tatlıymışsınız ama şuan değilsiniz")
            elif ("rastgele") in klasör:
                os.startfile("A:\!!!!!\pictures\diğer")
                speak("ne söyleyeceğimi bilmiyorum")
            elif ("evrin ablanın düğünü") in klasör:
                os.startfile("A:\!!!!!\pictures\Evrin ablanın düğünü")
                speak("Eğlenceli duruyor")
            elif ("manzaralar") in klasör:
                os.startfile("A:\!!!!!\pictures\manzaralar")
                speak("İlk defa güzel yeteneğiniz varmış")
            elif ("onur abinin nişanı") in klasör:
                os.startfile("A:\!!!!!\pictures\onur abinin nişanı")
                speak("sıkıcı duruyor")
            elif ("köpekler") in klasör:
                os.startfile("A:\!!!!!\pictures\Rodi ve Arap")
                speak("Çok tatlılar keşke cameramla da görebilsem")
        elif "acil durum" in durum:
            speak("Nereye ihtiyacınız var")
            yer=Komutal()
            if "Hastane" or "hastane" in yer:
                webbrowser.open_new_tab("https://www.google.com/search?client=opera-gx&hs=XBH&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALeKk02nr619jrihhF1ixb8qB3lA3WS0Xw:1611944032878&q=en+yakın+hastane&rflfq=1&num=10&ved=2ahUKEwjQu-i738HuAhWOw4sKHWiKAMMQtgN6BAgDEAc#rlfi=hd:;si:;mv:[[41.0227697,28.8981094],[40.9898852,28.841603499999998]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2")
                speak("En yakın hastane")
            elif "eczane" or "Eczane" in yer:
                webbrowser.open_new_tab("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj-luCJsILuAhXxlIsKHRCvDYMQFjAAegQIAhAC&url=https%3A%2F%2Fmaps.google.com%2Fmaps%2Fms%3Fie%3DUTF8%26oe%3DUTF8%26msa%3D0%26msid%3D112522603410425481368.00047b2cf56f6aa68011e&usg=AOvVaw3Vk9z0huMNxESWac5kRrVL")
                speak("En yakın eczane")
            elif "Benzinlik" or "benzinlik" in yer:
                webbrowser.open_new_tab("https://www.google.com/search?client=opera-gx&biw=1879&bih=970&tbs=lf:1,lf_ui:4&tbm=lcl&sxsrf=ALeKk01K2-3biai1WqgfIcqQQmm8o68R0Q:1609767164904&q=en+yakın+benzinlik+google+maps&rflfq=1&num=10&ved=2ahUKEwisuaOAsoLuAhWBmIsKHYOOA6cQtgN6BAgFEAc#rlfi=hd:;si:;mv:[[41.1007986,29.029627500000004],[40.9750114,28.7737689]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4")
                speak("En yakın benzinlik")
            elif "Lokanta" or "lokanta" or "Restoran" or "restoran" or "restorant" or "Restorant" in yer:
                webbrowser.open_new_tab("https://www.google.com/search?client=opera-gx&sa=X&biw=1879&bih=970&tbs=lf:1,lf_ui:4&tbm=lcl&sxsrf=ALeKk03WbpDN722glnaDQLrvJYhouuzsyA:1609767116904&q=en+yakın+restaurant+google+maps&rflfq=1&num=10&ved=2ahUKEwjS57HpsYLuAhUQlIsKHTs1Ca8QtgN6BAgFEAc#rlfi=hd:;si:;mv:[[41.077905699999995,28.982286700000003],[40.952814499999995,28.759789899999998]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4")
                speak("En yakın lokanta")
            elif "Karakol" or "karakol" or "polis" or "Polis" in yer:
                speak("En yakın karakol")
                webbrowser.open_new_tab("https://www.google.com/search?client=opera-gx&biw=1879&bih=970&tbs=lf:1,lf_ui:4&tbm=lcl&sxsrf=ALeKk00--B964btlogSBHQ-JrNXQVe3gIg:1609767041117&q=en+yakın+ilçe+emniyet+google+maps&rflfq=1&num=10&ved=2ahUKEwi3pKDFsYLuAhWS-ioKHbRaBjsQtgN6BAgFEAc#rlfi=hd:;si:;mv:[[41.3587698787428,30.294654313058675],[40.502833122383834,28.2910227212618],null,[40.93218758254495,29.292838517160238],10]")

        elif durum in neşe:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=Cqwic8ufpWk")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=PDdqRQOzQ6A")
            resim = cv2.imread("download.jpg")
            print(type(resim))
            cv2.imshow("sdsf", resim)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif durum in müzik:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=xAooPC2ZToo&list=RDxAooPC2ZToo&index=1")
            speak("İyi eğlenceler")

        elif durum in sosyalmedya:
            speak("Nereye girmek istiyorsunuz Birinci: İnstagram ikinci Facebook üçüncü twitter")
            site = Komutal()
            if "birinci" in site:
                webbrowser.open_new_tab("https://www.instagram.com/?hl=tr")
                speak("İyi eğlenceler")
            elif "ikinci" in site:
                speak("İyi eğlenceler")
                webbrowser.open_new_tab(
                    "https://www.facebook.com/campaign/landing.php?&campaign_id=1603087355&extra_1=s%7Cc%7C305038450781%7Ce%7Cfacebook%7C&placement=&creative=305038450781&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1603087355%26adgroupid%3D61834755758%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D1012782%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQiAzsz-BRCCARIsANotFgO1eFulBC-HZjFgyfIUH3_mwJj2oIpoz2XLT4SmBoeBW9IzDzkiGM8aAjpqEALw_wcB")
            elif "üçüncü" in site:
                webbrowser.open_new_tab("https://twitter.com/home")
                speak("İyi eğlenceler")

        elif durum in oyun:
            subprocess.call([r"A:\Program Dosyaları (x86)\Call of Duty Warzone\Call of Duty Modern Warfare\Modern Warfare Launcher.exe"])
            speak("Lütfen çok oynamayın")

        elif durum in hesapmakinesi:
            speak("Neyi yapmak istiyorsunuz")
            işlem = Komutal()
            if "toplama" in işlem:
                speak("İlk sayı nedir")
                ilksayı = Komutal()
                speak("İkinci sayı nedir")
                ikincisayı = Komutal()
                t1 = ilksayı
                t2 = ikincisayı
                try:
                    t_1 = int(t1)
                    t_2 = int(t2)
                    print(t_1 + t_2)
                    results = (t_1 + t_2)
                    speak(results)
                except ValueError:
                    speak("Lütfen daha sona tekrar deneyin")
            elif "çıkartma" in işlem:
                speak("İlk sayı nedir")
                ilksayı = Komutal()
                speak("İkinci sayı nedir")
                ikincisayı = Komutal()
                c1 = ilksayı
                c2 = ikincisayı
                try:
                    c_1 = int(c1)
                    c_2 = int(c2)
                    print(c_1 - c_2)
                    results = (c_1 - c_2)
                    speak(results)
                except ValueError:
                    speak("Lütfen daha sona tekrar deneyin")
            elif "çarpma" in işlem:
                speak("İlk sayı nedir")
                ilksayı = Komutal()
                speak("İkinci sayı nedir")
                ikincisayı = Komutal()
                m1 = ilksayı
                m2 = ikincisayı
                try:
                    m_1 = int(m1)
                    m_2 = int(m2)
                    print(m_1 * m_2)
                    results = (m_1 * m_2)
                    speak(results)
                except ValueError:
                    speak("Lütfen daha sona tekrar deneyin")
            elif "bölme" in işlem:
                speak("İlk sayı nedir")
                ilksayı = Komutal()
                speak("v")
                ikincisayı = Komutal()
                b1 = ilksayı
                b2 = ikincisayı
                try:
                    b_1 = int(b1)
                    b_2 = int(b2)
                    print(b_1 / b_2)
                    results = (b_1 / b_2)
                    speak(results)
                except ValueError:
                    speak("Lütfen daha sona tekrar deneyin")
            elif "üslü" in işlem:
                speak("İlk sayı nedir")
                ilksayı = Komutal()
                speak("İkinci sayı nedir")
                ikincisayı = Komutal()
                u1 = ilksayı
                u2 = ikincisayı
                try:
                    u_1 = int(u1)
                    u_2 = int(u2)
                    print(u_1 ** u_2)
                    results = (u_1 ** u_2)
                    speak(results)
                except ValueError:
                    speak("Lütfen daha sona tekrar deneyin")
            elif "karekök" or "karakök" in işlem:
                speak("Sayı nedir")
                ilksayı = Komutal()
                s1 = ilksayı
                try:
                    s_1 = int(s1)
                    print(s_1 ** 0.5)
                    results = (s_1 ** 0.5)
                    speak(results)
                except ValueError:
                    speak("Lütfen daha sona tekrar deneyin")

        elif durum in yazı:
            speak("NE yazmak istiyorsunuz")
            yazı1 = Komutal()
            dosya = open('metin_dosyası.txt', 'w')
            dosya.write(yazı1)
            dosya.close()

        elif durum in birim:
            speak("Sayınız hangi türe aittir")
            birim1 = Komutal()
            if "Litre" or "litre" in birim1:
                speak("Neye çevirmek istiyorsunuz")
                birim2 = Komutal()
                if "mililitre" or "mili litre" or "Mili litre" in birim2:
                    speak("Sayınız nedir")
                    eldesayı = Komutal()
                    e1 = eldesayı
                    e2 = 1000
                    try:
                        e_1 = int(e1)
                        e_2 = int(e2)
                        print(e_1 * e_2)
                        results = (e_1 * e_2)
                        speak(results)
                    except ValueError:
                        speak("Lütfen daha sonra tekrar deneyin")
            elif "Miliitre" or "mililitre" in birim1:
                speak("Neye çevirmek istiyorsunuz")
                birim3 = Komutal()
                if "Litre" or "litre" or "ligde" in birim3:
                    speak("Sayınız nedir")
                    eldesayı2 = Komutal()
                    z1 = eldesayı2
                    z2 = 1000
                    try:
                        z_1 = int(z1)
                        z_2 = int(z2)
                        print(z_1 / z_2)
                        results = (z_1 / z_2)
                        speak(results)
                    except ValueError:
                        speak("Lütfen daha sonra tekrar deneyin")

        elif durum in uygulamalar:
            speak("which place do you want to study")
            yayıncılık = Komutal()
            if "okyanus" in yayıncılık or "Okyanus" in yayıncılık:
                speak("which lesson do you want to study")
                ders2 = Komutal()
                if ders2 in biyoloji:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Biyoloji\Biyoloji.exe"])
                elif "coğrafya" in ders2:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Coğrafya\Coğrafya.exe"])
                elif ders2 in edebiyat:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Edebiyat\Edebiyat.exe"])
                elif ders2 in fizik:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Fizik\Fizik.exe"])
                elif ders2 in kimya:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Kimya\Kimya.exe"])
                elif ders2 in matematik:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Matematik\Matematik.exe"])
                elif ders2 in tarih:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Tarih\Tarih.exe"])
            elif "limit" in yayıncılık:
                speak("which lesson do you want to study")
                ders3 = Komutal()
                if ders3 in coğrafya:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Limit\Coğrafya\kutuphane_GAK31HCY.exe"])
                elif ders3 in tarih:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Limit\Tarih\kutuphane_1DAMH6DG.exe"])
                elif ders3 in edebiyat:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Limit\Edebiyat\kutuphane_7CEMC6A9.exe"])
                elif ders3 in fizik:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Limit\Fizik\kutuphane_KDN48LAL.exe"])
                elif ders3 in matematik:
                    speak("Have good lessons sir")
                    subprocess.call([r"A:\!!!!!\Her Şey\Uygulamalar\Okyanus\Matematik\kutuphane_CBJBZ8AV.exe"])
            elif "VIP" in yayıncılık:
                speak("which lesson do you want to study")
                ders4 = Komutal()
                if ders4 in biyoloji:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Biyoloji\kutuphane_MBBCRYBN.exe")
                elif ders4 in coğrafya:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Coğrafya\kutuphane_8AA8DFAV.exe")
                elif ders4 in edebiyat:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Edebiyat\Edebiyat.exe")
                elif ders4 in felsefe:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Felsefe\Felsefe.exe")
                elif ders4 in fizik:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Fizik\Fizik.exe")
                elif ders4 in kimya:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Kimya\Kimya.exe")
                elif ders4 in matematik:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Matematik\Matematik.exe")
                elif ders4 in tarih:
                    speak("Have good lessons sir")
                    subprocess.call(r"A:\!!!!!\Her Şey\Uygulamalar\VİP yayınları\Tarih\Tarih.exe")
            elif "paraf" in yayıncılık or "Paraf" in yayıncılık or "haram" in yayıncılık:
                speak("Which lesson do you want to study")
                ders5 = Komutal()
                if ders5 in biyoloji:
                    speak("Have good lessons")
                    subprocess(r"A:\!!!!!\Her Şey\Uygulamalar\PRF\biyoloji\kutuphane_2DAV5KBC.exe")
                if ders5 in matematik:
                    speak("Have good lessons")
                    subprocess(r"A:\!!!!!\Her Şey\Uygulamalar\PRF\matematik\kutuphane_MCAR52AT.exe")
                if ders5 in fizik:
                    speak("Have good lessons")
                    subprocess(r"A:\!!!!!\Her Şey\Uygulamalar\PRF\Fizik\kutuphane_SGA76NAH.exe")
               








































