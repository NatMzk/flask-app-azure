from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if operation == 'Sum':
        result = var_1 + var_2
    elif operation == 'Substract':
        result = var_1 - var_2
    elif operation == 'Multiply':
        result = var_1 * var_2
    elif operation == 'Divide':
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)
