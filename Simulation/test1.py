orgPos={}
count_dict = {'img1': 45, 'img2': 20, 'img3': 10, 'img4': 30}
count_dictKeys=list(count_dict.keys())
for i in range(0,len(count_dictKeys)):
        orgPos[count_dictKeys[i]]=i
sorted_keys = sorted(count_dict, key=count_dict.get, reverse=True)
sorted_values = sorted(count_dict.values(), reverse=True)
signal_order = [orgPos[element] for element in sorted_keys]
print(orgPos)
print(sorted_keys)
print(sorted_values)
print(signal_order)