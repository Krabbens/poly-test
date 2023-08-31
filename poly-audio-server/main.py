from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/mp3/<path:path>')
def send_mp3(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)