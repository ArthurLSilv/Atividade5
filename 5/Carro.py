from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

    def correr(self):
        print(f'O {self._tipo} esta correndo a {self._velocidade}km/h')






