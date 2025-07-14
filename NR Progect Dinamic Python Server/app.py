from flask import Flask, jsonify, send_from_directory, render_template_string, request
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
    import threading
    import requests
    import time

    port = 8080  # qui e dove puoi cambiare la porta predefinita
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number '{sys.argv[1]}', using default port {port}")

    @app.route('/shutdown', methods=['POST'])
    def shutdown():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            return "Not running with the Werkzeug Server", 500
        func()
        return "Server shutting down..."

    import socket

    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # non deve essere raggiungibile
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def run_app():
        local_ip = get_local_ip()
        url_localhost = f"http://127.0.0.1:{port}" # url per accedere al server tramite localhost
        url_network = f"http://{local_ip}:{port}" # url per accedere al server tramite la rete
        print(f" * Running on {url_localhost} (clickable link)") # url per accedere al server tramite localhost
        print(f" * Also accessible on your network at: {url_network}") # url per accedere al server tramite la rete
        app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)  # serve il server con debug disattivato

    server_thread = threading.Thread(target=run_app)
    server_thread.start()

    try:
        while True:
            command = input()
            if command.strip().lower() == 'stop':
                print("Stopping server...")
                try:
                    requests.post(f"http://127.0.0.1:{port}/shutdown")
                except requests.exceptions.RequestException:
                    pass
                print("Server stopped correctly.")
                break
    except KeyboardInterrupt:
        print("Keyboard interrupt received, stopping server...")

    server_thread.join()
