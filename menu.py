#This is a throwaway CLI interface prototype.
def getMenuResponse(items):
    response = int(input('Choose and option [1-' + str(items) + ']: '))
    if response in range(1,items+1):
        return response
    else:
        print("Item not in range. Please try again.")
        return getMenuResponse(items)

def subMenu():
    print("This is a sub menu. What would you like to do?")
    print("1. Go back")
    print("2. What's 1+1?")
    response = getMenuResponse(2)
    if response == 1:
        return 0
    else:
        print("It's 2.")
    subMenu()

def mainMenu():
    print("Welcome to a test menu. What would you like to do?")
    print("1. Say hi")
    print("2. Say bye (and quit)")
    print("3. More...")
    response = getMenuResponse(3)
    if response == 1:
        print("Hi there.")
    elif response == 2:
        print("Goodbye")
        return 0
    else:
        subMenu()
    mainMenu()

if __name__ == '__main__':
    mainMenu()