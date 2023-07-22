
n=int(input("enter the HCF "))
m=int(input("enter the Hcf"))
if m>n:
	f=m
else:
	f=n
i=1
while i<f+1:
	if m%i==0 and n%i==0:
		h=i
	i=i+1
print(h)

