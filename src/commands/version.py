from colorama import Fore, init


def VersionCommand():
    # ColoramaConfig
    init(autoreset=True)
    Appversion = "Moldy CLI Version 0.5 Alpha"
    print(Fore.CYAN + Appversion)
