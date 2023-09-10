from colorama import init, Fore, Back, Style
init()

def p(msg, style):
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
    
    print(text)
