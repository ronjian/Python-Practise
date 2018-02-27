# This is a mathematical problem... and you have to understand the relationship
# that exists between the averages of the slices.
#
# We know from the problem description that the slices are a minimum length of 2.
# The trick to this problem is that the min average slice also cannot be longer than 3.
# So we only have to calculate the avg of the slices of length 2 and 3.
#
# To understand why the min average slice cannot be longer than 3, consider
# the case where it is longer than 3...
#
# ex. [-10, 3, 4, -20]
#
# avg(0,3) = -23 / 4 = -5.75 // entire array is -5.75 average
# avg(0,1) = -7 / 2 = -3.5 // subslice (0,1)
# avg(2,3) = -16 / 2 = -8 // subslice (2,3)
#
# Notice that (avg(0,1) + avg(2,3)) / 2 = avg(0,3)
# Therefore, if avg(0,1) != avg(2,3) then one of them must be smaller than the other.
#
# No matter which way we split up this array, if the slices aren't exactly the same,
# then one of them must have a lower average than the full slice. Play around with it
# and you'll see that it's true. There are mathematical proofs out there for this.