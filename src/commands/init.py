import yaml
from colorama import init, Fore
import secrets


def InitProjectMoldy():
    init(autoreset=True)
    packagename = input("What is the name of the Moldy package? ")
    authorpackage = input("What is the author of the Moldy package? ")
    versionpackage = input("What is the version of the Moldy package? ")
    hashofpackage = secrets.token_hex(nbytes=16)
    templateText = [
        {
            "package": [
                f"name: {packagename}",
                f"author: {authorpackage}",
                f"version: {versionpackage}",
                f"hash: {hashofpackage}",
            ]
        }
    ]
    try:
        with open("MoldySpecs.yaml", "w") as f:
            yaml.dump(templateText, f)

        print(Fore.CYAN + "Created the MoldySpecs.yaml file")
    except Exception as err:
        print(Fore.RED + "Error: " + err)
