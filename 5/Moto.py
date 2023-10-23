from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

    def correr(self):
        print(f'o {self._tipo} esta correndo a {self._velocidade}km/h')

