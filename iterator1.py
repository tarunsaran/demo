class Cube:
    def __init__(self, cube_num):  
        self.cube_num = cube_num
        self.p_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.p_num > self.cube_num:  
            raise StopIteration
        cube_1 = self.p_num ** 3
        self.p_num += 1
        return cube_1


cube_iterator = Cube(5)
c = iter(cube_iterator)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

