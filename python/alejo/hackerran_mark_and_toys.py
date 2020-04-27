# get the number of toys and the budget
number_of_toys, budget = input().split(' ')
number_of_toys = int(number_of_toys)
budget = int(budget)

# Get the prices of the toys
toys = [int(x) for x in input().split(' ')]

toys.sort()

bought_toys = 0
money_expend = 0
for index, toy in enumerate(toys):

    if money_expend + toy <= budget:
        money_expend += toy
        bought_toys = index + 1

        continue
    else:
        break

print(bought_toys)
