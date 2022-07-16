#flask run --reload
#Importing Blueprint and render_template
from flask import (Blueprint, render_template)
import json
#Underneath that, we can open() the pets.json file by passing it as an argument.
#Once that file is opened, however, it still isn't readable for Python. This is where json comes in. Pass the entire open function as an argument to json.load().
#Save that decoded JSON file to a variable. Let's name it pets.
pets = json.load(open('pets.json'))
#To ensure we loaded it in correctly, print the pets variable. Once you save the file, you should see the data in terminal.
#print(pets)

#Create a new instance of Blueprint and save it to a variable called bp.
'''
Remember, creating a new blueprint instance requires three arguments:
    The name of the blueprint. Let's name ours pet.
    The location of the blueprint. We can just use the handy __name__.
    The URL prefix that should be used for all routes attached to this blueprint. Let's go with /pets.
'''
bp = Blueprint('pet', __name__, url_prefix="/pets")

#Define a route on the blueprint instance that goes to '/'.
@bp.route('/')
#Define a method for the route named index.
def index(): 
    #In the index method, return a string (for example: 'This is the pets index'). This is just for testing purposes.
    #returning render_template from index.html file
    #In the index route method, pass the render_template a second argument. Let's name it pets as well and pass it the pets variable that we just loaded with data.
    #Now in templates/index.html, we can loop through the data using the pets variable.
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')#int accepts positive integers
def show(id):
    pet = pets[id -1]
    return render_template('pets/show.html', pet=pet)

