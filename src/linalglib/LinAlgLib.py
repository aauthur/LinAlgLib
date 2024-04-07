class rowVector():
    #Row vectors for matrix initialization or other uncommon applications.
    def __init__(self, contents=[], size=0):
        #Takes as argument a list of the vectors contents, or a desired size of which to initialize a zero vector.
        if contents != []:
            self.contents = []
            for i in range(0, len(contents)):
                self.contents.append(contents[i])
            self.size = len(self.contents)
        else:
            self.contents = contents
            if size != 0:
                if (type(size) != type(1)) or (size < 0):
                    print("Vector size must be a positive integer.")
                    raise TypeError
                else:
                    for i in range(size):
                        self.contents.append(0)
                    self.size = size
    def __repr__(self):
        #Prints vectors contents.
        return f"{self.contents}"
    
    def __add__(self, u):
        #Method to add two vectors.
        if isinstance(u, Matrix):
            if (u.rows != 1) or (u.columns != len(self.contents)):
                raise TypeError("Can only add column vectors with matricies of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i]+u.contents[0][i])
                return rowVector(contents=tmp)
        elif isinstance(u, rowVector):
            if len(self.contents) != len(u.contents):
                raise TypeError("Vector addition must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i]+u.contents[i])
                return rowVector(contents=tmp)
        else:
            raise TypeError("Cannot add column vectors with non-vectors or row vectors (Aside from n*1 matricies of the same dimension).")
        
    def __sub__(self, u):
        #Method to subtract one vector from another.
        try:
            if len(self.contents) != len(u.contents):
                raise TypeError("Invalid pair of vectors. Vector subtraction must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(round(self.contents[i] - u.contents[i]))
                return rowVector(contents=tmp)
        except AttributeError:
            raise TypeError("Cannot subtract non-vectors from vectors!")
        
    def __mul__(self, u):
        #Method for scalar multiplication of vectors.
        if (type(u) == int) or (type(u) == float):
            tmp = []
            for i in range(len(self.contents)):
                tmp.append(self.contents[i]*u)
            return rowVector(contents=tmp)
        else:
            raise TypeError("Vectors can only be multiplied by scalars.")

class columnVector():
    #Column vectors for applications involving n*1 matricies.
    def __init__(self, contents=[], size=0):
        #Takes as argument a list of the vectors contents, or a desired size of which to initialize a zero vector.
        if contents != []:
            self.contents = []
            for i in range(0, len(contents)):
                self.contents.append([contents[i]])
            self.size = len(self.contents)
        else:
            self.contents = contents
            if size != 0:
                try:
                    for i in range(size):
                        self.contents.append([0])
                except TypeError:
                    raise TypeError("Size must be a positive integer!")

    def __repr__(self):
        #Prints vectors contents.
        row_copy = rowVector([i[0] for i in self.contents])
        return f"{row_copy}**T"
    
    def __add__(self, u):
        #Method to add two vectors.
        if isinstance(u, Matrix):
            if (u.columns != 1) or (u.rows != len(self.contents)):
                raise TypeError("Can only add column vectors with matricies of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i][0]+u.contents[i][0])
                return columnVector(contents=tmp)
        elif isinstance(u, columnVector):
            if len(self.contents) != len(u.contents):
                raise TypeError("Vector addition must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i][0]+u.contents[i][0])
                return columnVector(contents=tmp)
        else:
            raise TypeError("Cannot add column vectors with non-vectors or row vectors (Aside from n*1 matricies of the same dimension).")

    def __sub__(self, u):
        #Method to subtract one vector from another.
        if isinstance(u, Matrix):
            if (u.columns != 1) or (u.rows != len(self.contents)):
                raise TypeError("Can only subtract column vectors with matricies of the same dimension!")
            else:
                tmp = []
                for i in range(self.contents):
                    tmp.append([self.contents[i][0]-u.contents[i][0]])
                return columnVector(contents=tmp)
        elif isinstance(u, columnVector):
            if len(self.contents) != len(u.contents):
                raise TypeError("Vector subtraction must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(self.contents):
                    tmp.append(self.contents[i][0]-u.contents[i][0])
                return columnVector(contents=tmp)
        else:
            raise TypeError("Cannot subtract column vectors with non-vectors or row vectors (Aside from n*1 matricies of the same dimension).")
        
    def __mul__(self, u):
        #Method for scalar multiplication of vectors.
        if (type(u) == int) or (type(u) == float):
            tmp = []
            for i in range(len(self.contents)):
                tmp.append(self.contents[i][0]*u)
            return columnVector(contents=tmp)
        else:
            raise TypeError("Vectors can only be multiplied by scalars.")

class Matrix():
    def __init__(self, content=[], size=(0,0)):
        #Create a matrix from a list of lists or row/column vectors, or initialize a zero matrix of a specified size.
        if content != []:
            self.contents = []
            if type(content[0]) == rowVector:
                self.columns = len(content[0].contents)
                self.rows = len(content)
                for i in range(len(content)):
                    if len(content[i].contents) != self.columns:
                        raise TypeError("Rows of a matrix must be of equal length!")
                    elif not isinstance(content[i], rowVector):
                        raise TypeError("Matrix elements must be consistent in typing.")
                    else:
                        self.contents.append(content[i].contents)
            elif type(content[0]) == list:
                self.columns = len(content[0])
                self.rows = len(content)
                for i in range(len(content)):
                    if len(content[i]) != self.columns:
                        raise TypeError("Rows of a matrix must be of equal length!")
                    elif not isinstance(content[i], list):
                        raise TypeError("Matrix elements must be consistent in typing.")
                    else:
                        self.contents.append(content[i])
            elif type(content[0] == columnVector):
                self.columns = len(content)
                self.rows = len(content[0].contents)
                for i in range(self.columns):
                    if len(content[i].contents) != self.rows:
                        raise TypeError("Columns of a matrix must be of equal size!")
                    elif not isinstance(content[i], columnVector):
                        raise TypeError("Matrix elements must be consistent in typing.")
                for i in range(self.rows):
                    tmp = []
                    for j in range(self.columns):
                        tmp.append(content[j].contents[i][0])
                    self.contents.append(tmp)
            else:
                raise TypeError("Matricies can only have vector objects or lists as rows.")
        else:
            if (size[0] == 0 and size[1] != 0) or (size[1] == 0 and size[0] != 0):
                raise ValueError("Cannot have a matrix with rows and no columns, or columns and no rows.")
            self.contents = []
            self.rows = size[0]
            self.columns = size[1]
            for i in range(self.rows):
                self.contents.append(rowVector(size=self.columns).contents)

    def __repr__(self):
        #Respresents the matrix as rows on new lines.
        if self.contents == []:
            return "[]"
        result = []
        for row in self.contents:
            tmp = []
            for i in range(len(row)):
                new = round(float(row[i]), 5)
                try:
                    if new - float((str(new)[0])) == 0.0:
                        tmp.append(int(new))
                    else:
                        tmp.append(new)
                except ValueError:
                    #Handle case where float is a negative, and its first character is '-'
                    if new - float((str(new)[1])) == 0.0:
                        tmp.append(int(new))
                    else:
                        tmp.append(new)
            result.append(tmp)
        newline = "\n"
        return f'{newline.join(f"{row}" for row in result)}'
    
    def __add__(self, B):
        #Adds matricies and raises an exception if they are of different dimensions.
        try:
            if (self.rows != B.rows) or (self.columns != B.columns):
                raise ValueError("Cannot add matricies with different dimensions.")
            else:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for j in range(self.columns):
                        tmp1.append(self.contents[i][j] + B.contents[i][j])
                    tmp.append(rowVector(contents=tmp1))
                return Matrix(content=tmp)
        except AttributeError:
            if isinstance(B, columnVector) or isinstance(B, rowVector):
                tmp = B + self
                return Matrix(content=[tmp.contents])
            else:
                raise TypeError("Cannot add matricies with non matricies.")
        
    def __sub__(self, B):
        #Subtracts matricies and raises an exception if they are of different dimensions.
        try:
            if (self.rows != B.rows) or (self.columns != B.columns):
                raise ValueError("Cannot subtract matricies with different dimensions.")
            else:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for j in range(self.columns):
                        tmp1.append(self.contents[i][j] - B.contents[i][j])
                    tmp.append(rowVector(contents=tmp1))
                return Matrix(content=tmp)
        except AttributeError:
            if isinstance(B, columnVector) or isinstance(B, rowVector):
                tmp = B - self
                return Matrix(content=[tmp.contents])
            else:
                raise TypeError("Cannot subtract matricies with non matricies.")

    def __mul__(self, B):
        #Defines matrix multiplication and scalar multiplication on matricies.
        if isinstance(B, int) or isinstance(B, float):
            tmp = []
            for i in range(self.rows):
                tmp1 = rowVector(self.contents[i])
                tmp.append(tmp1*B)
            return Matrix(content=tmp)
        elif isinstance(B, Matrix):
            if self.columns == B.rows:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for k in range(self.columns):
                        tmp2 = 0
                        for j in range(self.columns):
                            tmp2 += (self.contents[i][j]*B.contents[j][k])
                        tmp1.append(tmp2)
                    tmp.append(tmp1)
                return Matrix(content=tmp)
            else:
                raise ValueError("To multiply matrix A by matrix B, number of columns of A must equal number of rows of B.")

    def row_swap(self,r1,r2):
        #Swap two rows of a matrix
        tmp = []
        if r1 == r2:
            raise Exception("Can't swap a row with itself.")
        if (r1 > self.rows) or (r2 > self.rows) or (r1 < 0) or (r2 < 0) or (type(r1) != int) or (type(r2) != int):
            raise Exception("Invalid input for rows.")
        tmp = self.contents[r1]
        self.contents[r1] = self.contents[r2]
        self.contents[r2] = tmp

    def row_scale(self, r, c):
        #Scales row r by a constant c
        if (type(c) != int) and (type(c) != float):
            raise TypeError("Row must be scaled by a scalar quantity.")
        elif (type(r) != int):
            raise TypeError("Row input must be an integer.")
        elif (r < 0) or (r > self.rows):
            raise TypeError("Specified row does not exist in the given matrix.")
        else:
            tmp = rowVector(contents=self.contents[r])*c
            self.contents[r] = tmp.contents
            
    def row_addition(self, r, rc, c=1):
        #Adds rc, scaled by a constant c (default 1), to r.
        if r == rc:
            raise Exception("Adding a row to itself is just scaling. Use .row_scale() method instead.")
        elif (r > self.rows) or (rc > self.rows) or (r < 0) or (rc < 0) or (type(r) != int) or (type(rc) != int):
            raise Exception("Invalid input for one or both rows.")
        elif (type(c) != int) and (type(c) != float):
            raise TypeError("Row must be scaled by a scalar quantity.")
        else:
            v_to_add = rowVector(contents=self.contents[rc])*c
            tmp = rowVector(contents=self.contents[r])
            tmp = tmp + v_to_add
            self.contents[r] = tmp.contents

    def transpose(self):
        #Returns a copy of the transpose of the matrix
        transpose = []
        for j in range(self.columns):
            trow = []
            for i in range(self.rows):
                trow.append(self.contents[i][j])
            transpose.append(trow)
        return Matrix(content=transpose)

    def ref(self):
        #Returns a copy of the matrix, having used row operations to reduce it to row echelon form.
        copy = Matrix(content=self.contents)
        for i in range(copy.columns):
            for j in range(i+1, copy.rows):
                if (copy.contents[j][i] != 0):
                    copy.row_addition(j, i, -(copy.contents[j][i])/(copy.contents[i][i]))
        return copy
            
    def rref(self):
        #Returns a copy of the matrix in reduced row echelon form.
        copy = self.ref()
        for i in range(copy.rows):
            for j in range(copy.columns):
                if (copy.contents[i][j] != 0):
                    copy.row_scale(i, 1/(copy.contents[i][j]))
                    break
        for i in range(1, min(copy.rows, copy.columns)):
            j = 1
            while j <= i:
                if copy.contents[i-j][i] != 0:
                    copy.row_addition(i-j, i, -copy.contents[i-j][i])
                j += 1
        return copy
                    
    def det(self):
        #Computes and returns the determinant of the matrix.
        copy = self.ref()
        det = 1
        for i in range(min(self.rows,self.columns)):
            det = det*copy.contents[i][i]
        if det == 0.0:
            return int(det)
        return round(det, 6)
    
    def row_space(self):
        #Returns a basis for the row space of a matrix.
        copy = self.rref()
        basis = set()
        for row in copy.contents:
            if all(i == 0 for i in row):
                continue
            else:
                basis.add(tuple(row))
        return basis
    
    def column_space(self):
        #Returns a basis for the column space of a matrix.
        copy = self.transpose()
        copy_reduced = copy.rref()
        basis = set()
        for i in range(copy.rows):
            if all(j == 0 for j in copy_reduced.contents[i]):
                continue
            else:
                basis.add(tuple(copy.contents[i]))
        return basis