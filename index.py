import json

class AssistenteSuporteTecnico:
    def __init__(self):
        self.carregar_base_conhecimento()

    def carregar_base_conhecimento(self):
        with open('base_conhecimento.json') as file:
            self.base_conhecimento = json.load(file)

    def fornecer_solucao(self, categoria):
        return self.base_conhecimento["solucoes"][categoria]

    def fazer_pergunta(self, pergunta):
        while True:
            resposta = input(f"{pergunta} (Digite um número de 1 a 5, onde 1 é pouca severidade e 5 é muita severidade): ")
            try:
                resposta = int(resposta)
                if 1 <= resposta <= 5:
                    return resposta
                else:
                    print("Desculpe, essa não é uma opção válida.")
            except ValueError:
                print("Desculpe, não entendi. Por favor, digite um número de 1 a 5.")

    def interagir(self):
        print("Olá! Sou seu assistente de suporte técnico. Vamos diagnosticar o seu problema.")
        severidades = {categoria: 0 for categoria in self.base_conhecimento["categorias_problemas"]}
        for categoria, pergunta in self.base_conhecimento["perguntas_iniciais"].items():
            resposta = self.fazer_pergunta(pergunta)
            severidades[categoria] += resposta

        categoria_maior_severidade = max(severidades, key=severidades.get)
        for pergunta in self.base_conhecimento["perguntas_detalhadas"][categoria_maior_severidade]:
            resposta = self.fazer_pergunta(pergunta)
            severidades[categoria_maior_severidade] += resposta

        print(self.fornecer_solucao(categoria_maior_severidade))

assistente = AssistenteSuporteTecnico()
assistente.interagir()
