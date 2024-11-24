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

# Cores do tema White Mode atualizadas
WHITE_BG = "#FFFFFF"  # Fundo branco
WHITE_FG = "#FFD700"  # Texto dourado
WHITE_LIGHT_BG = "#F0F0F0"  # Cor de fundo para caixas de texto e botões no modo claro
WHITE_BUTTON_BG = "#FFFFFF"  # Cor de fundo dos botões no modo claro (branco)
WHITE_BUTTON_FG = "#000000"  # Cor do texto dos botões no modo claro (preto)
WHITE_HOVER_BG = "#D3D3D3"  # Cor ao passar o mouse nos botões (cinza claro)
WHITE_TITLE_COLOR = "#FFD700"  # Cor do título no modo claro (dourado)

class InterfaceGrafica:
    def __init__(self, root, simulador):
        self.root = root
        self.simulador = simulador
        self.root.title("Extrator De Criptomoeda")
        self.root.geometry("1600x900")  # Aumentando a resolução para 1600x900
        self.root.config(bg=DARK_BG)
        self.dark_mode = True  # Inicialmente, o modo escuro está ativo

        # Redirecionar a saída para o terminal (Console)
        self.terminal_output = StringIO()
        sys.stdout = self.terminal_output

        # Configuração da área de terminal
        self.terminal_frame = tk.Frame(self.root, bg=DARK_BG)
        self.terminal_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.terminal_text = tk.Text(
            self.terminal_frame, height=30, width=80,
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
        self.root.geometry("1600x900" if is_fullscreen else "1920x1080")
        self.atualizar_layout()

    def criar_menu(self):
        """Cria a interface de menu com botões responsivos."""
        self.menu_frame = tk.Frame(self.root, bg="#2C2C2C", bd=0)
        self.menu_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        titulo = tk.Label(
            self.menu_frame, text="Extrator De Criptomoeda",
            font=("Roboto", 24, "bold"), fg=WHITE_TITLE_COLOR, bg="#2C2C2C"
        )
        titulo.grid(row=0, column=0, pady=(20, 30))

        # Botões para as opções do menu, com tamanho reduzido
        self.criar_botao("Avançar no tempo", self.avancar_tempo).grid(row=1, column=0, sticky="ew", pady=8)
        self.criar_botao("Manutenção em um PC", self.manutencao_computador).grid(row=2, column=0, sticky="ew", pady=8)
        self.criar_botao("Manutenção em Todos", self.manutencao_todos).grid(row=3, column=0, sticky="ew", pady=8)
        self.criar_botao("Manutenção Preventiva em um Computador", self.manutencao_preventiva).grid(row=4, column=0, sticky="ew", pady=8)
        self.criar_botao("Gerar Status", self.gerar_insights).grid(row=5, column=0, sticky="ew", pady=8)
        self.criar_botao("Gerar Gráficos", self.gerar_graficos).grid(row=6, column=0, sticky="ew", pady=8)
        self.criar_botao("Pagar Conta Energia", self.pagar_energia).grid(row=7, column=0, sticky="ew", pady=8)
        self.criar_botao("Alternar Tema", self.alternar_tema).grid(row=8, column=0, sticky="ew", pady=8)
        self.criar_botao("Limpar Terminal", self.limpar_terminal).grid(row=9, column=0, sticky="ew", pady=8)
        self.criar_botao("Sair", self.sair, bg=EXIT_BUTTON_BG, width=20, height=2).grid(row=10, column=0, sticky="ew", pady=(30, 10))

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_rowconfigure(10, weight=1)

    def criar_botao(self, texto, comando, bg=WHITE_BUTTON_BG, width=18, height=2):
        """Cria um botão com o estilo White Mode, bordas arredondadas e efeitos de hover."""
        botao = tk.Button(
            self.menu_frame, text=texto, command=comando,
            font=("Roboto", 12, "bold"), bg=bg, fg=WHITE_BUTTON_FG,
            relief="flat", pady=10, width=width, height=height,
            activebackground=WHITE_HOVER_BG, activeforeground=WHITE_FG,
            borderwidth=0, highlightthickness=0
        )
        # Aplicando arredondamento ao botão
        botao.config(highlightbackground=bg, padx=10, pady=5)
        botao.bind("<Enter>", lambda e: botao.config(bg=WHITE_HOVER_BG))
        botao.bind("<Leave>", lambda e: botao.config(bg=bg))
        return botao

    def atualizar_terminal(self):
        """Atualiza o conteúdo do terminal com a última saída."""
        output = self.terminal_output.getvalue()
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.delete(1.0, tk.END)
        self.terminal_text.insert(tk.END, output)
        self.terminal_text.config(state=tk.DISABLED)
        self.terminal_text.see(tk.END)  # Scroll automático para o final

    def alternar_tema(self):
        """Alterna entre Dark Mode e White Mode."""
        if self.dark_mode:
            # Alterando para o modo claro (White Mode)
            self.root.config(bg=WHITE_BG)
            self.menu_frame.config(bg=WHITE_LIGHT_BG)
            self.terminal_frame.config(bg=WHITE_BG)
            self.terminal_text.config(bg=WHITE_BG, fg=WHITE_FG)
            self.terminal_text.tag_configure("stderr", foreground=ERROR_COLOR)
            self.terminal_text.tag_configure("stdout", foreground=INFO_COLOR)
            for widget in self.menu_frame.winfo_children():
                widget.config(bg=WHITE_BUTTON_BG, fg=WHITE_BUTTON_FG)
            self.dark_mode = False
        else:
            # Alterando para o modo escuro (Dark Mode)
            self.root.config(bg=DARK_BG)
            self.menu_frame.config(bg="#2C2C2C")
            self.terminal_frame.config(bg=DARK_BG)
            self.terminal_text.config(bg="#1C1C1C", fg=DARK_FG)
            self.terminal_text.tag_configure("stderr", foreground=ERROR_COLOR)
            self.terminal_text.tag_configure("stdout", foreground=INFO_COLOR)
            for widget in self.menu_frame.winfo_children():
                widget.config(bg=BUTTON_BG, fg=BUTTON_FG)
            self.dark_mode = True
        self.atualizar_terminal()

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

    def manutencao_preventiva(self):
        """Realiza a manutenção preventiva em um computador específico."""
        try:
            computador_id = int(self.exibir_input_dialog("Digite o ID do computador (1 a 5) para manutenção preventiva:"))
            if 1 <= computador_id <= 5:
                computador = self.simulador.computadores[computador_id - 1]
                computador.manutencao_preventiva()  # Chama a manutenção preventiva
                self.atualizar_terminal()
            else:
                print("ID inválido! O ID do computador deve ser entre 1 e 5.")
                self.atualizar_terminal()
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o ID do computador.")
            self.atualizar_terminal()

    def gerar_insights(self):
        """Gera insights baseados no estado atual do simulador."""
        self.simulador.gerar_insights()
        self.atualizar_terminal()

    def gerar_graficos(self):
        """Chama a função para gerar gráficos de lucros."""
        graficos = Graficos(self.simulador)  # Instancia a classe Graficos com o simulador
        graficos.gerar_graficos_lucros()  # Chama a função para gerar os gráficos de lucros
        self.atualizar_terminal()

    def pagar_energia(self):
        """Realiza o pagamento da conta de energia."""
        self.simulador.pagar_energia()
        self.atualizar_terminal()

    def limpar_terminal(self):
        """Limpa o terminal."""
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.delete(1.0, tk.END)
        self.terminal_text.config(state=tk.DISABLED)

    def sair(self):
        """Finaliza o programa."""
        self.root.quit()

    def exibir_input_dialog(self, prompt):
        """Exibe um dialog de entrada para coletar um valor do usuário."""
        return simpledialog.askstring("Entrada", prompt, parent=self.root)

    def atualizar_layout(self):
        """Atualiza o layout do menu quando o tamanho da janela muda."""
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_rowconfigure(10, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    simulador = Simulador()  
    app = InterfaceGrafica(root, simulador)
    root.mainloop()