from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route('/')
# def index():
#     return " <h1>Hello World! </h1>"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def success():
#     global f
#     f=request.files['file']
#     success.file_name=f.filename
#     f.save(success.file_name)
    input1 = int(request.form['value_a'])
    input2 = int(request.form['value_b'])
    oper=request.form['oper']
    if oper == '+':
        return ('<p> Addition was selected </p2><br>'
                '<p> a + b = {}</p>'.format(input1+input2))
    elif oper == '-':
        return ('<p> Subtraction was selected </p2><br>'
                '<p> a - b = {}</p>'.format(input1-input2))
    elif oper == '*':
        return ('<p> Multiplication was selected </p2><br>'
                '<p> a * b = {}</p>'.format(input1*input2))
    elif oper == '/':
        if input2 == 0:
            return ('<p> Division was selected </p2><br>'
                    '<p> a / b is not possible. Divide by zero error !!</p>')
        else:
            return ('<p> Division was selected </p2><br>'
                    '<p> a / b = {}</p>'.format(input1/input2,))
        
@app.route('/success2', methods = ['POST'])
def success2():
#    if request.method == 'POST':
     f = request.files['file']
#    f.save(secure_filename(f.filename))
     success2.file_name=f.filename
     f.save(success2.filename)
     return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
