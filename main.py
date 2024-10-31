askstring = "what you want : \n 1. set timer \n 2. see all timers you put \n 3. exit" # writting the option

print(askstring) # printing them

ask = input("enter the number: ") # ask which one 

# time codes
def starttimer():
    
    import time # import time
    Mtimer = input("enter your timer (m): ") # to get the minit 
    Stimer = input("enter your timer (s): ") # to get the second 
    
    for s in range(int(Stimer) + 1): # making a for loop for second  and making Stimer as s
        
        time.sleep(int(Stimer)) # sleep as the value of (Stimer) if Stimer == 4 : sleep(4s)
     
    if s == int(Stimer) : #  when the second is finished the timer will start with minit
        
        print("the second is finished") # note the user that the second is finished 
        
        for m in range(int(Mtimer) + 1): # making a for loop for minit  and making Mtimer as s
            
         if Mtimer == "": # checking that the minit does not equal to string 
             
            print("you cant put a string ") # print a note that the input contain string not integer
            
         else :  # if the Mtimer != "" :
         
          time.sleep(int(Mtimer) * 60) # sleep as the input value exmple: Mtimer == 1 (1 * 60)
          
    if s == int(Stimer) and m == int(Mtimer): # when the s == stimer and m == mtimer :
          with open("History.txt","a") as f : # openning a page named history.txt 
              a = f.write(f" \n {int(Mtimer)}m : {int(Stimer)}s / time set: [{time.ctime()}] \n ") # adding the timer to a page named history.txt 
          print("the timer is finished") # telling that the timer is finished
# history codes
def history():
    with open("History.txt","r") as f : # openning a file named history.txt
        if f.readable() == True: # checking if the file is readable()
            a = f.read() # getting the data from the file
            print(a) # print them
        else:  # if the file is not readable
            print("the file is not readable") # print that there is an errore
    
# if ask input eqaul one then the starttimer func will start to put a timer
if ask == "1":
    starttimer()
# if ask input eqaul one then the history func will get all the timer that the user put 
elif ask == "2":
    history()
# if ask doesnt eqal 1 or 2 then he will equit
else:
    pass