def pattern_rtriangle(num):
    curr_num = (num * (num+1) // 2) + 1
    counter = 1
    temp=1
    
    for i in range(num):
        for j in range(i):
            #if num will be even than this part will execute 
            if(num%2==0):
                if((1<i<=num-1 and j==i-1)):
                    print(counter+num,"",end="")
                    counter+=1

                elif(1<i<=num-1 and j==i-2):
                    print(num-counter,"",end="")

                elif(i==num-1 and j==0):
                    print("1 ",end="") 
                else:
                    print(num,"",end="")    

            #if num will be odd than this part will execute 
            else:
                if((1<i<=num-1 and j==i-1)):
                    print(counter+num+2,"",end="")
                    counter+=1

                elif(1<i<=num-1 and j==i-2):
                    print(num+temp,"",end="")
                    temp-=1

                
                elif(1<i<=num-1 and j==i-3):
                    print(num-counter,"",end="")
                
                elif(i==num-1 and j==0):
                    print("1 ",end="") 
                else:
                    print(num+2,"",end="")     
        curr_num-=1
        print(curr_num)

pattern_rtriangle(4)
print()
pattern_rtriangle(5)
