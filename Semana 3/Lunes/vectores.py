vec1 = [1,2,3]
vec2 = [-1,0,2]
result_sum = 0 

for index in range(len(vec1)):
    result_sum += (vec1[index]*vec2[index])

print("The result is",result_sum)