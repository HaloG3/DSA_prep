# approach
'''1. first flatten the matrix in 1 D
2. do a binary search operation for target value
3. its a list so we can perform list operation there
4. divmod = div + mod = m//n + m %n
'''

def searchElement (matrix, target):
    m,n = len(matrix), len(matrix[0])
    left ,right = 0, m*n-1

    while left<= right:
        mid = (left+right)>>1
        x,y = divmod(mid,n)

        if matrix[x][y]==target:
            return True
        elif matrix[x][y] >target:
            right = mid-1
        else:
            left = mid+1
        return False
    
