from flask import Flask, render_template, request # import the module
from werkzeug.utils import secure_filename
import os
import socket 

app=Flask(__name__) # instatiate the object

@app.route('/<name>')  # deine a route 
def variables(name): # writing the function that will return to the route
    return f'Teste: {name}'

@app.route('/', methods=['POST', 'GET'])
def index(): # note that each function must have an unique name
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    s.close()
    print(ip)
    if request.method == 'POST':
        print('Hello Post')
        arquivos = request.files.getlist('arquivo')
        for a in arquivos:
            print(secure_filename(a.filename))
            a.save(f'{os.getcwd()}/downloads/{secure_filename(a.filename)}')
        return f' <html> <head> <link rel="styleshet" type="text/css" href="/style/index.css"/> </head> <body> <img src="https://art.pixilart.com/4b680819d6447f3.gif"/> <br/> Deu certo! <a href="http://{ip}:5000">Voltar<a/> </body></html>'

    return f' <html> <head> <link rel="styleshet" type="text/css" href="/style/index.css"/> </head> <body> <form action="http://{ip}:5000" method="POST" enctype="multipart/form-data"/><label>Insira seus arquivos na caixinha</label><br/><input type="file" name="arquivo" multiple="multiple"><br/><input type="submit" value="Enviar"></form></body></html>'

if __name__=='__main__':
    app.debug=True
    print(os.getcwd())
    app.run(host="0.0.0.0")
