def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    #Find Minimum
    minval = num1
    if(num2<minval):
        minval = num2
    if(num3<minval):
        minval = num3
    
    #Find Maximum
    maxval = num1
    if(num2>maxval):
        maxval = num2
    if(num3>maxval):
        maxval = num3
    
    #Set Median
    if(num1!=minval and num1!=maxval):
        median = num1
    elif(num2!=minval and num2!=maxval):
        median = num2
    elif(num3!=minval and num3!=maxval):
        median = num3
    else:
        median = num1

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
