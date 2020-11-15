'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
'''


class Flip:
    """Flips and inverts an arbitrary binary matrix A.
    First the image is getting flipped horizontally and then inverted
    by turning 1 to 0 (and the opposite)."""
    
    def flip_inv_image(self, A):
        final_list = list()
        for j in range(0,len(A)):
            
            # Flip
            temp = [A[j][i] for i in range(len(A)-1,-1,-1)]
            
            # Invert
            for i in temp:
                if i == 0:
                    A[i] = 1
                else:
                    A[i] = 0
                    
            # Return final list
            final_list.append(temp)
            
        return final_list



x = Flip()
x.flip_inv_image([[1,1,0],[1,0,1],[0,0,0]])
