# this is code for diagonal traversal of matrix 

matrix = [[11,12,13,14],[21,22,23,14],[31,32,33,34],[41,42,43,44]]
m = len(matrix[1])

n =  len (matrix)
def diagonal(matrix):
    if matrix==[]:
        return 'not a valid matrix'
    # diagonals in mat  = m+n-1 m= row , n= column 
    for i in range (0,m,1) :
        k =i
        j = 0
        while k>=0:
            print(matrix[k][j] , end=" ")
            k-=1
            j+=1
    for i in range (1, n,1):
        k = m-1
        j = i
        while j<=n-1:
            print(matrix[k][j], end=" ")
            k-=1
            j+=1
    return None
    


# when we reach the even iterration we reverse the output 
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Get the dimensions of the matrix
        m, n = len(mat), len(mat[0])
        # Prepare the result list
        result = []
        # Start from the top-left corner
        i, j = 0, 0
        # This variable keeps track of direction: 1 for up-right, -1 for down-left
        dir = 1
        
        # Loop until we've added all elements to the result
        for _ in range(m * n):
            # Add the current element to the result
            result.append(mat[i][j])
            # Move in the current direction
            if dir == 1:  # Moving up-right
                if j == n - 1:  # Hit the right boundary
                    i += 1      # Move down to next row
                    dir = -1    # Change direction
                elif i == 0:    # Hit the top boundary
                    j += 1      # Move right to next column
                    dir = -1    # Change direction
                else:
                    i -= 1      # Move up
                    j += 1      # Move right
            else:  # dir == -1, Moving down-left
                if i == m - 1:  # Hit the bottom boundary
                    j += 1      # Move right to next column
                    dir = 1     # Change direction
                elif j == 0:    # Hit the left boundary
                    i += 1      # Move down to next row
                    dir = 1     # Change direction
                else:
                    i += 1      # Move down
                    j -= 1      # Move left
        return result
    
    
print(diagonal(matrix))

print(matrix[0], "\n", matrix[1],"\n", matrix[2],"\n", matrix[3])
