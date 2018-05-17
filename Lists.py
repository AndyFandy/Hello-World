fruits = ['oranges', 'apples', 'kiwi', 'mango', 'banana']
veggies = ['brocoli', 'tomato', 'squash', 'okra']
print(fruits, veggies)
fruits.append('tangerine')
veggies.append('green beans')
print(fruits, veggies)
pop = fruits.index('oranges')
print(fruits.pop(pop))
print(fruits)