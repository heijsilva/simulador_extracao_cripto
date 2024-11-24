import random
from computador import Computador

class Simulador:
    def __init__(self):
        self.computadores = [Computador(i + 1, 1000) for i in range(5)]
        self.histórico_saldo = []
        self.histórico_consumo = []
        self.histórico_falhas = []
        self.custo_energia_por_hora = 3.00  # Aumento no custo de energia por kWh (R$3.00 por kWh)
        self.precos_moedas = {
            "Bitcoin": 190000,
            "Ethereum": 000,
            "Dogecoin": 4,
            "Litecoin": 500,
            "Solana": 225,
            "Cardano": 50,
            "Polkadot": 30,
        }
        
        # Inicializando um dicionário para acumular o custo de energia por computador
        self.energia_gasta_por_computador = {computador.id: 0 for computador in self.computadores}
        self.conta_energia_acumulada = 0  # Acumula o valor da conta de energia
        
        # Histórico de energia consumida por hora
        self.energia_consumida_por_hora = {computador.id: [] for computador in self.computadores}

    def avançar_tempo(self, horas):
        """Avança o tempo e simula o impacto nas máquinas."""
        print(f"\nAvançando o tempo em {horas} horas...")

        # Lista para armazenar os ganhos de cada computador
        ganhos_computadores = []

        for computador in self.computadores:
            if computador.estado == "Funcional":
                # Realiza a mineração
                mineracao_por_moeda = {moeda: {"quantidade": 0, "valor": 0} for moeda in self.precos_moedas}
                valor_total_minerado = 0  # Variável para somar o valor total minerado

                for _ in range(horas):
                    for moeda, preco in self.precos_moedas.items():
                        if random.random() < 0.05:  # 5% de chance de minerar por hora
                            quantidade = random.uniform(0.001, 0.01)
                            mineracao_por_moeda[moeda]["quantidade"] += quantidade
                            mineracao_por_moeda[moeda]["valor"] += quantidade * preco
                            valor_total_minerado += quantidade * preco
                            computador.ganhos += quantidade * preco

                # Exibe o resumo de mineração
                print(f"\nComputador {computador.id} minerou:")
                for moeda, dados in mineracao_por_moeda.items():
                    if dados["quantidade"] > 0:
                        print(f"  - {moeda}: {dados['quantidade']:.6f} unidades (R${dados['valor']:.2f})")

                # Armazenar o valor minerado para ajuste do uso
                ganhos_computadores.append((computador.id, valor_total_minerado))

            # Simula falhas aleatórias e diminuição da vida útil
            computador.simular_falhas(horas)

            # Calcular o consumo de energia com base no uso
            maior_ganho = max(ganho for _, ganho in ganhos_computadores)
            uso_computador = 70 + (96 - 70) * (valor_total_minerado / maior_ganho) if maior_ganho > 0 else 70

            # Ajuste o consumo com base no uso
            consumo_base = 10  # Consumo base de 10 kWh por hora (para 70% de uso)
            consumo_ajustado = consumo_base * (uso_computador / 70)  # Aumenta o consumo proporcionalmente ao uso

            # Acumula o custo de energia para este computador
            custo_energia_computador = consumo_ajustado * horas * self.custo_energia_por_hora
            self.energia_gasta_por_computador[computador.id] += consumo_ajustado * horas
            self.conta_energia_acumulada += custo_energia_computador

            # Registrar o consumo de energia por hora
            for hora in range(horas):
                self.energia_consumida_por_hora[computador.id].append(consumo_ajustado)

            # Atribui o uso calculado ao computador
            computador.uso_percentual = uso_computador

            # Exibe o uso atual do computador
            print(f"  Uso do Computador {computador.id}: {computador.uso_percentual:.2f}%")

        print("\nAvanço de tempo concluído!")

    def pagar_energia(self):
        """Paga a conta de energia e debita do saldo total."""
        saldo_total = sum(c.ganhos for c in self.computadores)
        
        if saldo_total >= self.conta_energia_acumulada:
            for computador in self.computadores:
                computador.ganhos -= self.conta_energia_acumulada / len(self.computadores)
            print(f"Conta de energia paga! R${self.conta_energia_acumulada:.2f} foi debitado do saldo total.")
            self.conta_energia_acumulada = 0  # Resetando a conta de energia após o pagamento
        else:
            print(f"Saldo insuficiente! A conta de energia custa R${self.conta_energia_acumulada:.2f}, mas o saldo disponível é de R${saldo_total:.2f}.")
            # Não reseta a conta de energia, ela acumula para a próxima vez

    def realizar_manutencao(self, computador_id):
        """Realiza manutenção em um computador específico.""" 
        computador = self.computadores[computador_id - 1]
        computador.realizar_manutencao()

    def realizar_manutencao_em_todos(self):
        """Realiza manutenção em todos os computadores.""" 
        print("\nRealizando manutenção em todos os computadores...")
        for computador in self.computadores:
            computador.realizar_manutencao()

    def gerar_insights(self):
        """Gera insights sobre o status de cada computador e o custo de energia individual."""
        print("\n--- Insights dos Computadores ---")
        
        lucro_total = 0
        consumo_total_energia = 0  # Variável para somar o custo total de energia
        total_manutencao = 0  # Variável para acumular o total de manutenção realizada

        for computador in self.computadores:
            print(f"\nComputador ID: {computador.id}")
            print(f"  Estado: {computador.estado}")
            print(f"  Ganhos: R${computador.ganhos:.2f}")
            print(f"  Gasto total com manutenção: R${computador.gasto_manutencao:.2f}")

            # Custo da manutenção das peças quebradas
            custo_manutencao = 0
            manutencao_por_computador = []  # Lista para armazenar detalhes de manutenção

            for peça, info in computador.peças.items():
                estado = "Funcionando" if info["estado"] else "Quebrado"
                print(f"  Peça: {peça}, Status: {estado}, Vida Útil: {info['vida_util']} horas")
                if not info["estado"]:  # Se a peça estiver quebrada
                    # Calcular o custo de manutenção da peça quebrada
                    custo_peça = info["custo_manutencao"]
                    custo_manutencao += custo_peça
                    manutencao_por_computador.append(f"    Peça: {peça}, Custo de manutenção: R${custo_peça:.2f}")

            # Exibe os custos de manutenção de peças quebradas
            if manutencao_por_computador:
                print("\n  Manutenção necessária para as peças quebradas:")
                for manutencao in manutencao_por_computador:
                    print(manutencao)

            # Adicionando o custo de manutenção ao total
            total_manutencao += custo_manutencao

            # Exibe o consumo total de energia baseado no tempo avançado
            consumo_total = self.energia_gasta_por_computador[computador.id]  # Agora é o consumo total baseado nas horas avançadas
            print(f"  Consumo total de energia: {consumo_total:.2f} kWh")

            lucro_total += computador.ganhos
            consumo_total_energia += consumo_total

        print(f"\n--- Resumo Geral ---")
        print(f"  Lucro total: R${lucro_total:.2f}")
        print(f"  Consumo total de energia: {consumo_total_energia:.2f} kWh")
        print(f"  Conta de energia acumulada: R${self.conta_energia_acumulada:.2f}")
        print(f"  Custo total de manutenção: R${total_manutencao:.2f}")