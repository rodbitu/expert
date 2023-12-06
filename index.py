class AssistenteSuporteTecnico:
    def __init__(self):
        self.categorias_problemas = ["Hardware", "Software", "Rede"]
        self.perguntas_iniciais = [
            "Em uma escala de 1 a 5, o quanto você está enfrentando problemas com o hardware?",
            "Em uma escala de 1 a 5, o quanto você está enfrentando problemas com o software?",
            "Em uma escala de 1 a 5, o quanto você está enfrentando problemas com a rede?"
        ]
        self.perguntas_hardware = [
            "Em uma escala de 1 a 5, o computador está fazendo barulhos estranhos?",
            "Em uma escala de 1 a 5, o computador está superaquecendo?",
            "Em uma escala de 1 a 5, há problemas com as conexões externas?",
            "Em uma escala de 1 a 5, o computador está reiniciando sozinho?"
        ]
        self.perguntas_software = [
            "Em uma escala de 1 a 5, o software está travando frequentemente?",
            "Em uma escala de 1 a 5, há problemas com a instalação de programas?",
            "Em uma escala de 1 a 5, o sistema operacional está atualizado?",
            "Em uma escala de 1 a 5, você está tendo problemas com vírus ou malware?"
        ]
        self.perguntas_rede = [
            "Em uma escala de 1 a 5, a internet está lenta?",
            "Em uma escala de 1 a 5, há problemas para conectar à rede Wi-Fi?",
            "Em uma escala de 1 a 5, a conexão está caindo frequentemente?",
            "Em uma escala de 1 a 5, há problemas com a configuração de rede?"
        ]

    def fornecer_solucao(self, categoria):
        if categoria == "Hardware":
            return (
                "Parece que você tem um problema de Hardware. Verifique se todos os cabos estão conectados corretamente, se o computador está limpo e livre de poeira, e se os componentes internos não estão superaquecendo."
            )
        elif categoria == "Software":
            return (
                "Seu problema parece ser de Software. Certifique-se de que todos os programas estão atualizados, faça uma varredura completa com um antivírus e verifique se não há conflitos de software ou problemas de drivers."
            )
        else:
            return (
                "Você está enfrentando problemas de Rede. Tente reiniciar o roteador, verifique se a senha da Wi-Fi está correta e confira as configurações de rede no seu dispositivo."
                )

    def fazer_pergunta(self, pergunta):
        while True:
            resposta = input(
                f"{pergunta} (Digite um número de 1 a 5, onde 1 é pouca severidade e 5 é muita severidade): ")
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
        severidades = [0, 0, 0]  # Severidades para hardware, software e rede
        for i, pergunta in enumerate(self.perguntas_iniciais):
            resposta = self.fazer_pergunta(pergunta)
            severidades[i] += resposta

        # Determinar a categoria de problema com maior severidade
        categoria_maior_severidade = self.categorias_problemas[severidades.index(max(severidades))]
        if categoria_maior_severidade == "Hardware":
            perguntas = self.perguntas_hardware
        elif categoria_maior_severidade == "Software":
            perguntas = self.perguntas_software
        else:
            perguntas = self.perguntas_rede

        # Fazer perguntas específicas da categoria
        for pergunta in perguntas:
            resposta = self.fazer_pergunta(pergunta)
            severidades[self.categorias_problemas.index(categoria_maior_severidade)] += resposta

        categoria_problema = self.categorias_problemas[severidades.index(max(severidades))]

        print(self.fornecer_solucao(categoria_problema))


assistente = AssistenteSuporteTecnico()
assistente.interagir()
