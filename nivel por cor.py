from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE  # qualquer outro valor

print("=== TABELA DE NÍVEIS DO RESERVATÓRIO ===")
for i in range(1, 6):
    print(niveis[i - 1])

nivel_usuario = int(input("\Digite o nível do reservatório: "))

cor = definir_cor(nivel_usuario)

if 1 <= nivel_usuario <= 5:
    mensagem = niveis[nivel_usuario - 1]
else:
    mensagem = "Nível desconhecido"

print("\
1Situação atual:")
print(cor + mensagem + Style.RESET_ALL)
