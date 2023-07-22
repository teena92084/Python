N=int(input("enter the number"))
i=1
d=[]
while i<=N:
	j=1
	c=0
	while j<=i:
		if i%j==0:
			c=c+1
		j=j+1
	if c==2:
		print("prime",i)
	i=i+1		
	
	
	
	
 
