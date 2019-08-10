#Pre Release Scenario
cowIds = []
milkStore = []
yieldCounter = 0
lowYieldList = []

# Task 1 : Record data
noOfCows = int(input("How many cows are there in the herd? "))

# for each cow in the heard prompt the cowId from the user and store them
for i in range(noOfCows):#i is working as a counter
    # prompt the cowId
    cowId = int(input("Enter your cows code starting with 100, follow with 101, 102 etc for the next cow: "))

    # validate the cowId
    if cowId < 100 or cowId > 999:
        print ("Wrong ID for cow. Id must be a 3 character code starting from 100.")
        exit(1)

    # add the cowId to the list
    cowIds.append(cowId)
    # add a slot in the milkStore to the cow with cowId
    milkStore.append(0)
    # low yield list
    lowYieldList.append(0)

# milk the cow for seven days in a week
for d in range(1, 8):#d is working as a counter and will repeat 7 times
    # for each cow in the cowIds list we prompt the user for the yield
    for j in range(len(cowIds)):#this loop will run the number of times the user entered i.e if the user asked for 3 cows, it will loop 3 times within the above range
        # each cow is yield twice per day

        perDayMilk = 0

        for k in range(2):#This is nested inside upper loop - range is set to 2 because we want this loop to run twice daily
            # prompt the yield
            milkYield = float(
                input("What is the Yield of the cow [day " + str(d) + "] for cowId:" + str(cowIds[j]) + " ? "))#This will take yield in outer loop d and append it against cowIds
            # add the yield to the milkStore
            milkStore[j] += milkYield
            perDayMilk += milkYield

        # check the daily yield for the day
        if perDayMilk < 12:
            lowYieldList[j] += 1

# print (cowIds)
# print (milkStore)

# Task 2 : Total yield of the cows for the week
print ("Total yield for the week : " + str(round(sum(milkStore))))

# Task 2 : Average yield for the cow
averageYield = sum(milkStore) / len(cowIds)#sums entries in list against number of cows to be milked
print ("Average yield per cow :" + str(round(averageYield)))

# Task 3 : Cow with the maximum yield
maxYield = 0#starts at 0 as we want this to change to output max yield
maxYieldCowId = ''
for m in range(len(cowIds)):#this will identify the number of items within array cowIds
    if milkStore[m] > maxYield:#using counter m from the abouve line
        maxYield = milkStore[m]#m identifies the position of the cow id in the list
        maxYieldCowId = cowIds[m]

print ("Cow " + str(maxYieldCowId) + " has the maximum yield of " + str(round(maxYield)) + " Litres")

# Task 3 : Cow with the least yield for four or more days
for n in range(len(cowIds)):
    # check if the cow yielded lesser than 12L for more than 4 days
    if lowYieldList[n] >= 4:
        print ("CowId : " + str(cowIds[n]) + " yielded low milk for " + str(lowYieldList[n]) + " days")
