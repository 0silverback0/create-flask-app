#!/usr/bin/env python3

import os
from helpers import *

def create_flask_app():
    """ creates the file strucure and boilerplates for basic flask app"""
    # make a new folder in the current directory
    # change into new folder
    # create files for root folder

    new_folder = input('Enter folder name: ')
    os.mkdir(new_folder)
    os.chdir(new_folder)
   
    root_files = ['app.py', 'requirements.txt', 'models.py', 'forms.py', 'seed.py', '.env']

    for file in root_files:
            if file == 'app.py':
                fill_app_py_file()
            elif file == 'requirements.txt':
                fill_requirements()
                pass
            elif file == 'models.py':
                fill_models()
            elif file == '.env':
                with open(file, 'w') as f:
                    f.write('FLASK_ENV=development')
            else:
                with open(file, 'w') as f:
                    pass

    
    os.mkdir('static') # make a static folder
    os.chdir('static') # change to static folder
    os.mkdir('Images') # make images folder 
    os.mkdir('Stylesheets') # make stylesheets folder inside static directory
    os.chdir('Stylesheets') # change into stylesheets and create styles.css

    with open('styles.css', 'w') as f:
        pass

    os.chdir('../..') # go back two levels and create template directory
    os.mkdir('templates') 
    os.chdir('templates') # go into templates and create index.html
    
    fill_templates_index_html()

create_flask_app()