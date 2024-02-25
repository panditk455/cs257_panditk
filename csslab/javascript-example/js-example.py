from flask import Flask, render_template

app = Flask(__name__)

@app.route('/RandomColorAndNumber')
def welcome():
    message = "Welcome to Kritika's Website."
    message = message + " We are generating Random numbers with different colors."
    return render_template("homepage.html", someText = message)

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port = my_port) 
