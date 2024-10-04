from flask import Flask, request, redirect

app = Flask(__name__)

# Lista para armazenar as mensagens (em memória)
messages = []

@app.route('/')
def index():
    # HTML gerado diretamente no Python
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat Anônimo</title>
    </head>
    <body>
        <h1>Chat Anônimo</h1>
        <form method="POST" action="/send">
            <label for="username">Nome:</label>
            <input type="text" id="username" name="username" required><br>
            
            <label for="message">Mensagem:</label>
            <textarea id="message" name="message" required></textarea><br>
            
            <input type="submit" value="Enviar">
        </form>

        <h2>Mensagens</h2>
        <ul>
    """
    
    # Adicionando as mensagens na lista para o HTML
    for msg in messages:
        html += f"<li>{msg}</li>"
    
    html += """
        </ul>
    </body>
    </html>
    """
    
    return html

@app.route('/send', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    
    # Adiciona a mensagem à lista
    messages.append(f"{username}: {message}")
    
    # Redireciona para a página inicial para mostrar as mensagens
    return redirect('/')

if __name__== '__main__':
    app.run(debug=True)