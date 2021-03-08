import click as cli
from commands.version import VersionCommand
from commands.info import InfoCommand
from commands.install import *
from commands.init import InitProjectMoldy
from commands.new import NewMoldyFile
from commands.dependencies import InstallDependencies

# App Declaration
@cli.group()
def app():
    """
    The best tool for initial his project :

    Moldy is a Project Starter writed in python that help for
    start his project and is 100% OPEN SOURCE.

    Author: Moldy Community
    Contact mail: moldycommunity@gmail.com
    Repository: www.github.com/Moldy/Cli
    Web Page: www.moldy.github.io

    -----------------------------

    Made with love in Ecuador and Colombia.
    """
    pass


# VERSION COMMAND
@app.command("version", short_help="Show Moldy Version")
def version():
    """
    Show the version of Moldy
    """
    VersionCommand()


# INFO COMMAND
@app.command("info", short_help="Show the information About Moldy")
def information():
    """
    Show the authors, Description and Contact of Moldy Project
    """
    InfoCommand()


# INSTALL COMMAND
@app.command("install", short_help="Help You for install a moldy package from Github ")
@cli.option("-gh", "--github", help="Install a package from GitHub")
def installGithub(github, gitlab, url):
    """
    Install the moldy packages using this command **moldy install -gh UserName/UserRepository** from github
    --------------------------------------------------------------
    """
    InstallCommandGitHub(github)


@app.command("custom", short_help="Help for install a moldy package for a custom url")
@cli.option("-u", "--url", help="Install a package from Custom URL")
def custom(url):
    """
    Install the moldy packages using this command **moldy install -u UserName/UserRepository** from custom url
    --------------------------------------------------------------
    """
    InstallCommandURL(url)


# INITIAL A PACKAGE
@app.command("new", help="Initial a template for make a package in Moldy")
def initial():
    """
    Initial a template for make a moldy package he helps generated a Moldy.yaml File
    """
    InitProjectMoldy()


@app.command("init", help="Initial a base template for install from Moldy.yaml file")
def new():
    """
    Initial a Moldy.yaml file for install more dependencies
    """
    NewMoldyFile()


@app.command("dependencies", help="Install the dependencies from Moldy.yaml file")
def dependencies():
    """
    Install the dependencies from the Moldy.yaml file
    """
    InstallDependencies()


if __name__ == "__main__":
    app()
