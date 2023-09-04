import csv

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaHeroes:
    def __init__(self):
        self.tabela_hash = [[] for _ in range(26)]  # Inicializa a tabela hash com 26 listas vazias

    def calcular_indice(self, letra):
        # Converte a letra para um número (A=0, B=1, ..., Z=25)
        return ord(letra.upper()) - ord('A')

    def adicionar_contato(self, contato):
        indice = self.calcular_indice(contato.nome[0])
        self.tabela_hash[indice].append(contato)

    def buscar_contato(self, nome):
        indice = self.calcular_indice(nome[0])
        for contato in self.tabela_hash[indice]:
            if contato.nome == nome:
                return contato
        return None

    def listar_contatos_por_letra(self, letra):
        indice = self.calcular_indice(letra)
        return self.tabela_hash[indice]

    def remover_contato(self, nome):
        indice = self.calcular_indice(nome[0])
        for contato in self.tabela_hash[indice]:
            if contato.nome == nome:
                self.tabela_hash[indice].remove(contato)
                return True
        return False

    def importar_contatos(self, arquivo):
        with open(arquivo, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                nome, telefone = row
                contato = Contato(nome, telefone)
                self.adicionar_contato(contato)

if __name__ == "__main__":
    agenda = AgendaHeroes()

    # Importe os contatos do arquivo 'agenda.csv'
    agenda.importar_contatos('agenda.csv')

    while True:
        print("\nMenu Interativo:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Listar Contatos por Letra")
        print("4. Remover Contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            contato = Contato(nome, telefone)
            agenda.adicionar_contato(contato)
            print("Contato adicionado com sucesso!")

        elif escolha == "2":
            nome = input("Digite o nome do contato que deseja buscar: ")
            contato = agenda.buscar_contato(nome)
            if contato:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
            else:
                print("Contato não encontrado.")

        elif escolha == "3":
            letra = input("Digite a letra inicial para listar os contatos: ")
            contatos = agenda.listar_contatos_por_letra(letra)
            if contatos:
                for contato in contatos:
                    print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
            else:
                print("Nenhum contato encontrado com essa letra inicial.")

        elif escolha == "4":
            nome = input("Digite o nome do contato que deseja remover: ")
            if agenda.remover_contato(nome):
                print(f"Contato {nome} removido com sucesso!")
            else:
                print("Contato não encontrado.")

        elif escolha == "5":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
