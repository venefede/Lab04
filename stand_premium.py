from stand import Stand


class StandPremium(Stand):
    def __init__(self, codiceS, superficie, padiglione, prezzo, posizione):
        super().__init__(codiceS, superficie, padiglione, prezzo)
        self.posizione = posizione

    @property
    def posizione(self):
        return self._posizione

    @posizione.setter
    def posizione(self, posizione):
        self._posizione = posizione


    def __str__(self):
        return f"{super().__str__()}, Posizione: {self.posizione}"