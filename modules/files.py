import screen as scr 
import os
import json

BASE = 'DATA/'

# Checks if the json file exists and if it doesn't creates it
# Receive: json file's name
def checkFile(file:str):
    if not os.path.isfile(BASE+file): # Checks if json file exists in DATA folder
        with open(BASE+file, 'w') as createFile: 
            json.dump({}, createFile, indent = 4) #Creates json file with an empty object
    else:
        return False

    
# Reads json file and loads it into a python dict
# Receive: json file's name
# Returns: Json file's content
def readFile(file:str):
    with open (BASE+file, 'r') as readFile: # Open json files and store it in a variable
        return json.load(readFile)  
    

# Updates json file with the given content
# Receive: json file's name
#          content to update the file
def updateFile(file:str, content):
    with open(BASE+file, 'w+') as updateFile: # Open json files and store it in a variable
        json.dump(content, updateFile, indent = 4)