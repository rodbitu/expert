class BaseConhecimento:
    def __init__(self):
        self.conhecimento = {
            'não liga': {
                'mensagem_erro': {
                    'sim': 'Pesquise o erro específico ou contate o suporte do software.',
                    'não': 'Tente reiniciar o dispositivo.'
                },
                'sem_mensagem_erro': 'Verifique se está corretamente ligado à fonte de energia.'
            },
            'problema_software': {
                'reiniciar': {
                    'sim': 'Reinstale o software problemático.',
                    'não': 'Reinicie o dispositivo.'
                },
                'sem_reiniciar': 'Verifique atualizações disponíveis para o software.'
            },
            'internet_lenta': {
                'router_reiniciado': {
                    'sim': 'Verifique se outros dispositivos também estão com internet lenta. Se sim, pode ser um problema com seu provedor de internet.',
                    'não': 'Tente reiniciar o router.'
                },
                'sem_router_reiniciado': 'Verifique se há muitos dispositivos conectados à mesma rede.'
            },
            'tela_azul': {
                'software_recente': {
                    'sim': 'Desinstale o software recentemente adicionado e veja se o problema persiste.',
                    'não': 'Tente atualizar seus drivers e o sistema operacional.'
                },
                'sem_software_recente': 'Considere realizar uma restauração do sistema para um ponto anterior ao início do problema.'
            }
            # Adicione mais cenários conforme necessário
        }

    def obter_solucao(self, problema, respostas):
        solucao = self.conhecimento
        for resposta in respostas:
            solucao = solucao.get(resposta, {})
        return solucao if isinstance(solucao,
                                     str) else "Não consegui diagnosticar o problema. Por favor, contate um técnico especializado."


class AssistenteSuporteTecnico:
    def __init__(self):
        self.base_conhecimento = BaseConhecimento()
        self.perguntas = {
            'nível_1': "Qual é o problema do dispositivo? (1: Não liga, 2: Problema de software, 3: Internet lenta, 4: Tela azul)",
            'não liga': "O dispositivo está ligando? (Sim/Não)",
            'problema_software': "Você já tentou reiniciar o dispositivo? (Sim/Não)",
            'internet_lenta': "Você já reiniciou o router? (Sim/Não)",
            'tela_azul': "Você instalou algum software recentemente? (Sim/Não)",
            # Adicione mais perguntas conforme necessário
        }

    def interagir(self):
        print("Olá! Sou o Assistente de Suporte Técnico. Vou te ajudar a diagnosticar o problema do seu dispositivo.")
        problemas = {'1': 'não liga', '2': 'problema_software', '3': 'internet_lenta', '4': 'tela_azul'}
        problema_escolhido = problemas[input(self.perguntas['nível_1'] + " ")]

        respostas = []
        for chave in [problema_escolhido, problema_escolhido]:
            resposta = input(self.perguntas[chave] + " ").lower()
            chave_resposta = 'mensagem_erro' if chave == 'não liga' and resposta == 'sim' else resposta
            respostas.append(chave_resposta)

        sugestao = self.base_conhecimento.obter_solucao(problema_escolhido, respostas)
        print(f"Sugestão: {sugestao}")


assistente = AssistenteSuporteTecnico()
assistente.interagir()
