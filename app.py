from flask import Flask, render_template, request

import ser


app = Flask(__name__)




@app.route('/')
def home():
    
    data = request.args.get('url')
    if data:
        return render_template('index.html')
    else:
        return render_template('error/index.html')



@app.route('/url')
def url():
    url = request.args.get('url')
    point = request.args.get('p')
    typ = request.args.get('t')
    if point and url and typ:
        ser.add_url(url,point,typ)
        return "add"
    else:
        return render_template('error/index.html')



if __name__ == '__main__':
    app.run()
