#this is an online mechanic it allows a user to find what the problem with their car might be

print("Welcome to Halfords online mechanic service.")
print('changes made')

file = open("diagnose.txt","r")
issue=input("What is your automobile related issue")
#call variable word in the for loop
for word in issue:
    if "Battery" in issue:
        lines=file.readlines()
        print (lines[0])
        file.close()
        break    #break is so for loop does not come up more than once
for word in issue:
    if "Keys" in issue:
        lines=file.readlines()
        print (lines[1]) #python index
        file.close()
        break
for word in issue:
    if "Tyre" in issue:
        lines=file.readlines() #as long as you got a txt file open at the top you dont need to open it again
        print (lines[2])
        file.close()
        break
for word in issue:
    if "Fuel" in issue:
        lines=file.readlines()
        print (lines[3])
        file.close()
        break
for word in issue:
    if "Clutch" in issue:
        lines=file.readlines()
        print (lines[4])
        file.close()
        break
else:
    print("We can't do that at the moment please contact our helpline")
          
