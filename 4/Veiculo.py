class Veiculo():
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

    def descricao(self):
        print(f'O {self._tipo} é azul e pode chegar a {self._velocidade}km/h')

