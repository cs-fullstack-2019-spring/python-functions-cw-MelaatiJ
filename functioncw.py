def main():   #creating my main function with my problems inside
    # problem1()
    # problem2()
    # problem3()
    problem4()


def problem1():
    counttoNumber(54)  #calling my function and the number i input will print 0 to the number

def counttoNumber(x):   #my function for the counting
    for x in range(0, x+1):  #for each loop to iterate each number
        print(x)



    # Create a function in your program that counts from 0 to [NUMBER]

def problem2():
    somethingaboutYou()       #calling the function


def somethingaboutYou():
    userinput = ""      #setting an empty string to my variable
    while userinput.lower() != "quit":
        userinput = input("Tell me a little bit about yourself. When you start to get boring enter 'quit' to stop\n")

# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.


def problem3():
    print(addFunction(3, 5))       #calling each function under my problem 3
    print(subtractFunction(3, 5))
    print(multiplyFunction(3, 5))
    print(divideFunction(3, 5))


def addFunction(x, y):                  #this function will return addition of the two numbers
    return x + y


def subtractFunction(x, y):                    #this function return subtraction of the two numbers
    return x - y


def multiplyFunction(x, y):                  #this function multiplies the two numbers
    return x * y


def divideFunction(x, y):                             #this function divides the two numbers
    return x / y

# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.



def problem4():
    userNumberFunction()    # calling my usernumber function with the saved var

def userNumberFunction():
    userNumberone = int(input("Enter a number\n"))              # asking for the first number
    userNumbertwo = int(input("Enter another number\n"))            # asking for the second number
    print(userOperation(userNumberone, userNumbertwo))                       #calling my bottom function useroperation

def userOperation(userNumberone, userNumbertwo):
    userOperationinput= input("Enter if you want to 'add','subtract','multiply', divide\n")
    if userOperationinput.lower() == "add":
        return (f"{userNumberone} + {userNumbertwo} = {userNumberone + userNumbertwo}")
    elif userOperationinput.lower() == "subtract":
        return (f"{userNumberone} - {userNumbertwo} = {userNumberone - userNumbertwo}")
    elif userOperationinput.lower() == "multipYYly":
        return (f"{userNumberone} * {userNumbertwo} = {userNumberone * userNumbertwo}")
    elif userOperationinput.lower() == "divide":
        return (f"{userNumberone} / {userNumbertwo} = {userNumberone / userNumbertwo}")

    # Create a function that will ask the user for a number.
    #     Use the function to get two numbers,
    #     then pass the two numbers to a function and ask a user if they want to add, subtract, multiple, or divide them.
    #     Return a string that prints the two numbers, which operation it did, and the result.















if __name__ == '__main__':
    main()
