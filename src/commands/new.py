from colorama import init, Fore
import yaml


def NewMoldyFile():
    init(autoreset=True)
    templateText = [
        {
            "moldyconfig": {"version": "Moldy 1.0  Alpha"},
            "packages": {
                "url": "https://www.github.com/Moldy-Community/HTML-Template",
                "github": "Moldy-Community/HTML-Template",
            },
        }
    ]
    try:
        with open("Moldy.yaml", "w") as f:
            yaml.dump(templateText, f)
        print(Fore.CYAN + "Created the Moldy.yaml file")
    except Exception as err:
        print(Fore.RED + "Error: " + err)
