import glob
from colorama import init, Fore
import yaml
from os import getcwd
from .install import InstallCommandURL


def InstallDependencies():
    try:
        directory = getcwd()
        MoldyYamlRoute = glob.glob(f"{directory}/*.yaml")
        MoldyYaml = MoldyYamlRoute[0]
        with open(MoldyYaml, "r") as f:
            global MoldyFile
            MoldyFile = yaml.load(f, Loader=yaml.FullLoader)
        index = MoldyFile[0]
        packages = index["packages"]
        urlPackage = packages["url"]
        InstallCommandURL(urlPackage)
        print(Fore.CYAN + "Succesfuly installed the dependencies")
    except Exception as err:
        print(Fore.RED+'Error: '+ err)