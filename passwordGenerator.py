import random

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

    
def generateRandomLowercaseLetter():
    return chr(random.randint(ord("a"),ord("z")))


def generateRandomUppercaseLetter():
    return chr(random.randint(ord("A"),ord("Z")))


def generateNumberOrSymbol():
    return chr(random.randint(33,64))


def generatePassword(passwordLength):
    # Store the randomly generated characters
    lowercaseLetters = []
    uppercaseLetters = []
    symbolsAndNumbers = []
    
    # Generate the random characters
    for currentChar in range(passwordLength): 
        if currentChar < passwordLength // 3: # Third of the password will be lowercase letters
            lowercaseLetters.append(generateRandomLowercaseLetter())
        elif currentChar > passwordLength // 3 and currentChar <= (passwordLength //3) * 2: # Another third will be uppercase letters
            uppercaseLetters.append(generateRandomUppercaseLetter())
        else: # The last third will be symbols and numbers
            symbolsAndNumbers.append(generateNumberOrSymbol())

    # Assemble password
    passwordCharList = lowercaseLetters + uppercaseLetters + symbolsAndNumbers
    random.shuffle(passwordCharList) # Shuffle all the generated characters to make the password
    return ''.join(passwordCharList) # Turn list values into a string which will be the password 

        
def newEntry(passwordLength):
    entryDescription = input("What is the username and password for? : ")
    entryUsername = input("What is the username for the account? : ")
    entryPassword = generatePassword(passwordLength)
    
    entry = []
    entry.append(entryDescription)
    entry.append(entryUsername)
    entry.append(entryPassword)
    
    return entry


def saveEntriesToTextFile(entriesList):
    # Create file
    fileCreated = False
    fileName = "entries"
    counter = 0 # Number to add to end of fileName
    while not fileCreated:
        try:
            if counter == 0:
                file = open(fileName+".txt", "x")
            else:
                file = open(fileName+str(counter)+".txt","x")
        except FileExistsError:
            counter += 1
        else:
            fileCreated = True
            print(file.name)
    
    # Write to file
    if counter == 0:
        file = open(fileName+".txt","w")
    else:
        file = open(fileName+str(counter)+".txt","w")
    
    entryNumber = 1 # used to number each entry that is written
    for entry in entriesList:
        file.write("ENTRY "+str(entryNumber)+" -> | ") # Number the entry that is to be written
        for data in entry:
            file.write(data)
            file.write(" | ") # separate each part of the entry
        file.write("\n\n") # New line + empty space between each entry
        entryNumber += 1
        
    file.close()    
    
        

# Main
entriesList = [] # 2D list of all the entries the user has made
running = True

while running:
    displayMenu()
    userChoice = getMenuChoice()
    
    if userChoice == 1: # Add new entry
        entriesList.append(newEntry(15))
        print(entriesList)
    elif userChoice == 2: # Save entries to text file
        saveEntriesToTextFile(entriesList)
    elif userChoice == 3: # Exit program
        confirm = input("Are You Sure You Want To Close The Program (Y/N): ")
        if confirm == "Y":
            running = False
    else: # Invalid input
        displayError("Please Only Enter an Number From the Available Menu Choices")

