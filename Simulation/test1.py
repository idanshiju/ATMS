orgPos={'img1': 0, 'img2': 1, 'img3': 2, 'img4': 3}
count_dict = {'img1': 20, 'img2': 6, 'img3': 45, 'img4': 15}
count_dictKeys=list(count_dict.keys())
i=1
for i in range(1,len(count_dictKeys)):
        orgPos[count_dictKeys[i]]=i
first_element = list(count_dict.keys())[0]

# Sort the keys based on values in descending order excluding the first element
sorted_keys = [first_element] + sorted(count_dict.keys(), key=lambda x: (-count_dict[x], x))

sorted_values = sorted(count_dict.values(), reverse=True)
signal_order = [orgPos[element] for element in sorted_keys]
print(orgPos)
print(sorted_keys)
print(sorted_values)
print(signal_order)