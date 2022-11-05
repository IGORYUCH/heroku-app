from flask import Flask, request, make_response, jsonify, redirect, url_for, render_template, send_file
from requests import get
app = Flask(__name__)
# fast-savannah 54.211.78.29
@app.route('/')
def index():
    return render_template('docs.html')


@app.route('/ip')
def getIp():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    result = get("https://api.myip.com", headers=headers)
    return jsonify(result.json())

@app.route('/file')
def getFile():
    return send_file("static/DJI_0023.JPG")

#ci
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=80)