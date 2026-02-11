"""
Aplicación Flask con vulnerabilidad XSS (Cross-Site Scripting)
ADVERTENCIA: Este código es intencionalmente inseguro para propósitos educativos
NO usar en producción
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Plantilla HTML vulnerable - NO sanitiza el input del usuario
VULNERABLE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aplicación Vulnerable XSS</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; background: #f0f0f0; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Buscador Vulnerable</h1>
        <form method="GET" action="/">
            <input type="text" name="search" placeholder="Ingresa tu búsqueda...">
            <button type="submit">Buscar</button>
        </form>
        
        {% if search_term %}
        <div class="result">
            <h3>Resultados para: {{ search_term|safe }}</h3>
            <p>No se encontraron resultados.</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def search():
    # VULNERABILIDAD: El parámetro 'search' se toma directamente sin validación
    search_term = request.args.get('search', '')
    
    # VULNERABILIDAD: Se usa |safe que deshabilita el auto-escape de Jinja2
    # Esto permite que código JavaScript malicioso se ejecute
    return render_template_string(VULNERABLE_TEMPLATE, search_term=search_term)

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    """Otra vulnerabilidad XSS en comentarios"""
    comment_text = request.args.get('comment', '')
    
    # VULNERABILIDAD: Concatenación directa de HTML sin sanitización
    html = f"""
    <html>
        <body>
            <h2>Tu comentario:</h2>
            <div>{comment_text}</div>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    # VULNERABILIDAD ADICIONAL: Debug mode en True expone información sensible
    app.run(debug=True, host='0.0.0.0', port=5000)
