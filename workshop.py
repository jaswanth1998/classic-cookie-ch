matSize = input("Enter the size of square matrix")
matSize = int(matSize)
matrix = []
for i in range(0,matSize):
    matrix.append([])
    for j in range(0,matSize):
        a = input()
        a = int(a)
        while((a>1)or(a<0)):
              print("enter only 0 or 1 as input")
              a = input()         
              
        matrix[i].append(a)

increase = True
count = 0
answer = []      
for i in range(5):
    for j in range(5):
        if(increase):
            a = matrix[j][i]
            if(j==4):
                increase = False
        else:
            a = matrix[4-j][i]
            if(j==4):
                increase = True

        a = int(a)
        if (a==1):
            count = count +1
        else:
            if(count>0):
                answer.append(count)
                count = 0
            
print(answer)
        
                     
