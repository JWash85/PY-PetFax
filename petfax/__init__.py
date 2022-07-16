#APPLICATION FACTORY:

#imported flask                  
from flask import Flask
#Define a function that will be our application factory. Let's call it create_app.
def create_app():
    #Inside that function, create a new app instance of Flask.
    app = Flask(__name__)
    #Still inside the function, create a basic index route that goes to '/' and just returns 'Hello, PetFax!' as a string.
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    #Above where we return the app in create_app, import the pet file.
    from . import pet
    #Underneath that, call the register_blueprint method on the app instance.
    app.register_blueprint(pet.bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    #Lastly, don't forget to return the app instance at the end of the factory.
    return app