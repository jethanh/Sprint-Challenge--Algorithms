#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because it is a single loop which runs n amount of times. Linear complexity


b) O(n^2) due to the nested loop. 


c) O(n) it calculates the number of ears based on n (bunnies) recursively n amount of times.

## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


## ANSWER BELOW:

# We could create a function that drops eggs off every floor and determines whether or not the egg breaks when dropped from that floor number. We could then contstruct a binary search that searches for eggs that have been broken. We could then search for the eggs that aren't broken and capture the floor (f) value they were dropped from. This would achieve O(log(n)) runtime complexity as we can rule out the broken eggs and only search for the eggs that survived and what floor they were dropped from.


