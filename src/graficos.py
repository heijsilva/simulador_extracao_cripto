import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, simulador):
        self.simulador = simulador

    def gerar_graficos_lucros(self):
        """Gera gráficos de lucros de todos os computadores do simulador."""
        lucros = [computador.ganhos for computador in self.simulador.computadores]

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(lucros) + 1), lucros, color='orange')

        plt.title("Lucros Totais dos Computadores")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros (R$)")
        plt.xticks(range(1, len(lucros) + 1), [f"Computador {i}" for i in range(1, len(lucros) + 1)])
        plt.tight_layout()
        plt.show()

        # Gráfico 2: Lucros acumulados ao longo do tempo
        lucros_acumulados = [sum(lucros[:i+1]) for i in range(len(lucros))]

        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(lucros_acumulados) + 1), lucros_acumulados, marker='o', color='green')
        plt.title("Lucros Acumulados ao Longo do Tempo")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros Acumulados (R$)")
        plt.xticks(range(1, len(lucros_acumulados) + 1), [f"Computador {i}" for i in range(1, len(lucros_acumulados) + 1)])
        plt.tight_layout()
        plt.show()

        # Gráfico 3: Lucros mensais
        lucros_mensais = [lucro / 30 for lucro in lucros]  # Supondo 30 dias no mês

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(lucros_mensais) + 1), lucros_mensais, color='blue')
        plt.title("Lucros Mensais por Computador")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros Mensais (R$)")
        plt.xticks(range(1, len(lucros_mensais) + 1), [f"Computador {i}" for i in range(1, len(lucros_mensais) + 1)])
        plt.tight_layout()
        plt.show()

        # Gráfico 4: Lucros por hora (supondo 24 horas em operação por dia)
        lucros_por_hora = [lucro / 720 for lucro in lucros]  # 720 = 30 dias * 24 horas

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(lucros_por_hora) + 1), lucros_por_hora, color='red')
        plt.title("Lucros por Hora de Operação")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros por Hora (R$)")
        plt.xticks(range(1, len(lucros_por_hora) + 1), [f"Computador {i}" for i in range(1, len(lucros_por_hora) + 1)])
        plt.tight_layout()
        plt.show()

        # Gráfico 5: Desempenho dos computadores (lucro por consumo de energia)
        desempenho = [computador.ganhos / computador.obter_consumo_energia() if computador.obter_consumo_energia() > 0 else 0
                      for computador in self.simulador.computadores]

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(desempenho) + 1), desempenho, color='purple')
        plt.title("Desempenho dos Computadores (Lucro por Consumo de Energia)")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros por kWh")
        plt.xticks(range(1, len(desempenho) + 1), [f"Computador {i}" for i in range(1, len(desempenho) + 1)])
        plt.tight_layout()
        plt.show()

        # Gráfico 6: Comparação entre o consumo de energia e os lucros
        consumos = [computador.obter_consumo_energia() for computador in self.simulador.computadores]

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(consumos) + 1), consumos, color='blue', alpha=0.6, label="Consumo de Energia (kWh)")
        plt.bar(range(1, len(lucros) + 1), lucros, color='orange', alpha=0.6, label="Lucros (R$)")
        plt.title("Consumo de Energia vs Lucros por Computador")
        plt.xlabel("Computadores")
        plt.ylabel("Valores")
        plt.xticks(range(1, len(consumos) + 1), [f"Computador {i}" for i in range(1, len(consumos) + 1)])
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Gráfico 7: Custo de manutenção total por computador
        custos_manutencao = [computador.gasto_manutencao for computador in self.simulador.computadores]

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(custos_manutencao) + 1), custos_manutencao, color='red')
        plt.title("Custo de Manutenção Total por Computador")
        plt.xlabel("Computadores")
        plt.ylabel("Custo de Manutenção (R$)")
        plt.xticks(range(1, len(custos_manutencao) + 1), [f"Computador {i}" for i in range(1, len(custos_manutencao) + 1)])
        plt.tight_layout()
        plt.show()

    def _grafico_consumo_energia(self):
        """Gera gráficos de consumo de energia de todos os computadores."""
        consumos = [computador.obter_consumo_energia() for computador in self.simulador.computadores]

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(consumos) + 1), consumos, color='blue')

        plt.title("Consumo de Energia dos Computadores")
        plt.xlabel("Computadores")
        plt.ylabel("Consumo (kWh)")
        plt.xticks(range(1, len(consumos) + 1), [f"Computador {i}" for i in range(1, len(consumos) + 1)])
        plt.tight_layout()
        plt.show()
