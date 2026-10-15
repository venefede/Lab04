class Espositori:

    def __init__(self, codiceE, nome, cognome):
        self.codiceE = codiceE
        self.nome = nome
        self.cognome = cognome


    @property
    def codiceE(self):
        return self._codiceE

    @codiceE.setter
    def codiceE(self, codiceE):
        self._codiceE = codiceE

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    def __str__(self):
        return f"Codice: {self.codiceE}, Nome: {self.nome}, Cognome: {self.cognome}"