
class Cliente:
    def __init__(self, id,tempoDeChegada, tempoDeFila, tempoFinal):
        self.id = id
        self.tempoDeChegada = tempoDeChegada
        self.tempoDeFila = tempoDeFila
        self.tempoFinal = tempoFinal

    #metodos set()
    def setId(self, id):
        self.id = id

    def setTempoDeChegada(self, tempoDeChegada):
        self.tempoDeChegada = tempoDeChegada

    def setTempoDeFila(self, tempoDeFila):
        self.tempoDeFila = tempoDeFila + self.tempoDeFila

    def setTempoFinal(self, tempoFinal):
        self.tempoFinal = tempoFinal + self.tempoDeFila

    #metodos get()
    def getId(self, id):
        return self.id

    def getTempoDeChegada(self, tempoDeChegada):
        return self.tempoDeChegada

    def getTempoDeFila(self, tempoDeFila):
        return self.tempoDeFila

    def getTempoFinal(self, tempoFinal):
        return self.tempoFinal

    #others
    def info(self):
        return (self.id, self.tempoDeChegada, self.tempoDeFila, self.tempoFinal)
    def __str__(self):
        return ("Cliente " + str(self.id) + " -> hora de chegada: " + str(self.tempoDeChegada) + ":00" + " -> tempo de fila: " + str(self.tempoDeFila) + " minutos " + " -> Tempo final: " + str(self.tempoFinal) + " minutos")
