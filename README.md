# flasklite

flasklite is meant to provide a simple structure for Flask projects.

## How to Run flasklite
> 1. Clone repository: <code>git clone https://www.github.com/sampson-q/flasklite</code>
> 2. Change into the cloned directory
> 3. Run setup.py: <code>python setup.py install</code>
> 4. run flasklite (with options)<br>
>> <pre>
>> Usage: flasklite [options], flasklite -p projectname
>> 
>> options:             description:
>> -h, --help           display help of this command
>> -p [projectname]     creates a new project
>> </pre>

## Intended Structure of flasklite
<pre>
  projectname\
  |
  +---> projectnameApp\
  |   |
  |   +---> static\
  |   |
  |   +---> templates\
  |   |    |
  |   |    +---> base.html
  |   |
  |   +---> __init__.py
  |   +---> auth.py
  |   +---> views.py
  |
  +---> main.py
</pre>

## Requirements to Use flasklite
> 1. Python 3 (must be added to path)
> 2. Flask
> 3. Flask-Login
> 4. pip

## Inside flasklite.py
    # Author: Hash 👽

    import os, subprocess, sys, secrets

    pythonVersion = subprocess.check_output("python --version", shell=True, universal_newlines=True)
    pipList = subprocess.check_output("pip install Flask", shell=True, universal_newlines=True)

    def displayError():
        print('\nUsage: flasklite [options]\n\noptions:\t\tdescription\n-h, --help\t\tdisplay help of this command\n-p\t\t\tcreates a new project: flasklite -p projectname')
        print('\nNote:\tThis command aims at creating a simple structure for your Flask project.\n\tLog your challenges at https://www.github.com/sampson-q/flasklite/issues.\n\tFor further information about Flask, read the documentation on Flask at https://flask.palletsprojects.com/')

    if pythonVersion[:10] != 'Python was':
        # print('Python installed. Check for Flask')
        if pipList[:30] != 'Requirement already satisfied:':
            print('Flask not installed. Try running \'pip install Flask\' to download Flask')
        elif pipList[:4] == '\'pip\'':
            print('pip is not recognized in your system. Try adding it to your environment variables')
        else:
            try:
                if sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] != '-p':
                    displayError()
                else:
                    if sys.argv[1] == '-p' and sys.argv[2] != '':
                        cd = os.getcwd() + '\\' + sys.argv[2]
                        os.mkdir(cd)

                        # create the project with the main.py file
                        createMainPY = 'type nul > {}\\main.py'.format(cd)
                        os.system(createMainPY)
                        with open(cd + '\\main.py', 'w') as writeMainPY:
                            writeMainPY.write('from {}App import create_app\n\napp = create_app()\n\nif __name__ == \'__main__\':\n\tapp.run(debug=True)'.format(sys.argv[2]))

                        cd += '\\{}App'.format(sys.argv[2])
                        os.mkdir(cd)

                        # create the static folder
                        os.mkdir(cd + '\\static')

                        # create the templates folder with base.html file
                        os.mkdir(cd + '\\templates')
                        with open(cd + '\\templates\\base.html', 'w') as writeBaseHTML:
                            writeBaseHTML.write('<h1>Your website, {} is live now. You made it! Edit this template file to suit your desire</h1>'.format(sys.argv[2]))

                        # create the __init__ file
                        with open(cd + '\\__init__.py', 'w') as writeInitPY:
                            writeInitPY.write('from flask import Flask\n\ndef create_app():\n\tapp = Flask(__name__)\n\tapp.config[\'SECRET_KEY\'] = \'{}\'\n\n\tfrom .views import views\n\tfrom .auth import auth\n\n\tapp.register_blueprint(views, url_prefix=\'/\')\n\tapp.register_blueprint(auth, url_prefix=\'/\')\n\n\treturn app'.format(secrets.token_hex(32)))

                        # create the auth file
                        with open(cd + '\\auth.py', 'w') as writeAuthPY:
                            writeAuthPY.write('from flask import Blueprint\n\nauth = Blueprint(\'auth\', __name__)\n\n# create your routes here.\n\n# @auth.route(\'/login\')\n# def login():\n#\treturn "<p>Login here</p>"')

                        # create the models file


                        # create the vies file
                        with open(cd + '\\views.py', 'w') as writeViewsPY:
                            writeViewsPY.write('from flask import Blueprint, render_template\n\nviews = Blueprint(\'views\', __name__)\n\n@views.route(\'/\')\ndef home():\n\treturn render_template(\'base.html\')')

                        print('{} project created successfully. \nNote:\tThis command aims at creating a simple structure for your Flask project.\n\tLog your challenges at https://www.github.com/sampson-q/flasklite/issues.\n\tFor further information about Flask, read the documentation on Flask at https://flask.palletsprojects.com/'.format(sys.argv[2]) + '\n')
                    else:
                        displayError()

            except IndexError as e:
                displayError()
    else:
        print('Python not installed. Get latest version at https://www.python.org/downloads/ to be able to run this script. Enable path during installation')

## Compile flasklite.py
### Packages Used (for compilation):
> 1. pyinstaller

### Packages used (in code):
> 1. os
> 2. subprocess
> 3. sys
> 4. secrets
