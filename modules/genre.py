import modules.files as FILE
import modules.screen as SCREEN
import modules.reusable as VAL 

def addGenre():
    isAddGenre = True
    while isAddGenre:
        SCREEN.cleanScreen() #Clean console
        FILE.checkFile('genre.json') #Check that file is create
        data = FILE.readFile('genre.json') #Save the content of the json into new variable
        # Dictionary of Genre
        genre = {
            "id": "",
            "name": "",
            "description": ""
        } 
        #Input the information into dictionary
        while True: #Cycle to check if the ID is repeated or not
            SCREEN.cleanScreen()
            genre["id"] = VAL.validationNumbers("Genre's ID: ")
            if str(genre['id']) in data.keys():
                SCREEN.cleanScreen()
                print('This ID is already registered')
                SCREEN.pauseScreen()
            else:
                break
        genre["name"] = str(input("Genre's name: "))
        genre["description"] = str(input("Description the genre: "))
        SCREEN.cleanScreen()
        data.update({genre["id"]:genre})
        FILE.updateFile('genre.json',data)
        isAddGenre = VAL.validationOtherInput('You want to enter another genre? (Yes(S) -- Enter(No)): ')