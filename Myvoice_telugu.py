!pip install gtts
!pip install playsound==1.2.2
from gtts import gTTS  
from playsound import playsound   
your_text = 'Na peru karthik. Idhi Na gonthu kaadhu'  
language = 'te'  
obj = gTTS(text=your_text, lang=language, slow=False)   
obj.save("Telugu_k.mp3")  
playsound("Telugu_k.mp3")  