from flask import Flask, render_template, request
from dadjokes import Dadjoke, DadjokeSearch

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def test():
    return render_template('test_html.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   # if request.method == 'POST':
      # result = request.form
    data_str = 'my test data'
    dadjoke = Dadjoke()
    print(dadjoke.joke)
    joke_str = dadjoke.joke
    return render_template("result.html", data = joke_str)

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('result.html', forward_message=forward_message)

@app.route("/items", methods=['GET', 'POST'])
def items():
    dadjoke = Dadjoke()
    print(dadjoke.joke)
    joke_str = dadjoke.joke
    return render_template("result.html", data = joke_str)

@app.route("/items_form", methods=['GET', 'POST'])
def items_form():
    if request.method == "POST":
        my_term = request.form.get("termInput")
        my_limit = request.form.get("rangeInput")
        print(my_term, my_limit)
        search = DadjokeSearch(term=str(my_term), limit=int(my_limit))

    return render_template("result.html", jokes = search)

@app.route("/jokes", methods=['GET', 'POST'])
def jokes():
    dadjoke = Dadjoke()
    print(dadjoke.joke)
    joke_str = dadjoke.joke
    return render_template("test_html.html", data = joke_str)

if __name__ == '__main__':
    app.run()