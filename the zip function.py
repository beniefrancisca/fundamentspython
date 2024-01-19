friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

dict([("Rolf",3), ("Bob", 7), ("Jen", 15),  ("Anne", 11)])

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}
print(long_timers)

# how to combine both variables friends and time since seen to make one dictionary
# we use the zip function to combine them into one list

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = list(zip(friends, time_since_seen))
print(long_timers)
