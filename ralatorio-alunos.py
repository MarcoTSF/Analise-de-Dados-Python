class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = {}
        self.faltas = 0

    def adicionar_nota(self, disciplina, nota):
        self.notas[disciplina] = nota

    def adicionar_falta(self):
        self.faltas += 1

    def calcular_media(self):
        if not self.notas:
            return None
        return sum(self.notas.values()) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media is None:
            return "Sem notas registradas"
        return "Aprovado" if media >= 7.0 else "Reprovado"

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - Curso: {self.curso}"

# Função para gerar um relatório de desempenho
def relatorio_desempenho(alunos):
    print("Relatório de Desempenho:")
    for aluno in alunos:
        print(f"\n{aluno}")
        for disciplina, nota in aluno.notas.items():
            print(f"   {disciplina}: {nota}")
        print(f"   Faltas: {aluno.faltas}")
        print(f"   Média: {aluno.calcular_media()}")
        print(f"   Situação: {aluno.verificar_aprovacao()}")

# Exemplo de uso
aluno1 = Aluno("João", "123", "Engenharia")
aluno2 = Aluno("Maria", "456", "Ciência da Computação")

# Registro de notas e faltas
aluno1.adicionar_nota("Matemática", 8.5)
aluno1.adicionar_nota("Física", 7.0)
aluno1.adicionar_falta()

aluno2.adicionar_nota("Matemática", 6.0)
aluno2.adicionar_nota("Física", 7.5)

lista_alunos = [aluno1, aluno2]

relatorio_desempenho(lista_alunos)