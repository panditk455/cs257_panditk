from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Rockpaperscissors')
def welcome():
    return render_template("homepage.html")

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port=my_port)
