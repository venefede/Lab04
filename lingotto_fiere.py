import operator

from stand import Stand
from stand_con_prese import StandConPrese
from stand_premium import StandPremium
from espositori import Espositori


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.stands = []
        self.stands_con_prese = []
        self.stands_premium = []
        self.espositori = []
        self.lista_stands = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome
    # TODO
    # fatto

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        with open(file_path, "r") as file:
            for riga in file:
                lista_riga = riga.strip().split(",")
                if "ST" in lista_riga[0]:
                    codice = lista_riga[0]
                    superficie = lista_riga[1]
                    padiglione = lista_riga[2]
                    prezzo = lista_riga[3]

                    if len(lista_riga) > 4:

                        if lista_riga[4].isdigit():
                            numPrese = lista_riga[4]
                            stand_con_prese = StandConPrese(codice, superficie, padiglione, prezzo, numPrese)
                            self.stands_con_prese.append(stand_con_prese)
                            self.lista_stands.append(stand_con_prese)

                        else:
                            posizione = lista_riga[4]
                            stand_premium = StandPremium(codice, superficie, padiglione, prezzo, posizione)
                            self.stands_premium.append(stand_premium)
                            self.lista_stands.append(stand_premium)
                    else:
                        stand = Stand(codice, superficie, padiglione, prezzo)
                        self.stands.append(stand)
                        self.lista_stands.append(stand)
                else:
                    codice = lista_riga[0]
                    nome = lista_riga[1]
                    cognome = lista_riga[2]
                    espositore = Espositori(codice, nome, cognome)
                    self.espositori.append(espositore)

        # TODO
        #fatto

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""



        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""

        lista_ordinata = self.lista_stands.copy()
        lista_ordinata.sort(key=operator.attrgetter("prezzo"))
        return lista_ordinata

        # TODO


