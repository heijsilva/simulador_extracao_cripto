import random

class Computador:
    def __init__(self, id, ganhos_iniciais, consumo_maximo_energia=1.5):
        self.id = id
        self.ganhos = ganhos_iniciais
        self.estado = "Funcional"  # Estado inicial

        # Dicionário para gerenciar as peças
        self.peças = {
            "Processador Ryzen 7": {
                "estado": True,
                "custo_manutencao": 2400,
                "vida_util": 40000,
                "vida_util_inicial": 40000,
            },
            "Memória RAM 16GB": {
                "estado": True,
                "custo_manutencao": 400,
                "vida_util": 90000,
                "vida_util_inicial": 90000,
            },
            "SSD 512GB": {
                "estado": True,
                "custo_manutencao": 390,
                "vida_util": 40000,
                "vida_util_inicial": 40000,
            },
            "Fonte 800W": {
                "estado": True,
                "custo_manutencao": 890,
                "vida_util": 35000,
                "vida_util_inicial": 35000,
            },
            "Placa de Vídeo RTX 4090": {
                "estado": True,
                "custo_manutencao": 2899,
                "vida_util": 29000,
                "vida_util_inicial": 29000,
            }
        }
        self.gasto_manutencao = 0
        self.uso_percentual = 70  # Percentual de uso inicial
        self.consumo_maximo_energia = consumo_maximo_energia  # Consumo máximo de energia em kWh

    def log(self, mensagem):
        """Registra mensagens sem timestamp."""
        print(mensagem)

    def realizar_manutencao(self):
        """Realiza manutenção nas peças e debita custos do saldo."""
        total_custo_manutencao = 0
        for peça, info in self.peças.items():
            if not info["estado"]:  # Se a peça estiver quebrada
                info["estado"] = True
                total_custo_manutencao += info["custo_manutencao"]
        if total_custo_manutencao > 0:
            self.ganhos -= total_custo_manutencao
            self.gasto_manutencao += total_custo_manutencao
            self.log(f"O computador {self.id} realizou manutenção no total de R${total_custo_manutencao:.2f}.")
        self.estado = "Funcional"

    def simular_falhas(self, horas):
        """Simula a falha aleatória e a redução da vida útil."""
        for peça, info in self.peças.items():
            if info["estado"]:  # Se a peça estiver funcionando
                info["vida_util"] -= horas
                if info["vida_util"] <= 0:
                    info["estado"] = False
                    self.estado = "Desligado"
                    self.log(f"A peça {peça} do computador {self.id} quebrou devido ao fim da vida útil!")
                if random.random() < 0.000008 * horas:  # Chance de falha 
                    info["estado"] = False
                    self.estado = "Desligado"
                    self.log(f"A peça {peça} do computador {self.id} apresentou uma falha!")

    def pode_avancar_no_tempo(self):
        """Verifica se o computador está funcional para avançar no tempo."""
        return self.estado == "Funcional"

    def atualizar_uso_percentual(self, ganho_total, maior_ganho):
        """Atualiza o percentual de uso do computador baseado no ganho total."""
        if maior_ganho > 0:
            self.uso_percentual = 70 + (96 - 70) * (ganho_total / maior_ganho)
        else:
            self.uso_percentual = 70

        # Limitando o uso entre 70% e 96%
        if self.uso_percentual > 96:
            self.uso_percentual = 96
        elif self.uso_percentual < 70:
            self.uso_percentual = 70

    def calcular_consumo_energia(self):
        """Calcula o consumo de energia baseado no uso percentual."""
        return (self.uso_percentual / 100) * self.consumo_maximo_energia

    def obter_consumo_energia(self):
        """Obtém o consumo de energia atual do computador em kWh."""
        return self.calcular_consumo_energia()

    def manutencao_preventiva(self):
            """Realiza manutenção preventiva nas peças e aumenta sua vida útil em 40%."""
            total_custo_preventiva = 0
            for peça, info in self.peças.items():
                # Aumenta a vida útil da peça em 35%
                incremento_vida_util = info["vida_util"] * 0.35
                info["vida_util"] += incremento_vida_util
                total_custo_preventiva += info["custo_manutencao"]
                print(f"A peça {peça} foi mantida preventivamente. Vida útil aumentada para {info['vida_util']:.2f} horas.")
            
            # Debita o custo da manutenção preventiva
            if total_custo_preventiva > 0:
                self.ganhos -= total_custo_preventiva
                self.gasto_manutencao += total_custo_preventiva
                self.log(f"O computador {self.id} realizou manutenção preventiva no total de R${total_custo_preventiva:.2f}.")

    def vida_util_precisa_manutencao(self):
        """Verifica se o computador precisa de manutenção preventiva."""
        for peça, info in self.peças.items():
            if info["vida_util"] <= 0.40 * info["vida_util_inicial"]:
                self.log(f"A peça {peça} do computador {self.id} precisa de manutenção preventiva!")
                return True
        return False
