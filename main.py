import speech_recognition as sr 
r = sr.Recognizer()  
while(1):     
    try: 
        r.adjust_for_ambient_noise(source2, duration=0.5) 
        audio2 = r.listen(source2) 
        MyText = r.recognize_google(audio2) 
        MyText = MyText.lower() 

        print(MyText) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 
