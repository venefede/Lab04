from stand import Stand

class StandConPrese (Stand):
    def __init__(self, codiceS, superficie, padiglione, prezzo, numPrese):
        super().__init__(codiceS, superficie, padiglione, prezzo)
        self.numPrese = numPrese

    @property
    def numPrese(self):
        return self._numPrese

    @numPrese.setter
    def numPrese(self, numPrese):
        self._numPrese = numPrese

    def __str__(self):
        return f"{super().__str__()}, Numero Prese: {self.numPrese}"