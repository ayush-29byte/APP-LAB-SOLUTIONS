rows = int(input("Enter the number of rows: "))    
n = rows    
for i in range(rows, 0, -1):  
    for j in range(0, i):    
        print(n, end=' ')  
    print()