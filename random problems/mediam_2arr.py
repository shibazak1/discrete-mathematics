num_1 = [1,5,9]
num_2 = [8,2,6]

merge_arr = []

for i in range(len(num_1)):
    if num_1[i]<num_2[i]:
        merge_arr.append(num_1[i])
    else:
        merge_arr.append(num_2[i])
            


#for i in num_1:
 #   merge_arr.append(i)
#for j in num_2:
 #   merge_arr.append(j)
#merge_arr.sort()

#if len(merge_arr)%2!=0:
 #   index = (len(merge_arr)-1)/2
    #print(index)
  #  print(merge_arr[int(index)])
#else:
 #   index = (len(merge_arr))/2
  #  print(index)
   # index_2 = index - 1
    #print(index_2)
    #print((merge_arr[int(index)]+ merge_arr[int(index_2)])/2)
    

print(merge_arr)

    



