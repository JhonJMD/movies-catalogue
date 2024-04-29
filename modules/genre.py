import files as FILE
import screen as SCREEN 

def addGenre():
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
    genre["id"] = str(input("Genre's ID: "))
    genre["name"] = str(input("Genre's name: "))
    genre["description"] = str(input("Description the genre:"))
    SCREEN.cleanScreen()
    genreToUpdate = {genre["id"]:genre}
    FILE.updateFile('genre.json',genreToUpdate)

addGenre()