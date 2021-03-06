import click as cli
from commands.version import VersionCommand
from commands.info import InfoCommand

# App Declaration
@cli.group()
def app():
    pass

# VERSION COMMAND 
@app.command('version', short_help='Show Moldy Version')
def version():
    """
    Show the version of Moldy
    """
    VersionCommand()
# INFO COMMAND
@app.command('info', short_help = 'Show the information About Moldy')
def information():
    """
    Show the authors, Description and Contact of Moldy Project
    """
    InfoCommand()
    
if __name__ == '__main__':
    app()