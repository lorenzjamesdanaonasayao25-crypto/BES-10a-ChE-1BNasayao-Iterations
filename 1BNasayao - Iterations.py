#This project is a tracker that keeps a list of lab inventory and calculates the total sum of items washed.
#As a first year ChE Student, cleaning up and doing inventory of the apparatus used is a common and important task.

inyou = input('Hello! Please state your name: ')
#input variables
#inyou is a variable that defines the user's name

inventory = []
#inventory is an empty list that will store the names and quantities of the items
total_sum = 0
#total_sum is the running total variable that starts at 0

print("Hello", inyou, "! Let's start the lab cleanup inventory.")

#iteration functions and calculations
while True:
    inITEM = input('Enter Name of Glassware Washed (type "done" to stop): ')
    
    if inITEM == "done":
        break
        #break is used to exit the loop once the user types "done"
        
    inQTY = input('Enter Quantity Washed: ')
    #inQTY is a variable for the number of pieces washed for that specific glassware
    
    total_sum = total_sum + int(inQTY)
    #The running total updates by adding the new quantity as an integer
    
    item_record = inITEM + " (" + inQTY + " pcs)"
    inventory.append(item_record)
    print("Recorded:", item_record)
    #The item name and quantity are combined, added to the list, and the loop repeats

#The output will show the final list and the total sum of glassware washed by the user.
print("\n--- Final Cleanup Report for", inyou, "---")
print("Items washed:")

#This is a 'for' loop to print out each recorded item from our list one by one
for item in inventory:
    print("-", item)

print("The total sum of all glassware washed today is:", total_sum, "pieces.")
