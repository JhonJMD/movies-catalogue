# Import necessary modules
from tabulate import tabulate
import modules.files as FILE
import modules.screen as SCREEN
import modules.reusable as VAL

# Check if the file 'genre.json' exists
FILE.checkFile('genre.json')
# Read the content of 'genre.json' and store it in the variable 'data'
data = FILE.readFile('genre.json')

# Function to add a genre
def addGenre():
    isAddGenre = True
    while isAddGenre:
        SCREEN.cleanScreen() # Clear the console screen
        # Dictionary to store genre information
        genre = {
            "id": "",
            "name": "",
            "description": ""
        } 
        # Input genre information into the dictionary
        while True: # Loop to check if the ID is unique
            SCREEN.cleanScreen()
            # Validate and input the genre's ID
            genre["id"] = VAL.validationNumbers("Genre's ID: ")
            # Check if the ID is already registered
            if str(genre['id']) in data.keys():
                SCREEN.cleanScreen()
                print('This ID is already registered')
                SCREEN.pauseScreen()
            else:
                break
        genre["name"] = str(input("Genre's name: ")) # Input genre's name
        genre["description"] = str(input("Description of the genre: ")) # Input genre's description
        SCREEN.cleanScreen()
        # Update data with the new genre
        data.update({genre["id"]:genre})
        # Update the 'genre.json' file with the new data
        FILE.updateFile('genre.json', data)
        # Ask user if they want to enter another genre
        isAddGenre = VAL.validationOtherInput('Do you want to enter another genre? (Yes(S) -- Enter(No)): ')

# Function to list all genres
def listGenre():
    SCREEN.cleanScreen() # Clear the console screen
    kys = ['ID','NAME','DESCRIPTION'] # Define column headers
    rows = [] # Initialize a list to store rows of genre data
    for key, value in data.items(): # Loop through each genre in the data
        row = [value["id"], value["name"], value["description"]] # Create a row with genre information
        rows.append(row) # Add the row to the list of rows
    # Print the genre data in a formatted table
    print(tabulate(rows, headers=kys, tablefmt='fancy_grid'))
    SCREEN.pauseScreen() # Pause the screen for user interaction
