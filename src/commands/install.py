import os
from colorama import Fore, init
import git


def InstallCommandGitHub(package):
    # Colorama Autoreset colors
    init(autoreset=True)
    try:
        # Message for clone
        print(Fore.BLUE + "Installing **" + package + "** package")
        # Variables to clone
        directory = os.getcwd()
        urlClone = "https://github.com/" + package
        # Clone
        git.Git(directory).clone(urlClone)
        print(
            Fore.GREEN
            + "Succesfuly Installed the package from GitHub : **"
            + package
            + "**"
        )
    except Exception as err:
        print(Fore.RED + "Error: " + err)


def InstallCommandURL(package):
    # Colorama Autoreset colors
    init(autoreset=True)
    try:
        # Message for clone
        print(Fore.BLUE + "Installing **" + package + "** package")
        # Variables to clone
        directory = os.getcwd()
        urlClone = package
        # Clone
        git.Git(directory).clone(urlClone)
        print(
            Fore.GREEN
            + "Succesfuly Installed the package from a Custom URL : **"
            + package
            + "**"
        )
    except Exception as err:
        print(Fore.RED + "Error: " + err)
