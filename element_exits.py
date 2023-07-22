n=int(input("enter the element"))
b=[1,3,5,6,8]
i=0
while i<len(b):
	if b[i]==n:
		print("yes")
		break
	else:
		print("no")
	i=i+1	
	
	
def convertDecimalToBinary(x):
    
    if x > 1:
        convertDecimalToBinary(x // 2)
    print(x % 2, end='')


# Get user input
num = int(input("Enter a decimal number: "))

convertDecimalToBinary(num)
