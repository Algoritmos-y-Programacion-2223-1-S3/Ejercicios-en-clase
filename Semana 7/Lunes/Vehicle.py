class Vehicle:
    def __init__(self,brand1,model,color,year):
        self.__brand = brand1
        self.model = model
        self.color = color
        self.year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand
        
    def print_color(self):
        print("El color es:",self.color)