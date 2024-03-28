class reserveEntity:
    def __init__(self, nome_professor, materia, inicio_reserva, fim_reserva) -> None:

        self.nome_professor = nome_professor
        self.materia = materia
        self.inicio_reserva = inicio_reserva
        self.fim_reserva = fim_reserva

    def __str__(self) -> str:
        return f"Início: {self.inicio_reserva} Fim: {self.fim_reserva}"
