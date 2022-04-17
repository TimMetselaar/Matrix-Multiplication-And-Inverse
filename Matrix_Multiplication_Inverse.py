import copy as cp

class Matrix:
    def __init__ (self, *args):
        if len (args) == 2:
            self.entries = [[0 for column in range (args [1])] for row in range (args [0])]
        else:
            self.entries = [[float (entry) for entry in row] for row in args [0]]
        self.nrOfRows = len (self.entries)
        self.nrOfColumns = len (self.entries [0]) if self.nrOfRows else 0


    def __matmul__ (self, other):
        if self.nrOfColumns == other.nrOfRows:
            result = Matrix (self.nrofRows, other.NrOfColumns)
            for rowIndex in range (result.nrOfRows):
                for columnIndex in range (result.nrOfColumns):
                    for termIndex in range (result.NrOfColumns):
                        result [rowIndex][columnIndex] += self [rowIndex][termIndex] * other [termIndex][columnIndex]
                        
            return result
        else:
            # Raise exception
            raise Exception ('Non matching dimensions')
    
    def __inverse__ (self):
        print ("Start calculating inverse. Press enter to go to the next step")
        if self.nrOfRows == self.nrOfColumns:
            input ('Copy matrix:')
            self = cp.deepcopy (self)
            print (self)

            input ('Augment matrix with unity matrix')
            for rowIndex in range (self.nrOfRows):
                self [rowIndex] += ([(1 if columnIndex == rowIndex else 0) for columnIndex in range (nrOfColumns)])
            self.nrOfColumns *= 2
            print (self)
            
            print ('Use each row of the matrix as pivot row')
            for pivotIndex in range (self.nrOfRows):

                input ('Swap rows if needed to get a nonzero pivot:\n')
                if not self [pivotlndex] [pivotIndex]:
                    for rowIndex in range (pivotlndex + 1, self.nrOfRows):
                        if self [rowlndex] [pivotlndex] : 
                            self [pivotIndex], self [rowlndex] = self [rowlndex], self [pivotIndex]
                            break

                print (self)


                input ('Make pivot entry')
                pivot = self [pivotIndex] [pivotIndex]
                for columnlndex in range (pivotIndex, self.nrOfColumns):
                    self [pivotIndex] [columnIndex] /= pivot
                print (self)

                input ( 'Sweep non-pivot rows to zero in their pivot column')
                for rowIndex in range (self.nrOfRows):
                    if rowIndex != pivotIndex:
                        multiplier = self [rowlndex] [pivotIndex]
                        for columnlndex in range (pivotIndex, self.nrOfCoIumns):
                            self [rowlndex] [columnlndex] -= multiplier * self [pivotIndex] [columnIndex]
                print (self)

                print ('Left matrix is Unity matrix and the right matrix is the inverse')
                

print ("")
print ("*********************************************************************************************")
print ("**************************** Matrix multiplication or inverse *******************************")
print ("*********************************************************************************************")
print ("")

print ("Do you want to multiply two matrices or do you want to compute an inverse of a matrix?")
print ("")
print ("1. Multiplication")
print ("2. Inverse")
print ("")

invalidChoice = None
#When the user does not chose the right number. He will redirected back to the first question.
while invalidChoice not in (1, 2):

    answer = int(input('Choose 1 or 2: '))

    if answer == 1:
        print ("You have chosen 1: Multiplication")
        print ("Do you want to generate two matrices or use two predefined matrices?")
        print ("")
        print("1. Generate matrices")
        print("2. Use predefined matrices")
        print("")

        invalidChoiceMulti = None

        while invalidChoiceMulti not in (1, 2):

            answerMulti = int(input('Choose 1 or 2: '))

            if answerMulti == 1:
                lowestNumber = -15
                highestNumber = 15
                maxRows = 6
                maxColumns = 6

                matrixMulti1 = [rd.choices(range(lowestNumber, highestNumber), k=maxColumns) for _ in range(maxRows)]
                matrixMulti2 = [rd.choices(range(lowestNumber, highestNumber), k=maxColumns) for _ in range(maxRows)]

                print("------------------- Matrix 1-------------------")
                print("")
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrixMulti1]))
                print("")

                print("------------------- Matrix 2-------------------")
                print("")
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrixMulti2]))
                print("")

            elif answerMulti == 2:
                pass
            else:
                print("You have chosen an invalid number during the multiplication program. Try again.")


    elif answer == 2:
        print ("You have chosen 2: Inverse")
        print("Do you want to generate a matrix or use a predefined matrix?")
        print("")
        print("1. Generate matrix")
        print("2. Use predefined matrix")
        print("")

        invalidChoiceInverse = None

        while invalidChoiceInverse not in (1, 2):

            answerInverse = int(input('Choose 1 or 2: '))

            if answerInverse == 1:
                pass
            elif answerInverse == 2:
                pass
            else:
                print("You have chosen an invalid number during the inverse program. Try again.")


    else:
        print("You have chosen an invalid number. Try again.")




