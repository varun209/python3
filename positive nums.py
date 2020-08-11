numbers=[5,-2,8,-11,7,4]
print("original numbers in the list:",numbers)
new_numbers = list(filter(lambda x:x>0,numbers))
print("positive numbers in the list:",new_numbers)
