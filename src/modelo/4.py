class rectangulo:
    def __init__(self):
        self.esquinax1=1
        self.esquinax2=2
        self.esquinay1=1
        self.esquinay2=2

    def calcular_perimetro(self):
        self.altura= self.esquinay1 - self.esquinay2
        self.base= self.esquinax1 - self.esquinax2
        perimetro= ((self.altura*2) + (self.base*2))
        return perimetro

    def calcular_area(self):
        area= self.base * self.altura
        return area

    def cuadrado (self):
        if self.altura == self.base:
            return ("el rectangulo es cuadrado")

        else:
            return ("no es cuadrado")