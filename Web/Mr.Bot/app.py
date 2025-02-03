from flask import Flask, Response, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots_txt():
    user_agent = request.headers.get('User-Agent', '').lower()

    if user_agent == 'robotbrowser':
        return render_template('./robots.txt')
    else:
        return Response('Access denied. Only users using robotbrowser are allowed.', status=403, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)