from flask import Flask, request, jsonify, send_from_directory, abort
import os

app = Flask(__name__)

hidden_dirs = {
    'admin': 'admin/',
    'config': 'config/',
    'secret': 'secret/flag.txt',  
    'uploads': 'uploads/',
    'logs': 'logs/',
}

for directory, path in hidden_dirs.items():
    os.makedirs(os.path.dirname(path), exist_ok=True) 
    if directory == 'secret' and not os.path.exists(path):  
        with open(path, 'w') as f:
            f.write("isfcr{y0u_c@5_br0tef0rc5}")

@app.route('/', methods=['GET'])
def index():
    return "Im hidden somewhere,find me if u can"

@app.route('/directories', methods=['GET'])
def list_directories():
    return jsonify(list(hidden_dirs.keys()))

@app.route('/<directory>', methods=['GET'])
def get_directory(directory):
    if directory in hidden_dirs:
        files = os.listdir(os.path.dirname(hidden_dirs[directory])) 
        return jsonify({"directory": directory, "files": files}), 200
    else:
        return jsonify({"message": "Directory not found."}), 404


@app.route('/<path:filename>', methods=['GET'])
def serve_file(filename):
    for dir_name in hidden_dirs.keys():
        if filename.startswith(dir_name):
            try:
                return send_from_directory(os.path.dirname(hidden_dirs[dir_name]), filename[len(dir_name)+1:])
            except FileNotFoundError:
                continue
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)