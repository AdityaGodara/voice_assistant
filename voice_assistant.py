import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

from traitlets import This

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....!")
        #for noice cancellation
        recognizer.adjust_for_ambient_noise(source)
        audio= recognizer.listen(source)
        try:
            print("reconizing...")
            data= recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("cant understand")

def speechtx(x):
    engine= pyttsx3.init()#class
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    #0==male voice& 1== female voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)#voice speed
    engine.say(x)
    engine.runAndWait()
if __name__ == '__main__':#program will split
    if "alexa" in sptext().lower():
        speechtx("initializinng alexa")
        while(True):
            data1=sptext().lower()

            if "your name" in data1:
             name= "my name is alexa"
             speechtx(name)

            elif "old are you" in data1:
             age="i am 2 years old"
             speechtx(age)

            elif "time" in data1:
             time=datetime.datetime.now()
             speechtx(time)

            elif "youtube" in data1:
             url=input("enter the  url")
             webbrowser.open(url)

            elif "open a website" in data1:
             url=input("enter url of webpage")
             webbrowser.open(url)

            elif "joke" in data1:
              joke_1=pyjokes.get_joke(language="en",category="neutral")
              print(joke_1)
              speechtx(joke_1)

            elif "clock" in data1:
               speechtx("opening clock")
               from tkinter import *
               import datetime

               def date_time():
                time=datetime.datetime.now()#stores exact time
                hr=time.strftime('%I')
                mi=time.strftime('%M')
                sec=time.strftime('%S')
                am=time.strftime('%p')

                date=time.strftime("%d")
                month=time.strftime('%m')
                year=time.strftime('%y')
                day=time.strftime('%a')
                lab_hr.config(text=hr)
                lab_min.config(text=mi)
                lab_sec.config(text=sec)
                lab_am.config(text=am)
                lab_date.config(text=date)
                lab_mo.config(text=month)
                lab_year.config(text=year)
                lab_day.config(text=day)
                lab_hr.after(200,date_time)#to change the time automatically, after 200 milisec
   
               clock= Tk()

               clock.title("****DIGITAL CLOCK****")
               clock.geometry('1000x500')
               clock.config(bg="yellow")#configuration dega

                ###time###

               lab_hr=Label(clock,text="00",font=('Times New Roman',60,'bold'),bg="Red",fg="White")
               lab_hr.place(x=120,y=50,height=110,width=100)

               lab_hr_txt=Label(clock,text="Hours",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_hr_txt.place(x=120,y=190,height=40,width=100)

               lab_min=Label(clock,text="00",font=('Times New Roman',60,'bold'),bg="Red",fg="White")
               lab_min.place(x=340,y=50,height=110,width=100)

               lab_min_txt=Label(clock,text="Min",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_min_txt.place(x=340,y=190,height=40,width=100)

               lab_sec=Label(clock,text="00",font=('Times New Roman',60,'bold'),bg="Red",fg="White")
               lab_sec.place(x=560,y=50,height=110,width=100)

               lab_sec_txt=Label(clock,text="Sec",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_sec_txt.place(x=560,y=190,height=40,width=100)

               lab_am=Label(clock,text="00",font=('Times New Roman',50,'bold'),bg="Red",fg="White")
               lab_am.place(x=780,y=50,height=110,width=100)

               lab_am_txt=Label(clock,text="Am/Pm",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_am_txt.place(x=780,y=190,height=40,width=100)

                 ###date###

               lab_date=Label(clock,text="00",font=('Times New Roman',60,'bold'),bg="Red",fg="White")
               lab_date.place(x=120,y=270,height=110,width=100)

               lab_date_txt=Label(clock,text="Date",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_date_txt.place(x=120,y=410,height=40,width=100)

               lab_mo=Label(clock,text="00",font=('Times New Roman',60,'bold'),bg="Red",fg="White")
               lab_mo.place(x=340,y=270,height=110,width=100)

               lab_mo_txt=Label(clock,text="Month",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_mo_txt.place(x=340,y=410,height=40,width=100)

               lab_year=Label(clock,text="00",font=('Times New Roman',60,'bold'),bg="Red",fg="White")
               lab_year.place(x=560,y=270,height=110,width=100)

               lab_year_txt=Label(clock,text="Year",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_year_txt.place(x=560,y=410,height=40,width=100)

               lab_day=Label(clock,text="00",font=('Times New Roman',35,'bold'),bg="Red",fg="White")
               lab_day.place(x=780,y=270,height=110,width=100)

               lab_day_txt=Label(clock,text="Day",font=('Times New Roman',20,'bold'),bg="Red",fg="White")
               lab_day_txt.place(x=780,y=410,height=40,width=100)

               date_time()

               clock.mainloop()
            

            elif "record screen" in data1:
               import cv2
               import pyautogui
               from win32api import GetSystemMetrics
               import numpy as np
               import time

               width= GetSystemMetrics(0)#width 0 se strt krega
               height= GetSystemMetrics(1)
               dim=(width,height)
 
               f=cv2.VideoWriter_fourcc(*"mp4v")

               output=cv2.VideoWriter("test.mp4",f,30.0,dim)#change location in this also, 30 is frames per second

               now_start_time=time.time()
               dur=10+4 #duration , +4 is for code compile timme
               end_time=now_start_time + dur
               speechtx("recording started")

               while True:
                image=pyautogui.screenshot()#screenshot capture
                frame_1=np.array(image)#collect all images
                frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

                output.write(frame)
    
                c_time=time.time()#for current time

                if c_time > end_time:
                 break

               output.release()
               speechtx("recording stopped")

               print("___end__")
               elif "exit" in data1:
               speechtx("thank you")
               break
    else:
       print("say again")
