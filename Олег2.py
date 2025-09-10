a=[12, 23, 43, 565,2, 5, 6, 4, 0, 1, 'banana', 'apple', 'melon', 'pear', 'plum', 'kiwi', 'cherry','peach', 'orange', 'grape']
numbers = []
letters = []
for item in a:
  if type(item) is stp:
    letters.append(item)
  elif type(item) is int:
      numbers.append(item)

number.sort()
letters.sort()

fin_list= numbers + letters

two=[]
for item in numbers
    if item % 2 == 0
        two.append(item)

caps = []
for item in letters
     caps.append(item.upper())

prinr('відсортований список', fin_list)
print('список парних чисел' two)
print('срисок літер написаних капсом', caps)
