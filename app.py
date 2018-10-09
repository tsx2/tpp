from flask import Flask
from flask_script import Manager,Server
from flask_migrate import MigrateCommand


from apps import create_app
from apps.settings import DEVELOP

app=create_app(DEVELOP)

manager=Manager(app)
manager.add_command('start',Server(port=8000))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
