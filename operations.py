class Vector:
    def __init__(self, components):
        self.components = components
        self.dim = len(components)

    def add(self, vec1, vec2):
        result = []
        for i in range(len(vec1)):
            result.append(vec1[i] + vec2[i])
        return result


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(Vector.add(v1, v2))
