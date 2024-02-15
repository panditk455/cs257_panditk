import flask
import psycopg2

app = flask.Flask(__name__)

# Adding two numbers:
@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    sum = int(num1) + int(num2)
    return str(sum) 

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port = my_port) 