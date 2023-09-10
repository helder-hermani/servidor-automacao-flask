from colorama import init, Fore, Back, Style
init()

def p(msg, style=None):
    if (style == 'primary'):
        text = (Fore.BLUE + msg + Fore.RESET)
    if (style == 'warning'):
        text = (Fore.YELLOW + msg + Fore.RESET)
    if (style == 'success'):
        text = (Fore.GREEN + msg + Fore.RESET)
    if (style == 'danger'):
        text = (Fore.RED + msg + Fore.RESET)
    if (style == 'bold'):
        text = (Style.BRIGHT + msg + Style.RESET_ALL)
    if (style == None):
        text = (Fore.WHITE + msg + Fore.RESET)

    print(text)
