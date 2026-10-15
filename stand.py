class Stand:
    def __init__(self, codiceS, superficie, padiglione, prezzo):
        self.codiceS = codiceS
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo


    @property
    def codiceS(self):
        return self._codiceS

    @codiceS.setter
    def codiceS(self, codiceS):
        self._codiceS = codiceS

    @property
    def superficie(self):
        return self._superficie

    @superficie.setter
    def superficie(self, superficie):
        self._superficie = superficie

    @property
    def padiglione(self):
        return self._padiglione

    @padiglione.setter
    def padiglione(self, padiglione):
        self._padiglione = padiglione

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = prezzo

    def __str__(self):
        return f"Codice: {self.codiceS},Superficie: {self.superficie},Padiglione: {self.padiglione},Prezzo: {self.prezzo}"