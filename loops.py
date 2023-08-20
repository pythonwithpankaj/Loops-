#n=int(input("enter a number:"))
#i=1
#while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=1


#factors -- completly divisible number

#12 -- 1,2,3,4,6,12

# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     if n%i==0:
#        print(i,end=" ")
#     i+=1


###To check a number is prime or not

# n=int(input("enter a number: "))
# i=2
# count=0
# while i<n:
#     if n%i==0:
#        count+=1
#     i+=1
# 
# if count==0:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")   

#1,2,3,4,5,6,7,8,9,10
# s=1
# i=1
# while i<=10:
#     s=s*i
#     i+=1
# 
# print("Multiply=",s) 


# n=int(input("enter a number:"))
# f=1
# while n>=1:
#     f=f*n
#     n-=1
# print("factorial=",f)  

##HCF (GCD)
#8 - 1,2,3,4,8
#12 - 1,2,3,4,6,12

##LCM
#8 - 8,16,24,32,40,48.......
#12 - 12,24 36 48.......

# n1=int(input("enter number1="))
# n2=int(input("enter number2="))

        # i=1
        # while i<=n1:
        #     if n1%i==0 and n2%i==0:
        #         hcf=1
        #     i+=1
        # print("HCF:",hcf) 
         
        # lcm=(n1*n2)//hcf
         
        # print("LCM:",lcm)


###break -- break the loop during loop iteration
   # i=1
   # while i<=50:
   #     print(i)
   #     if i%8==0:
   #         break
   #     i+=1

###continue -- skip the loop iteration  during loop iteration

# i=1
# while i<=50:
#     i+=1
#     if i%5==0:
#         continue
#     print(i)   


### find the sum of 10 user input data
# s=0
# i=1
# while i<=10:
#     i+=1
#     n=int(input("enter number:"))
#     if n<0:
#         continue
#     s=s+n
 
# print("Sum=",s)


### else block in loop
 # i=1
 # while i<=10:
 #     print("hello python")
 #     if i==6:
 #         break
 #     i+=1
 # else: 
 #     print("Done") 

   # n=int(input("enter a number:"))
   # i=2
   #  while i<n:
   #      if n%i==0:
   #          print(n,"is not a prime number")
   #          break
   #      i+=1
   #  else:
   #      print(n,"is a prime number")


### Nested loop

  # i=1
  # while i<=3:
  #     j=1
  #     while j<=3:
  #         print("i=",i,"j=",j)
  #         j+=1
  #     i+=1    
