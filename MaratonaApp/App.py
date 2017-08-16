from Model.Pessoa import Pessoa
from Model.Cliente import Cliente
from Model.Funcionario import Funcionario
from Model.Maratona import Maratona

def main():
    funcionario = Funcionario("Maria")
    cliente = Cliente("josé")
    maratona = Maratona()
    maratona.correr(cliente)
    maratona.correr(funcionario)
    pessoa = Pessoa("josé")
    print(pessoa)

if __name__ == "__main__":
    main()
