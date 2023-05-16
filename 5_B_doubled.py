# num_digits is even
# first and second halves are equal as strings

N = int(input())
end_length = len(str(N))
end_length_half = end_length // 2
# Approach 1 : for loop from 1 to N, increment each time both conditions are met
# Status : TIME LIMIT EXCEEDED -> X
num_doubled = 0
# for num in range(N+1):
#     if(len(str(num))%2 == 0):
#         # string slicing
#         middle_index = len(str(num)) // 2
#         first_half = str(num)[:middle_index]
#         second_half = str(num)[middle_index:]
#         if(first_half == second_half):
#             num_doubled += 1
# print(num_doubled)

# Approach 2 : generate required numbers 
# Status
# 1333
# 2 and 4 digit numbers : 
# 2 : all possible numbers : 22 33 44 55 66 77 88 99
# ÷ 4 digit numbers : it ahs to limit itslef to the first half of given number : 1313, but NOT 1414
for num_digit in range(end_length_half):
    if(num_digit == 0):
        num_doubled += 0
    # 2 digit numbers
    elif(num_digit == 1):
        num_doubled += 9
    # 4 digit numbers
    else:
        num_doubled += 9 * 10**(num_digit-1)

# string slicing
first_half_N = int(str(N)[:end_length_half])
# ÷find the smallest en_length_half value  : 
smallest_end_length_half = 10**(end_length_half-1)
num_doubled += (first_half_N - smallest_end_length_half + 1)
# parse through its digits
# num_doubled += first_half_possible_vals
print(num_doubled)



