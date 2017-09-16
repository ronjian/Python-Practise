# A = [9, 3, 9, 3, 9, 7,9]
# unpair_l = []
# for x in A:
#     if x in unpair_l:
#         unpair_l.remove(x)
#     else:
#         unpair_l.append(x)
#     res=0
#     if len(unpair_l) == 1 :
#         res = unpair_l[0]
#
#
# print(1^2)
# print(2^2)
# print(3^2)
# print(3^3)
#
# #####################
#
# z = int('101', 2) ^ int('011' ,2)
# v = 0 ^ int('011' ,2)
# print '{0:b}'.format(v)
#
# result = int('0' ,2)
# for x in A:
#     result ^= int(bin(x)[2:], 2)
# print(int(result))
#
# # This is a bitwise-based solution. And no, I don't know why it's in Lesson #2 of basic array manipulation... but anyways...
# #
# # You have to think of the integers in their binary format. By applying the XOR function of the running result to every element in the array, the binary versions of these integers end up "cancelling each other out" because the first XOR flips certain bits, and by applying XOR again with the same integer later on, you end up flipping them back. What you are left with is the one integer that never cancelled itself out.
# #
# # Read about the python bitwise: https://wiki.python.org/moin/BitwiseOperators
# #
# # To walk through an example case: [5, 3, 5]
# #
# # var result = 101 // 5 in binary
# # result = 101 ^ 011 = 110 // 6 in binary (but we don't care)
# # result = 110 ^ 101 = 011 // 3 in binary, and this is our answer
# #
# # ##############################################################################################
# #
# # If you have chance to write hard task, you will need it. Bitwise is good tool for many case.
# #
# # Once I used "AND" in bitwise for store array value as single integer in database. This is possible by use integer from 2^n. (1,2,4,8,16,32....)
# #
# # I will use this value as index key of array. If I have array like these.
# # 1 = red
# # 2 = blue
# # 4 = green
# # 8 = black
# #
# # If I want to save this item has blue and black color, I will save 2 + 8 = 10 to color field as integer in DB.
# #
# # When I want to select item that have color. I can write sql like these.
# # select * from items where color & 8;
# # so I can select any items that have black in color or If I want multiple color I can add more where to sql.
# # select * from items where color & 8 and color & 2;
# #
# # This pratise have good performance better than you store json to db or create many relation on multiple table.
# #
# # Bitwise have 6 operators so I hope you can have change to use them. it's nice tool.

z = int('101', 2) ^ int('011' ,2)
z = int('101', 2) | int('011' ,2)