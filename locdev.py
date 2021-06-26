from flask import Flask
from app import app,db
from login import api_login


app.register_blueprint(api_login)




if __name__ == '__main__':
    app.run(debug=True)