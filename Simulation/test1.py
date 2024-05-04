orgPos={}
temp=1
index=[0,2,1]
count_dict = count_dict ={'img1': 45, 'img2': 30, 'img3': 20, 'img4': 30}
count_dictValues=list(count_dict.values()) #extract keys of count_dict
#assign original position
for i in range(len(count_dictValues)):
    orgPos[count_dictValues[i]]=i
print(orgPos)
# Convert dictionary values into a list
values_list = list(count_dict.values())
print(values_list)
if temp!=0:
    t=[values_list[i] for i in range(len(values_list)) if i not in index]
else:
    t=values_list
print(t)
sorted_values= sorted(t, reverse=True)
signal_order = [orgPos[element] for element in sorted_values]
signal_order=index+signal_order
# Find the maximum value
max_value = max(t)
# Find the index of the maximum value in the list
max_index = values_list.index(max_value)
index.append(max_index)
print(index)
print(signal_order)