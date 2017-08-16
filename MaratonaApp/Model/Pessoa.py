class Pessoa():
    def __init__(self,nome):
        self.nome = nome

    def falar(self):
        print("pessoa falando genericamente.")

    def andar(self):
        print("pessoa andando genericamente.")

    def pagar(self):
        print("pessoa pagando genericamente.")

    def __str__(self):
        return "o nome é " + self.nome
