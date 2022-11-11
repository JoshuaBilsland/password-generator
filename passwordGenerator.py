def displayMenu():
    print("\n***** Menu *****")
    print("1 - Add New Entry")
    print("2 - Save Entries to a Text File")
    print("3 - Close the Program")
    print("******************")

def getMenuChoice():
    return int(input("Enter Menu Choice Using the Related Number: "))

def displayError(errorDescription):
    errorBorder = "\n*************************************************\n"
    print(errorBorder + "ERROR - " + errorDescription + errorBorder)
    

# Main
entriesList = [] # 2D list of all the entries the user has made
running = True

while running:
    displayMenu()
    userChoice = getMenuChoice()
    
    if userChoice == 1:
        print(1)
    elif userChoice == 2:
        print(2)
    elif userChoice == 3:
        confirm = input("Are You Sure You Want To Close The Program (Y/N): ")
        if confirm == "Y":
            running = False
    else:
        displayError("Please Only Enter an Number From the Available Menu Choices")

