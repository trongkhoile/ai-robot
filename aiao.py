import pyttsx3
import speech_recognition
from datetime import date

        
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
        print("Robot:I'm Listening")
        audio= robot_ear.listen(mic)
print("...")
try:
  you = robot_ear.recognize_google(audio)
except:
  you=""

print("You:",you)   

if "hello" in you :
        robot_brain="hello my friend"
elif "how are you" in you:
        robot_brain="i'm fine and you"
elif "my name" in you:
        robot_brain="Khoi"
elif "your name" in you:
        robot_brain="my name is Ray"   
elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
elif "wow" in you:
        robot_brain="thank you" 
elif "bye" in you:
        robot_brain="bye my friend"
        print(robot_brain)
        engine = pyttsx3.init()
        engine.say(robot_brain)
        engine.runAndWait()
       
else :
        robot_brain="i can't hear you"    
print(robot_brain)
engine = pyttsx3.init()
engine.say(robot_brain)
engine.runAndWait()
               





   