#****By default, Flask assumes a basic entry point file will be named app.py
#****In most cases if there is no file named that way, it will not run

#As the __init__.py configures everything, we can now import the petfax folder as a package.
#Specifically, we want to import the application factory function that we wrote. Import create_app from the petfax folder.
from petfax import create_app
app = create_app() #App Instance that invoke the create_app and saves it to a variable called app




#MODULE 5 Activity 1 below: 
'''
#Remember to push this to own repository

# config  
#imported flask                  
from flask import Flask
app = Flask(__name__)

# index route (Get Route)
#As we just learned, to create a route we need to call .route() on the app instance.
#The method expects at least one argument specifying what endpoint to use for the route. Let's just have it go to '/'
@app.route('/')
#To tell our route what to do when that endpoint is used, we need to define a method directly underneath it. Let's name our method index
def index(): 
    #Have the method simply return a string that says 'Hello, this is PetFax!'
    return 'Hello, this is PetFax!'

#in terminal type 'flask run' to run application similar to node.js npm run
#By default flask runs on port 5000 http://127.0.0.1:5000
#'flask run' does not automatically restart when a file changes run 'flask run --reload'             


# pets index route
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'
'''

