from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self, color: str):
        self._color = color 

    @abstractmethod
    def obtenerArea(self) -> float:
        pass

    def __str__(self):
        return f"Color: {self._color}"




class Cuadrado(Figura):
    def __init__(self, color: str, lado: int):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self) -> float:
        return float(self.lado * self.lado)

    def __str__(self):
        datos = super().__str__()
        return f"Cuadrado:\n{datos}\nLado: {self.lado}\nÁrea: {self.obtenerArea():.2f}\n"


class Triangulo(Figura):
    def __init__(self, color: str, lado1: int, lado2: int, lado3: int):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3


    def obtenerArea(self) -> float:
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        dentro_raiz = s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)
        return math.sqrt(max(0, dentro_raiz))

    def __str__(self):
        datos = super().__str__()
        return f"Triángulo:\n{datos}\nLados: {self.lado1}, {self.lado2}, {self.lado3}\nÁrea: {self.obtenerArea():.2f}\n"


class Redondo(Figura):
    def __init__(self, color: str, radio: int):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self) -> float:
        return math.pi * (self.radio ** 2)

    def __str__(self):
        datos = super().__str__()
        return f"Redondo:\n{datos}\nRadio: {self.radio}\nÁrea: {self.obtenerArea():.2f}\n"



if __name__ == "__main__":

    print("INCISO C: Instanciar 2 objetos de cada subclase y mostrarlos \n")
    
    c1 = Cuadrado("Rojo", 4)
    c2 = Cuadrado("Azul", 6)
    
    t1 = Triangulo("Verde", 3, 4, 5)
    t2 = Triangulo("Amarillo", 5, 5, 5)
    
    r1 = Redondo("Negro", 3)
    r2 = Redondo("Blanco", 5)

    print(c1)
    print(c2)
    print(t1)
    print(t2)
    print(r1)
    print(r2)

    print("--- INCISO D: Comparar un Cuadrado y un Triángulo y mostrar el color del mayor ---\n")
    
    print(f"Área del Cuadrado ({c1._color}): {c1.obtenerArea():.2f}")
    print(f"Área del Triángulo ({t1._color}): {t1.obtenerArea():.2f}")
    
    if c1.obtenerArea() > t1.obtenerArea():
        print(f"El color de la figura con mayor área es: {c1._color}")
    elif t1.obtenerArea() > c1.obtenerArea():
        print(f"El color de la figura con mayor área es: {t1._color}")
    else:
        print("Ambas figuras tienen la misma área.")
