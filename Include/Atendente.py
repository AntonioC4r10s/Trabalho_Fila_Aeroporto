
class Atendente:
    def __init__(self, id, lista):
        self.id = id
        self.lista = lista


    def setId(self, id):
        self.id = id

    def setLista(self, lista):
        self.lista = lista

    def getId(self, id):
        self.id = id

    def getLista(self, lista):
        self.lista = lista

    def mostrarHora(hora, minutos):
        return ("hora: {0}:{1}".format(hora, minutos))