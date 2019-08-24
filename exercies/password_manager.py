
PASSWORD = {"user":None,"password":None,"passwords":{}}

def register():
    user = input("Podaj nazwę użtkownika:")
    password = input("Podaj hasło:")
    PASSWORD["user"] = user
    PASSWORD["password"] = password

register()

def add_password(item,password):

    PASSWORD["passwords"][item] = password



