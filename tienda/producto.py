class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    
    # GETTERS PARA NOMBRE, PRECIO, STOCK
    # @property es propiedad de una clase.
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    
    
    # Setter para stock, asegurando que no sea menor que 0
    @stock.setter
    def stock(self, value):
        self.__stock = max(0, value)
    
    # Sobrecarga de igualdad para comparar productos por nombre
    def __eq__(self, other):
        return self.__nombre == other.nombre
    
    # Sobrecarga de adición para agregar stock
    def __add__(self, other):
        if self == other:
            return Producto(self.__nombre, self.__precio, self.__stock + other.stock)
        return self
    
    # Sobrecarga de sustracción para restar stock
    def __sub__(self, value):
        self.stock -= value
        return self

    # STRING
    def __str__(self):#
        return f'{self.__nombre} - ${self.__precio} - Stock: {self.__stock}'
