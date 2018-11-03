def BMI():
    # get weight
    while True:
        weight = input("Enter your weight in pounds (no decimals): ")
        if not weight.isdigit():
            print("That is not a valid number. Please try again.")
            continue
        else:
            weight = int(weight)
            break
    
    # get height
    while True:
        height = input("Enter your weight in inches (no decimals): ")
        if not height.isdigit():
            print("That is not a valid number. Please try again.")
            continue
        else:
            height = int(height)
            break

    bmi = 703 * weight / height**2
    print("Your BMI is: {:.1f}".format(bmi))

    # check if over/under weight
    if bmi < 18.5:
        print("You are underweight")
    elif bmi >= 30:
        print("You are obese")
    elif bmi > 25:
        print("You are overweight")
    else:
        print("That is a normal weight")

def CtoF():
    while True:
        degreesC = input("Enter the temperature in degrees 'C: ")
        if not degreesC.isnumeric():
            print("That is not a valid number. Please try again.")
            continue
        else:
            degreesC = int(degreesC)
            break
    degreesF = 32 + 9/5*degreesC
    print("The temperature is {:.1f}'F".format(degreesF))


def feet2inches():
    while True:
        feet = input("Enter your measurement in feet (no decimals): ")
        if not feet.isdigit():
            print("That is not a valid number. Please try again.")
            continue
        else:
            feet = int(feet)
            break
    inches = feet * 12
    print("{} feet is equal to {} inches.".format(feet,inches))



if __name__ == '__main__':
    option = ''
    menu = {"BMI":"Body Mass Index",'CTF':"Celsius to Fahrenheit",'FTI':"Feet to Inches",'q':"Quit"}
    menuoptions = {"BMI":BMI,'CTF':CtoF,'FTI':feet2inches,'q':quit}
    while (option + ' ')[0].lower()!='q':
        print("\n\n")
        print("Please enter your choice. Valid options are:")
        for calc in menuoptions.keys():
            print("{}:\t{}".format(calc.upper(),menu[calc]))
        option = input("(or 'q' to quit) --> ")
        if option.upper() not in menuoptions.keys():
            print("That was not a valid choice. Please try again.\n\n")
            continue

        menuoptions[option.upper()]()