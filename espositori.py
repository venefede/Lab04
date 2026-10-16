class Espositori:

    def __init__(self, codiceE, nome, cognome):
        self.codiceE = codiceE
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    @property
    def codiceE(self):
        return self.__codiceE

    @codiceE.setter
    def codiceE(self, codiceE):
        self.__codiceE = codiceE

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome

    def __str__(self):
        return f"Codice: {self.codiceE}, Nome: {self.nome}, Cognome: {self.cognome}"