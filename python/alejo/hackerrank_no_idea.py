

my_list_len, sets_len = input().split(' ')
sets_len = int(sets_len)
my_list_len = int(my_list_len)
my_list = input().split(' ')

set_a = set(input().split(' '))
set_b = set(input().split(' '))
happiness = 0
for number in my_list:
    if number in set_a:
        happiness += 1
    if number in set_b:
        happiness -= 1
        
print(happiness)
