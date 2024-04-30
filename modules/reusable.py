import modules.screen as SCREEN

#Function for validation data input
def validationNumbers(message : str):
    while True: #Cycle to repeat try until a valid data is entered
        try:
            num = int(input(message))
        except ValueError:
            SCREEN.cleanScreen()
            print('Data input wrong')
            SCREEN.pauseScreen()
            SCREEN.cleanScreen()
        else:
            return num

#Function for validation if the user want input another input
def validationOtherInput(message : str):
    while True:
        SCREEN.cleanScreen()
        answer = input(message)
        if answer == ('S' or 's'):
            return True
        elif (answer == ''):
            return False
            
