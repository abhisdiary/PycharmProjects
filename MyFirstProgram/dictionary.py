states = {42: "Washington", 50: "Hawaii", 1: "Delaware"}

print(states[42])
print(states[50])
print(states[1])

# Adding to Dictionary
emptyDict = {}
emptyDict[1964] = "Pradip"
emptyDict[1977] = "Supriya"
emptyDict[1992] = "Unknown"
emptyDict[1994] = "Abhijeet"
emptyDict[1999] = "Arijeet"

print(emptyDict)
# length of Dictionary
lenOfDict = len(emptyDict)
print(lenOfDict)

# Reassign a value in Dictionary
emptyDict[1992] = "Wedding of Pradip & Supriya"
print(emptyDict)

# DELETING/ REMOVING a value
del emptyDict[1992]
print(emptyDict)
