
from colorama import Fore, Style, init #nesta parte foram colocados as bibliotecas? não funcionou de primeiro mometno pois não estavam isntalado sas bibliotecasnecessárias
print("**********Simulador de Níveis do Reservatório*********")
print("*******************")
# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com as mensagens dos níveis do reservatório ( precisei da ajuda da Ia para fazer essa parte pois não esstava funcionando)
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função que escolhe a cor conforme o nível (errei na hora de colocar a função, mas consegui corrigir com a ajuda da IA. A organização ficou melhor)
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED #letras das cores deu erro usando letras maiúsculas, mas consegui corrigir com a ajuda da IA    
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação dos níveis registrados -  a lógica de repetição foi feita com a ajuda da IA, pois não estava funcionando corretamente. PQP, praticamente a IA fez tudo. Errei muito nessa atividade! Preciso revisar os conceitos básicos)
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)
