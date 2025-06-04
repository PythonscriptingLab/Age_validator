from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
<!doctype html>
<html>
<head><title>Age Checker</title></head>
<body>
    <h2>Enter your details</h2>
    <form method="post">
        Name: <input type="text" name="name" required><br><br>
        Age: <input type="number" name="age" required><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if message %}
        <h3>{{ message }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def check_age():
    message = ''
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        if age < 18:
            message = f"Sorry {name}, you are not allowed."
        else:
            mess
