class Stand:
    def __init__(self, codiceS, superficie, padiglione, prezzo, disponibilita):
        self.codiceS = codiceS
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        self.espositore = None

    @property
    def codiceS(self):
        return self.__codiceS

    @codiceS.setter
    def codiceS(self, codiceS):
        self.__codiceS = codiceS

    @property
    def superficie(self):
        return self.__superficie

    @superficie.setter
    def superficie(self, superficie):
        self.__superficie = superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    @property
    def disponibilita(self):
        return self.__disponibilita

    @disponibilita.setter
    def disponibilita(self, disponibilita):
        self.__disponibilita = disponibilita

    def __str__(self):
        return f"Codice: {self.codiceS}, Superficie: {self.superficie}, Padiglione: {self.padiglione}, Prezzo: {self.prezzo}, Disponibilità: {self.disponibilita}"

