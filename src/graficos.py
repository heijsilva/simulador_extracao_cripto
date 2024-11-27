import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, simulador):
        self.simulador = simulador

    def gerar_graficos_lucros(self):
        """Gera gráficos de lucros de todos os computadores do simulador e os retorna."""
        lucros = [computador.ganhos for computador in self.simulador.computadores]
        figuras = []  # Lista para armazenar as figuras geradas

        # Gráfico 1: Lucros Totais
        fig1 = plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(lucros) + 1), lucros, color='orange')
        plt.title("Lucros Totais dos Computadores")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros (R$)")
        plt.xticks(range(1, len(lucros) + 1), [f"Computador {i}" for i in range(1, len(lucros) + 1)])
        plt.tight_layout()
        figuras.append(fig1)  # Adiciona a figura à lista

        # Gráfico 2: Lucros Acumulados
        lucros_acumulados = [sum(lucros[:i+1]) for i in range(len(lucros))]
        fig2 = plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(lucros_acumulados) + 1), lucros_acumulados, marker='o', color='green')
        plt.title("Lucros Acumulados ao Longo do Tempo")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros Acumulados (R$)")
        plt.xticks(range(1, len(lucros_acumulados) + 1), [f"Computador {i}" for i in range(1, len(lucros_acumulados) + 1)])
        plt.tight_layout()
        figuras.append(fig2)

        # Gráfico 3: Lucros Mensais
        lucros_mensais = [lucro / 30 for lucro in lucros]  # Supondo 30 dias no mês
        fig3 = plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(lucros_mensais) + 1), lucros_mensais, color='blue')
        plt.title("Lucros Mensais por Computador")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros Mensais (R$)")
        plt.xticks(range(1, len(lucros_mensais) + 1), [f"Computador {i}" for i in range(1, len(lucros_mensais) + 1)])
        plt.tight_layout()
        figuras.append(fig3)

        # Gráfico 4: Lucros por Hora
        lucros_por_hora = [lucro / 720 for lucro in lucros]  # 720 = 30 dias * 24 horas
        fig4 = plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(lucros_por_hora) + 1), lucros_por_hora, color='red')
        plt.title("Lucros por Hora de Operação")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros por Hora (R$)")
        plt.xticks(range(1, len(lucros_por_hora) + 1), [f"Computador {i}" for i in range(1, len(lucros_por_hora) + 1)])
        plt.tight_layout()
        figuras.append(fig4)

        # Gráfico 5: Desempenho dos Computadores
        desempenho = [
            computador.ganhos / computador.obter_consumo_energia()
            if computador.obter_consumo_energia() > 0 else 0
            for computador in self.simulador.computadores
        ]
        fig5 = plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(desempenho) + 1), desempenho, color='purple')
        plt.title("Desempenho dos Computadores (Lucro por Consumo de Energia)")
        plt.xlabel("Computadores")
        plt.ylabel("Lucros por kWh")
        plt.xticks(range(1, len(desempenho) + 1), [f"Computador {i}" for i in range(1, len(desempenho) + 1)])
        plt.tight_layout()
        figuras.append(fig5)

        # Gráfico 6: Comparação entre Consumo de Energia e Lucros
        consumos = [computador.obter_consumo_energia() for computador in self.simulador.computadores]
        print(f"Consumos: {consumos}")  # Verifique se os dados estão corretos
        fig6 = plt.figure(figsize=(10,6))
        largura_barra = 0.4  # Largura das barras
        posicoes_consumo = [i - largura_barra / 2 for i in range(1, len(consumos) + 1)]
        posicoes_lucros = [i + largura_barra / 2 for i in range(1, len(lucros) + 1)]

        # Barras de Consumo de Energia
        plt.bar(
            posicoes_consumo,
            consumos,
            color='blue', alpha=0.8, label="Consumo de Energia (kWh)", width=largura_barra
        )

        # Barras de Lucros
        plt.bar(
            posicoes_lucros,
            lucros,
            color='orange', alpha=0.8, label="Lucros (R$)", width=largura_barra
        )

        plt.title("Consumo de Energia vs Lucros por Computador")
        plt.xlabel("Computadores")
        plt.ylabel("Valores")
        plt.xticks(range(1, len(consumos) + 1), [f"Computador {i}" for i in range(1, len(consumos) + 1)])
        plt.legend()
        plt.tight_layout()

        # Adiciona o gráfico à lista de figuras
        figuras.append(fig6)

        
        # Gráfico 7: Custo de Manutenção
        custos_manutencao = [computador.gasto_manutencao for computador in self.simulador.computadores]
        fig7 = plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(custos_manutencao) + 1), custos_manutencao, color='red')
        plt.title("Custo de Manutenção Total por Computador")
        plt.xlabel("Computadores")
        plt.ylabel("Custo de Manutenção (R$)")
        plt.xticks(range(1, len(custos_manutencao) + 1), [f"Computador {i}" for i in range(1, len(custos_manutencao) + 1)])
        plt.tight_layout()
        figuras.append(fig7)

        return figuras  # Retorna a lista de gráficos gerados

    def _grafico_consumo_energia(self):
        """Gera gráficos de consumo de energia de todos os computadores."""
        consumos = [computador.obter_consumo_energia() for computador in self.simulador.computadores]

        fig = plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(consumos) + 1), consumos, color='blue')
        plt.title("Consumo de Energia dos Computadores")
        plt.xlabel("Computadores")
        plt.ylabel("Consumo (kWh)")
        plt.xticks(range(1, len(consumos) + 1), [f"Computador {i}" for i in range(1, len(consumos) + 1)])
        plt.tight_layout()

        return fig  # Retorna a figura gerada