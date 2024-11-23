import tkinter as tk
from tkinter import ttk, simpledialog
import sys
from io import StringIO
from simulador import Simulador
from graficos import Graficos  # Certifique-se de que a classe Graficos está importada corretamente

# Cores do tema Dark Mode conforme a imagem
DARK_BG = "#2E2E2E"  # Fundo mais escuro
DARK_FG = "#FFFFFF"  # Texto branco
LIGHT_BG = "#3A3A3A"  # Cor de fundo para caixas de texto e botões
BUTTON_BG = "#1F1F1F"  # Cor de fundo dos botões
BUTTON_FG = "#4CAF50"  # Cor do texto dos botões (Verde vibrante)
HOVER_BG = "#333333"  # Cor ao passar o mouse nos botões
TITLE_COLOR = "#FFFFFF"  # Cor do título
ERROR_COLOR = "#F44336"  # Cor para mensagens de erro
SUCCESS_COLOR = "#8BC34A"  # Cor para mensagens de sucesso
INFO_COLOR = "#FFFFFF"  # Cor para informações gerais
EXIT_BUTTON_BG = "#D32F2F"  # Cor do botão de sair (vermelho)

class InterfaceGrafica:
    def __init__(self, root, simulador):
        self.root = root
        self.simulador = simulador
        self.root.title("Extrator De Criptomoeda")
        self.root.geometry("1280x800")  # Aumentando um pouco o tamanho inicial da janela
        self.root.config(bg=DARK_BG)

        # Redirecionar a saída para o terminal (Console)
        self.terminal_output = StringIO()
        sys.stdout = self.terminal_output

        # Configuração da área de terminal
        self.terminal_frame = tk.Frame(self.root, bg=DARK_BG)
        self.terminal_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.terminal_text = tk.Text(
            self.terminal_frame, height=30, width=60,
            bg="#1C1C1C", fg=DARK_FG, font=("Arial", 12), wrap=tk.WORD, relief="flat"
        )
        self.terminal_text.pack(fill=tk.BOTH, expand=True)
        self.terminal_text.config(state=tk.DISABLED)

        # Criar o menu e os botões
        self.criar_menu()

        # Alterar o comportamento para fullscreen e responsividade
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.atualizar_layout()

    def toggle_fullscreen(self, event=None):
        """Alterna entre fullscreen e janela normal."""
        is_fullscreen = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not is_fullscreen)
        self.root.geometry("1280x800" if is_fullscreen else "1920x1080")
        self.atualizar_layout()

    def criar_menu(self):
        """Cria a interface de menu com botões responsivos."""
        self.menu_frame = tk.Frame(self.root, bg="#2C2C2C", bd=0)
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        titulo = tk.Label(
            self.menu_frame, text="Extrator De Criptomoeda",
            font=("Roboto", 24, "bold"), fg=TITLE_COLOR, bg="#2C2C2C"
        )
        titulo.grid(row=0, column=0, pady=(20, 30))

        # Botões para as opções do menu
        self.criar_botao("Avancar no tempo", self.avancar_tempo).grid(row=1, column=0, sticky="ew", pady=10)
        self.criar_botao("Manutencao em um PC", self.manutencao_computador).grid(row=2, column=0, sticky="ew", pady=10)
        self.criar_botao("Manutencao em Todos", self.manutencao_todos).grid(row=3, column=0, sticky="ew", pady=10)
        self.criar_botao("Gerar Status", self.gerar_insights).grid(row=4, column=0, sticky="ew", pady=10)
        self.criar_botao("Gerar Graficos", self.gerar_graficos).grid(row=5, column=0, sticky="ew", pady=10)
        self.criar_botao("Pagar Conta Energia", self.pagar_energia).grid(row=6, column=0, sticky="ew", pady=10)
        self.criar_botao("Sair", self.sair, bg=EXIT_BUTTON_BG, width=15, height=2).grid(row=7, column=0, sticky="ew", pady=(30, 10))

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_rowconfigure(7, weight=1)

    def criar_botao(self, texto, comando, bg=BUTTON_BG, width=20, height=2):
        """Cria um botão com o estilo dark mode, bordas arredondadas e efeitos de hover."""
        botao = tk.Button(
            self.menu_frame, text=texto, command=comando,
            font=("Roboto", 14, "bold"), bg=bg, fg=BUTTON_FG,
            relief="flat", pady=10, width=width, height=height,
            activebackground=HOVER_BG, activeforeground=DARK_FG,
            borderwidth=0, highlightthickness=0
        )
        # Aplicando arredondamento ao botão
        botao.config(highlightbackground=bg, padx=10, pady=5)
        botao.bind("<Enter>", lambda e: botao.config(bg=HOVER_BG))
        botao.bind("<Leave>", lambda e: botao.config(bg=bg))
        return botao

    def atualizar_terminal(self):
        """Atualiza o conteúdo do terminal com a última saída."""
        output = self.terminal_output.getvalue()
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.delete(1.0, tk.END)
        self.terminal_text.insert(tk.END, output)
        self.terminal_text.config(state=tk.DISABLED)

    def avancar_tempo(self):
        horas = int(self.exibir_input_dialog("Quantas horas deseja avançar?"))
        self.simulador.avançar_tempo(horas)
        self.atualizar_terminal()

    def manutencao_computador(self):
        computador_id = int(self.exibir_input_dialog("Digite o ID do computador para manutenção:"))
        self.simulador.realizar_manutencao(computador_id)
        self.atualizar_terminal()

    def manutencao_todos(self):
        self.simulador.realizar_manutencao_em_todos()
        self.atualizar_terminal()

    def gerar_insights(self):
        self.simulador.gerar_insights()
        self.atualizar_terminal()

    def gerar_graficos(self):
        """Chama a função para gerar gráficos de lucros"""
        graficos = Graficos(self.simulador)  # Instancia a classe Graficos com o simulador
        graficos.gerar_graficos_lucros()  # Chama a função para gerar os gráficos de lucros
        self.atualizar_terminal()

    def pagar_energia(self):
        self.simulador.pagar_energia()
        self.atualizar_terminal()

    def sair(self):
        self.root.quit()

    def exibir_input_dialog(self, mensagem):
        """Exibe uma caixa de entrada para pegar a resposta do usuário."""
        resposta = simpledialog.askstring("Entrada", mensagem)
        return resposta

    def atualizar_layout(self):
        """Atualiza o layout responsivo quando em fullscreen ou janela normal."""
        if self.root.attributes("-fullscreen"):
            self.terminal_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
            self.menu_frame.grid(row=0, column=0, sticky="nsew")
            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(1, weight=2)
        else:
            self.terminal_frame.grid(row=0, column=1, sticky="nsew")
            self.menu_frame.grid(row=0, column=0, sticky="nsew")
            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(0, weight=1)
            self.root.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    # Exemplo de criação do simulador (você deve adaptar conforme a implementação real)
    simulador = Simulador()

    # Criar a janela principal do Tkinter
    root = tk.Tk()

    # Criar a interface gráfica
    app = InterfaceGrafica(root, simulador)

    # Iniciar o loop principal do Tkinter
    root.mainloop()
