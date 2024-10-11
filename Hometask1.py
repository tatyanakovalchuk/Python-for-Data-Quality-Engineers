import random
#create list of 100 random numbers from 0 to 1000
rand_list = []
n = 100
for i in range(n):
	rand_list.append(random.randint(0,1000))
#sort list from min to max
rand_list.sort(reverse=False)
#create even and odd list
even_list = []
odd_list = []
for i in rand_list:
    if i % 2 == 0:
        even_list.append(i)
    if i % 2 == 1:
        odd_list.append(i)
#create average function for lists
def Average(lst):
    sum_of_list = 0
    for i in range(len(lst)):
        sum_of_list += lst[i]
    average = sum_of_list / len(lst)
    return average
#calculate average for even numbers
average_even_list = Average(even_list)
#calculate average for odd numbers
average_odd_list = Average(odd_list)
#result
print(average_even_list)
print(average_odd_list)