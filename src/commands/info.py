from colorama import Fore, init
import pyfiglet


def InfoCommand():
    init(autoreset=True)
    MoldyDescription = """ 
    The best tool for initial his project :

    Moldy is a Project Starter writed in python that help for 
    start his project and is 100% OPEN SOURCE.

    Author: Moldy Community
    Contact mail: moldycommunity@gmail.com
    Repository: www.github.com/Moldy/Cli
    Web Page: www.moldy.github.io

    -----------------------------------------------------
    Made with love in Ecuador and Colombia.
    """
    MoldyAscii = pyfiglet.figlet_format("Moldy")

    print(Fore.BLUE + MoldyAscii)
    print(MoldyDescription)
