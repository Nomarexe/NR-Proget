from flask import Flask, jsonify, send_from_directory, render_template_string
import os
import re

app = Flask(__name__, static_folder='')

ARTICLES_DIR = 'Article'
ARTICLES_HTML = 'articles.html'

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return os.path.basename(file_path)

@app.route('/')
def serve_articles_html():
    with open(ARTICLES_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template_string(content)

@app.route('/api/articles')
def list_articles():
    articles = []
    for filename in sorted(os.listdir(ARTICLES_DIR)):
        if filename.endswith('.html'):
            filepath = os.path.join(ARTICLES_DIR, filename)
            title = extract_title(filepath)
            articles.append({'filename': filename, 'title': title})
    return jsonify(articles)

@app.route('/Article/<path:filename>')
def serve_article_file(filename):
    return send_from_directory(ARTICLES_DIR, filename)

if __name__ == '__main__':
    import sys
    port = 8080  # qui e dove puoi cambiare la porta predefinita
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number '{sys.argv[1]}', using default port {port}")
    url = f"http://127.0.0.1:{port}"
    print(f" * Running on {url} (clickable link)")
    app.run(debug=True, port=port)
