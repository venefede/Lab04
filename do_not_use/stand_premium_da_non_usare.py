from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    @posizione.setter
    def posizione(self, valore):
        self.__posizione = valore

    def __str__(self):
        return f"{super().__str__()}, {self.posizione}"

    def descrivi_stand(self):
        return f"{super().descrivi_stand()} - Posizione: {self.posizione} - {self.stato()}"

    def prezzo_finale(self):
        return self.prezzo_base * 1.30