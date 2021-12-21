from random import Random, sample
from datetime import date


class MegaSena:
    def __init__(self, qtde_numeros=6, seed=None):
        self.qtde_numeros = qtde_numeros
        self.seed = seed
        self.numeros = []

    def gerar_numeros(self):
        if self.seed:
            random = Random(self.seed)
        else:
            random = Random()

        self.numeros = sample(range(1, 61), self.qtde_numeros)
        self.numeros.sort()

    def __str__(self):
        return ', '.join(map(str, self.numeros))


    def bolao_da_familia(self):
        try:
            with open(f'bolao_da_familia_{date.today()}.txt', 'a') as arquivo:
                arquivo.write(f'Aposta: {seed} = {str(megasena)}\n')
        except Exception as e:
            print(e)


for i, seed in enumerate(range(1, 61)):
    megasena = MegaSena(seed=seed)
    megasena.gerar_numeros()
    print(f'Aposta: {seed} - {megasena}')
    megasena.bolao_da_familia()
