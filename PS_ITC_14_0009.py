## Template
#!/usr/bin/env python3

# Name: <Edward Nathan Larbi>
# Index number: <PS_ITC_14_0009>

# TODO: Put your codes here ...

#question 1:

#Creates a variable called line 
line = ""

#Iterate through a number of range from 1000 to 7000
for numbers in range(1000, 7001):
    #Check if numbers is divisible by 7 and not a multiple of 5
    if(numbers % 7 == 0) and (numbers % 5 != 0):
        #Stores Everything on in line variable with comma-sepated
        line += str(numbers) + ", " 
#Prints the line variable
print (line)



#QUESTION 2:

total = 0

for numbers in range(2000):
    if(numbers % 3 == 0) or (numbers % 5 == 0):
        total += numbers

print (total)

#QUESTION3

decimal_value = int(input("Please enter a value: "));          


print ('{0:b}'.format(int(decimal_value)))

raw_input('Press enter to end!')


#QUESTION 4

def fibbonachi():
    sumTotal = 0
    term1 = 1
    term2 = 2
    count = 1


    while True:

        tempTerm = term1 + term2
        term1 = term2
        term2 = tempTerm
        count += 1

        
        if (term1 % 2 == 0):
            sumTotal += term1

        

        if term2 > 4000000:
            break
        
    return sumTotal



print (fibbonachi())


#QUESTION:5a

my_input = "0123456789"
Zero = ["****** ", "*    * ", "*    * ", "*    * " , "*    * " , "*    * " , "****** "]
One = ["*      ","*      ","*      ","*      ","*      ","*      ","*      "]
Two = ["****** ", "     * ","     * ", "****** ", "*      ","*      ", "****** "]
Three = ["****** ", "     * ","     * ", "****** ", "     * ","     * ", "****** "]
Four = ["*    * ", "*    * ","*    * " ,  "****** ", "     * ","     * ","     * "]
Five = ["****** ", "*      ","*      " , "****** ", "     * ", "     * ", "****** "]
Six = ["****** ", "*      ","*      " , "****** ", "*    * ", "*    * ", "****** "]
Seven = ["****** ","     * " , "     * ", "     * ", "     * ", "     * ", "     * "]
Eight = ["****** ", "*    * ", "*    * ", "****** ", "*    * " , "*    * " , "****** "]
Nine = ["****** ", "*    * ", "*    * ", "****** ", "     * " , "     * " , "****** "]

Digits = [Two, Three, Four, Five, Six, Seven, Eight, Nine, Zero, One]

# TODO: Print all the digits on the same line
try:
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(my_input):
            # TODO: Put your code after this comment
            
            line += Digits[column][row]            
            column += 1
            
        # TODO: Print line here and add an incrementer
        print (line)
        row += 1   
except:
    # TODO: Handle one suitable error which may occur
    pass



#QUESTION5b:


my_input = "0123456789"
Zero = ["****** ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * " , "*    * " , "*    * " , "****** "]
One = ["*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      "]
Two = ["****** ", "     * ","     * ", "     * ","     * ", "****** ","*      ","*      ","*      ","*      ", "****** "]
Three = ["****** ", "     * ","     * ","     * ","     * ", "****** ", "     * ","     * ","     * ","     * ", "****** "]
Four = ["*    * ", "*    * ","*    * " , "*    * " ,"*    * " ,  "****** ", "     * ","     * ", "     * ","     * ","     * ","     * ","     * "]
Five = ["****** ", "*      ","*      " ,"*      " ,"*      " , "****** ", "     * ", "     * ","     * ","     * ", "****** "]
Six = ["****** ", "*      ","*      " ,"*      " ,"*      " , "****** ", "*    * ", "*    * ","*    * ","*    * ", "****** "]
Seven = ["****** ","     * " , "     * ", "     * ", "     * ", "     * ","     * ","     * ","     * ","     * ", "     * "]
Eight = ["****** ", "*    * ", "*    * ","*    * ","*    * ", "****** ", "*    * " , "*    * " ,"*    * " ,"*    * " , "****** "]
Nine = ["****** ", "*    * ", "*    * ", "*    * ","*    * ", "****** ", "     * " ,"     * " ,"     * " , "     * " , "****** "]

Digits = [Two, Three, Four, Five, Six, Seven, Eight, Nine, Zero, One]

# TODO: Print all the digits on the same line
try:
    row = 0
    while row < 11:
        line = ""
        column = 0
        while column < len(my_input):
            # TODO: Put your code after this comment
            
            line += Digits[column][row]            
            column += 1
            
        # TODO: Print line here and add an incrementer
        print (line)
        row += 1   
except:
    # TODO: Handle one suitable error which may occur
    pass



















