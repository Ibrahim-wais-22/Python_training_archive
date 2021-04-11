rows, cols = (5, 5) 

arr = [[0 for i in range(cols)]for j in range(rows)]

arr[0][1]= 1
for row in arr :
    print(row)