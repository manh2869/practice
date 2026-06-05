class Vector:
    def __init__(self, components):
        self.components = components
        self.dim = len(components)

    def __repr__(self):
        return f"{self.components}"

    def __add__(self, other_vector):
        return Vector([x + y for x, y in zip(self.components, other_vector.components)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.components])  # [1,2,3] * 5  = [5,10,15]

    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    # def subtrac(self, other_vector):
    #     return Vector([x - y for x, y in zip(self.components, other_vector.components)])


class Matrix:
    def __init__(self, data):
        self.data = data
        self.cols = len(data[0])
        self.rows = len(data)

    def __repr__(self):
        return f"{self.data}"

    def __add__(self, other):
        result = []
        for x, y in zip(self.data, other.data):
            curr = []
            for i, j in zip(x, y):
                curr.append(i + j)
            result.append(curr)
        return Matrix(result)
        print(other.rows)
        print(other.columns)

    def dot(self, other):
        return [
            [x * y for x, y in zip(row, col)] for row, col in zip(self.data, other.data)
        ]


# --------------------------------MATRIX

v1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])


# v3 = v1 + v2
v3 = v1.dot(v2)

print(v3)

# -------------------------------- VECTOR
v1 = Vector([1, 2, 3])
v2 = Vector([7, 8, 9])
v3 = v1.dot(v2)
# v3 += v1
# print(v3)
print(v3)

# print(v3.components)

# v1 = [[1, 2, 3], [4, 5, 6]]
# v2 = [[7, 8, 9], [10, 11, 12]]


# print(list(zip(v1, v2)))
