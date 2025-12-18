# basically its same like global method but inside a class to organize it better


class Math:

    @staticmethod
    def add(x):
        return x + 5
    
print(Math.add(5))