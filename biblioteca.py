import os

class Livro:
    lista_de_livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano_publicacao = ano_publicacao
        self._ativo = True
        Livro.lista_de_livros.append(self)

    def __str__(self):
        return f'- {self.autor.ljust(20)} | {self.titulo.ljust(25)} | {str(self.ano_publicacao).ljust(10)} | {self.emprestar}.'

    @staticmethod
    def exibir_nome_do_programa():
        os.system('cls')
        print("""
██████████████████████████████████████████████████████████████████████████████
█▄─▄███▄─▄█▄─█─▄█▄─▄▄▀██▀▄─██▄─▄▄▀█▄─▄██▀▄─█████▀▄─██▄─▄███▄─██─▄█▄─▄▄▀██▀▄─██
██─██▀██─███▄▀▄███─▄─▄██─▀─███─▄─▄██─███─▀─█████─▀─███─██▀██─██─███─▄─▄██─▀─██
▀▄▄▄▄▄▀▄▄▄▀▀▀▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀
""")

    @staticmethod
    def exibir_subtitulo(texto):
        os.system('cls')
        linha = '*' * (len(texto) + 8)
        print(linha)
        print(f'\n {texto} \n')
        print(linha)
        print()    

    #------------Ativ_02 - Print
    @staticmethod
    def print_livro():
        os.system('cls')
        print(f'\n{"Autor".ljust(20)} | {"Titulo do Livro".ljust(25)} | {"Ano de Lançamento".ljust(20)} | Status\n')
        for livro in Livro.lista_de_livros:
            print(str(livro))
        Livro.voltar_ao_menu_principal()

    #------------Ativ_03 - Status do Livro
    @property
    def emprestar(self):
        return '☑ - Emprestado' if self._ativo else '☐ - Disponível'

    def alterar_estado(self):
        self._ativo = not self._ativo
        print(f'O livro "{self.titulo}" agora está {self.emprestar}.')
        Livro.voltar_ao_menu_principal()

    #------------Ativ_04 - Verificar Disponibilidade
    @staticmethod
    def verificar_disponibilidade():
        print(f'\n{"Titulo do Livro".ljust(25)} | Status\n')
        for livro in Livro.lista_de_livros:
            print(f'{livro.titulo.ljust(25)} | {livro.emprestar}')
        Livro.voltar_ao_menu_principal()

    #------------Ativ_07 - Por data
    @staticmethod
    def verificar_disponibilidade_ano():
        try:
            ano_pesquisado = int(input('\nDigite o ano que deseja procurar: '))
            livros_encontrados = False
            for livro in Livro.lista_de_livros:
                if ano_pesquisado == livro.ano_publicacao:
                    print(f'{livro.titulo.ljust(25)} | {livro.emprestar}')
                    livros_encontrados = True
            if not livros_encontrados:
                print(f'Nenhum livro encontrado para o ano {ano_pesquisado}.')
        except ValueError:
            print("Ano inválido! Por favor, insira um número inteiro.")
        Livro.voltar_ao_menu_principal()

    #------------Extras
    @staticmethod
    def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu principal.\n')
        Livro.exibir_nome_do_programa()
        Livro.exibir_opcoes()
        Livro.escolher_opcao()

    @staticmethod
    def finalizar_app():
        print('Finalizando o app\n')

    @staticmethod
    def opcao_invalida():
        print('\nOpção Inválida!\n')
        Livro.voltar_ao_menu_principal()

    #------------Menu Principal
    @staticmethod
    def exibir_opcoes():
        opcoes = [
            '1. Listar Livros',
            '2. Verificar Disponibilidade',
            '3. Atualizar Status',
            '4. Sair'
        ]
        print("\n".join(opcoes))

    @staticmethod
    def escolher_opcao():
        try:
            # Solicita a escolha do usuário e garante que a entrada seja válida
            opcao_escolhida = int(input('Escolha uma das opções: '))
            if opcao_escolhida == 1:
                Livro.print_livro()
            elif opcao_escolhida == 2:
                Livro.exibir_opcoes_verificar()
                Livro.escolher_opcao_verificar()
            elif opcao_escolhida == 3:
                Livro.exibir_opcoes_status()
                Livro.escolher_opcao_status()
            elif opcao_escolhida == 4:
                Livro.finalizar_app()
            else:
                Livro.opcao_invalida()
        except ValueError:
            # Mensagem de erro caso a entrada não seja um número válido
            print("Opção inválida! Por favor, insira um número inteiro.")
            Livro.voltar_ao_menu_principal()

    #------------Menu Verificar
    @staticmethod
    def exibir_opcoes_verificar():
        # Exibe as opções de verificação de disponibilidade
        opcoes_verificar = [
            '\n1. Verificar por nome',
            '2. Verificar por data',
            '3. Voltar ao menu principal'
        ]
        print("\n".join(opcoes_verificar))

    @staticmethod
    def escolher_opcao_verificar():
        try:
            # Solicita ao usuário que escolha uma opção e valida a entrada
            opcao_escolhida = int(input('Escolha uma das opções: '))
            if opcao_escolhida == 1:
                Livro.verificar_disponibilidade()
            elif opcao_escolhida == 2:
                Livro.verificar_disponibilidade_ano()
            elif opcao_escolhida == 3:
                Livro.voltar_ao_menu_principal()
            else:
                Livro.opcao_invalida()  # Caso a opção não seja válida
        except ValueError:
            # Caso o usuário insira um valor que não seja um número inteiro
            print("Opção inválida! Por favor, insira um número inteiro.")
            Livro.voltar_ao_menu_principal()

    #------------Menu Status
    @staticmethod
    def exibir_opcoes_status():
        for i, livro in enumerate(Livro.lista_de_livros, start=1):
            print(f'{i}. Livro: {livro.titulo}')
        print('4. Voltar ao menu principal\n')

    @staticmethod
    def escolher_opcao_status():
        try:
            opcao_escolhida = int(input('Escolha uma das opções: '))
            if 1 <= opcao_escolhida <= len(Livro.lista_de_livros):
                Livro.lista_de_livros[opcao_escolhida - 1].alterar_estado()
            elif opcao_escolhida == 4:
                Livro.voltar_ao_menu_principal()
            else:
                Livro.opcao_invalida()
        except ValueError:
            Livro.opcao_invalida()

#------------Autores
autor1 = Livro('O poder do hábito', 'Charles Duhigg', 2012)
autor2 = Livro('+ Esperto que o diabo', 'Napoleon Hill', 2014)
autor3 = Livro('Em nome do povo', 'Bruno Perini', 2024)