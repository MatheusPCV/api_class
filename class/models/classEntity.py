class salaEntity:
    def __init__(self,numero=0, capacidade=0) ->None:

        self.numero = numero
        self.capacidade = capacidade

    def __str__(self) -> str:
        return f"Sala: {self.numero}"
