


favourite_fruits = {'apple', 'banana', 'orange', 'grape', 'kiwi'}

friend_favourite_fruits = {'apple', 'banana', 'kiwi', 'mango', 'pineapple'}

all_fruits = favourite_fruits.union(friend_favourite_fruits)

# print(all_fruits)

print('intersection: ', favourite_fruits.intersection(friend_favourite_fruits))

print('difference: ', favourite_fruits.difference(friend_favourite_fruits))