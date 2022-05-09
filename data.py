class Datas:
    def __init__(self, dia, mes, ano):
        self.dia = str(dia) if len(str(dia)) >= 2 else f"0{dia}"
        self.mes = str(mes) if len(str(mes)) >= 2 else f"0{mes}"
        self.ano = str(ano)

    def formatar_data(self):
        print(f"{self.dia} / {self.mes} / {self.ano}")
