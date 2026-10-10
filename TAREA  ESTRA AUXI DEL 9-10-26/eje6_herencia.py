

class Animal:
    def __init__(self, edad: int, peso: float, especie: str):

        self._edad = edad
        self._peso = peso
        self._especie = especie

    def respirar(self) -> str:
        return "Tomando oxígeno del entorno."

    def mover(self) -> str:
        return "El animal está cambiando de posición."

    def __str__(self):
        return f"Especie: {self._especie} | Edad: {self._edad} años | Peso: {self._peso} kg"


class Terrestre(Animal):
    def __init__(self, edad: int, peso: float, especie: str, numero_patas: int, tipo_pelaje: str):
        super().__init__(edad, peso, especie)
        self.numero_patas = numero_patas
        self.tipo_pelaje = tipo_pelaje


    def caminar(self):
        return f"El {self._especie} está caminando apoyando sus {self.numero_patas} patas."

    def correr(self):
        return f"¡El {self._especie} está corriendo velozmente!"

    def respirar(self) -> str:
        accion_base = super().respirar()
        return f"{accion_base} Respira aire a través de sus pulmones terrestres."

    def mover(self) -> str:
        return f"Movimiento terrestre: Camina o corre sobre el suelo firme."

    def __str__(self):
        datos_padre = super().__str__()
        return f"--- Terrestre ---\n{datos_padre}\nPatas: {self.numero_patas} | Pelaje: {self.tipo_pelaje}\n"


class Aereo(Animal):
    def __init__(self, edad: int, peso: float, especie: str, envergadura_alas: float, tipo_pico: str):
        super().__init__(edad, peso, especie)
        self.envergadura_alas = envergadura_alas  
        self.tipo_pico = tipo_pico

    def volar(self):
        return f"El {self._especie} despliega sus alas de {self.envergadura_alas}m y vuela."

    def construirNido(self):
        return f"El {self._especie} está recolectando ramitas usando su pico {self.tipo_pico}."

    def respirar(self) -> str:
        accion_base = super().respirar()
        return f"{accion_base} Respira de forma eficiente mediante pulmones y sacos aéreos."

    def mover(self) -> str:
        return f"Movimiento aéreo: Surca los cielos batiendo sus alas."

    def __str__(self):
        datos_padre = super().__str__()
        return f"--- Aéreo ---\n{datos_padre}\nAlas: {self.envergadura_alas}m | Pico: {self.tipo_pico}\n"


class Acuatico(Animal):
    def __init__(self, edad: int, peso: float, especie: str, numero_aletas: int, tiene_branquias: bool):
        super().__init__(edad, peso, especie)
        self.numero_aletas = numero_aletas
        self.tiene_branquias = tiene_branquias

    def nadar(self):
        return f"El {self._especie} se impulsa en el agua usando sus {self.numero_aletas} aletas."

    def sumergirse(self):
        return f"El {self._especie} se sumerge a gran profundidad."

    def respirar(self) -> str:
        accion_base = super().respirar()
        if self.tiene_branquias:
            return f"{accion_base} Filtra el oxígeno directamente del agua usando sus branquias."
        else:
            return f"{accion_base} Sale a la superficie a tomar aire pulmonar (como los delfines)."

    def mover(self) -> str:
        return f"Movimiento acuático: Se desplaza nadando y buceando en el agua."

    def __str__(self):
        datos_padre = super().__str__()
        sistema_respiratorio = "Branquias" if self.tiene_branquias else "Pulmones"
        return f"--- Acuático ---\n{datos_padre}\nAletas: {self.numero_aletas} | Respira por: {sistema_respiratorio}\n"



if __name__ == "__main__":
    
    leon = Terrestre(edad=5, peso=190.5, especie="León", numero_patas=4, tipo_pelaje="Corto y dorado")
    aguila = Aereo(edad=3, peso=4.2, especie="Águila", envergadura_alas=2.1, tipo_pico="Ganchudo")
    delfin = Acuatico(edad=8, peso=150.0, especie="Delfín", numero_aletas=3, tiene_branquias=False)

    print("=== INCISO B: MOSTRAR DATOS DE LOS ANIMALES ===\n")
    print(leon)
    print(aguila)
    print(delfin)

    print("=== INCISOS C y D: PROBAR MÉTODOS HEREDADOS Y SOBREESCRITOS ===\n")
    
    animales = [leon, aguila, delfin]
    for animal in animales:
        print(f"Animal: {animal._especie}")
        print(f"  -> Respiración: {animal.respirar()}")
        print(f"  -> Movimiento:  {animal.mover()}")
        print("-" * 50)
