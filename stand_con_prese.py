from stand import Stand

class StandConPrese (Stand):
    def __init__(self, codiceS, superficie, padiglione, prezzo, numPrese, disponibilita):
        super().__init__(codiceS, superficie, padiglione, prezzo, disponibilita)
        self.numPrese = numPrese

    @property
    def numPrese(self):
        return self.__numPrese

    @numPrese.setter
    def numPrese(self, numPrese):
        self.__numPrese = numPrese

    def __str__(self):
        return f"{super().__str__()}, Numero Prese: {self.numPrese}"