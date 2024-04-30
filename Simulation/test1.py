count_dict = {'img1': 45, 'img2': 20, 'img3': 10, 'img4': 30}
defaultGreen = {0:15, 1:10, 2:10, 3:15}
sorted_values = sorted(count_dict.values(), reverse=True)
order=[0, 3, 1, 2]
for i in range(len(order)):
    if(sorted_values[i]>20):
        defaultGreen.update({order[i]:20})
    elif(sorted_values[i]<20):
        defaultGreen.update({order[i]:5})