from gpiozero import LED
import RPi.GPIO
from guizero import App, Text, TextBox, PushButton
from time import sleep
RPi.GPIO.setmode(RPi.GPIO.BCM)

## PIN ##

blueLed = LED(21)

##  1 unit = 1 second
##  . (dot) = 1u
##  - (dash) = 3u
##  between components of the same letter = 1u
##  between letters of the word = 3u


## DICTIONARY - dot / dash representation for each aplhabet letter, as a string ##

dict = {'a' : '.-' ,
        'b' : '-...' ,
        'c' : '-.-.' ,
        'd' : '-..' ,
        'e' : '.' ,
        'f' : '..-.' ,
        'g' : '--.' ,
        'h' : '....' ,
        'i' : '..' ,
        'j' : '.---' ,
        'k' : '-.-' ,
        'l' : '.-..' ,
        'm' : '--' ,
        'n' : '-.' ,
        'o' : '---' ,
        'p' : '.--.' ,
        'q' : '--.-' ,
        'r' : '.-.' ,
        's' : '...' ,
        't' : '-' ,
        'u' : '..-' ,
        'v' : '...-' ,
        'w' : '.--' ,
        'x' : '-..-' ,
        'y' : '-.--' ,
        'z' : '--..',
        ' ' : '-'      ## in case we have 2 words ##
        ## because space and dash are same length -> 3u ##
        }
        
## FUNCTIONS ##



def dot():
    blueLed.on()
    sleep(1)          ## 1u is a dot ##
    blueLed.off()
    sleep(1)          ## 1u between components of the same letter , because after this line next letter will be executed ##
    
def dash():
    blueLed.on()
    sleep(3)     ## 3u is a dash ##
    blueLed.off
    sleep(1)     ## 1u between components of the same letter ##
    
    

def Convert():
    text = userInput.value
    #button = text[0:12]
    #code = [dict[lower()]]
    #morse = ' '.join(code)   ## we want to break the input string so that there is space ' ' between each letter ## 
    
    if len(text) <13:  ## max 12 characters ##
        for letter in text:
            
            for dotORdash in dict[letter.lower()]:
                if dotORdash=='.' :
                    dot()  
        
                elif dotORdash == '-' :
                    dash()
            
            sleep(3)     ## space between letters -> 3u
        execution.value= "success"
        
    blueLed.off()  ## to know when the execution ends
    if len(text)>12:
        execution.value = "failure"

def Reset():
    execution.value = "           "
        
## GUI ##

app = App(title = "CONVERTER program",bg="wheat", height = 250)     ## app = main window containing all other widgets ##
intro = Text(app, text = "enter a word",size=45, bg = "salmon")
userInput = TextBox(app,width = 20)
execution = Text(app, text = "           ",size = 20, bg = "bisque3")
button = PushButton(app, text = "enter" ,command = Convert)
button2 = PushButton(app, text = "reset" ,command = Reset)



app.display() 