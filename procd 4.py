#CONVERT BINARY NUMBER TO DECIMAL AND VICE-VERSA
print(" For Decimal to Binary...Press 1.")
print(" For Binary to Decimal... Press 2")
my_choice=int(input("Enter your choice: "))
if my_choice==1:
 i=1
s=0
my_dec=int(input("Enter decimal to be converted: "))
while my_dec>0:
   rem=int(my_dec%2)
   s=s+(i*rem)
   my_dec=int(my_dec/2)
   i=i*10
   print ("The binary of the given number is ",s,'.')
else:
   my_bin=input ('Enter binary to be converted: ')
   n=len(my_bin)
   res=0
for i in range(1,n+1):
   res=res+ int(my_bin[i-1])*2**(n-i)
print ("The decimal of the given binary is ",res,'.')
#code by ayush saxena