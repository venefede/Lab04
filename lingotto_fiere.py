from operator import attrgetter

from stand import Stand
from stand_con_prese import StandConPrese
from stand_premium import StandPremium
from espositori import Espositori


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.stands = {}
        self.espositori = {}

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
        disponibilita = "Disponibile"
        with open(file_path, "r") as file:
            for riga in file:
                lista_riga = riga.strip().split(",")
                if "ST" in lista_riga[0]:
                    codice = lista_riga[0]
                    superficie = lista_riga[1]
                    padiglione = lista_riga[2]

                    if len(lista_riga) > 4:

                        if lista_riga[4].isdigit():
                            numPrese = int(lista_riga[4])
                            prezzo = round(int(lista_riga[3]) * (1 + 0.07 * numPrese),2)
                            lista_riga.append(disponibilita)
                            stand_con_prese = StandConPrese(codice, superficie, padiglione, prezzo, numPrese, disponibilita)
                            self.stands[codice] = stand_con_prese


                        else:
                            prezzo = round(int(lista_riga[3]) * 1.30,2)
                            posizione = lista_riga[4]
                            stand_premium = StandPremium(codice, superficie, padiglione, prezzo, posizione, disponibilita)
                            self.stands[codice] = stand_premium

                    else:
                        prezzo = int(lista_riga[3])
                        stand = Stand(codice, superficie, padiglione, prezzo, disponibilita)
                        self.stands[codice] = stand

                else:
                    codice = lista_riga[0]
                    nome = lista_riga[1]
                    cognome = lista_riga[2]
                    espositore = Espositori(codice, nome, cognome)
                    self.espositori[codice] = espositore
        # TODO
        #fatto

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stands or codice_espositore not in self.espositori:
            raise ValueError("Stand o/e Espositore inesistente/i")

        stand = self.stands[codice_stand]
        espositore = self.espositori[codice_espositore]

        if stand.disponibilita != "Disponibile":
            raise ValueError("Stand non disponibile")

        if espositore.stand is not None:
            raise ValueError("Espositore già associato a uno stand")

        stand.espositore = espositore
        espositore.stand = stand

        stand.disponibilita = "Non disponibile"
        # TODO
        #fatto

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.espositori.values():
            print(espositore.codiceE, espositore.nome, espositore.cognome)

            if espositore.stand is not None:
                print("Stand assegnato:", espositore.stand.codiceS)
            else:
                print("Nessuno stand assegnato")

            print()
        # TODO
        #fatto

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        lista_stands = list(self.stands.values())
        lista_stands.sort(key=attrgetter("prezzo"))
        return lista_stands
        # TODO
        #fatto


