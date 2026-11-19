from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, num_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__num_prese = num_prese

    @property
    def num_prese(self):
        return self.__num_prese
    @num_prese.setter
    def num_prese(self, valore):
        self.__num_prese = valore

    def __str__(self):
        return f"{super().__str__()}, {self.num_prese}"

    def prezzo_finale(self):
        return self.prezzo_base * (1 + 0.07 * self.num_prese)

    def descrivi_stand(self):
        return f"{super().descrivi_stand()} - Prese aggiuntive: {self.num_prese} - {self.stato()}"