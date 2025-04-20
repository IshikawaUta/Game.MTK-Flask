## Portfolio dengan flask framework
### Installasi flask
- Install from apt package
```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3
$ sudo apt-get install python3-flask
```

- Install from yum package
```bash
$ sudo yum update
$ sudo yum install python3
$ sudo yum install python3-flask
```

- Install from dnf package
```bash
$ sudo dnf update
$ sudo dnf install python3
$ sudo dnf install python3-flask
```

- Install from zypper package
```bash
$ sudo dnf update
$ sudo dnf install python3
$ sudo dnf install python3-flask
```

### Installasi flask dengan python Virtual environment (venv)
**VENV** Python Virtual environment lingkungan terisolasi dibuat untuk proyek Python dan untuk menyimpan direktori dengan struktur berkas tertentu
- ### Install from apt package
```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-pip
$ python3 -m venv venv
```
**activate venv**
```bash
$ source venv/bin/activate
$ pip3 install flask
```

- ### Install from yum package
```bash
$ sudo yum update
$ sudo yum install python3
$ sudo yum install python3-pip
```
**activate venv**
```bash
$ source venv/bin/activate
$ pip3 install flask
```


- ### Install from dnf package
```bash
$ sudo dnf update
$ sudo dnf install python3
$ sudo dnf install python3-pip
```
**activate venv**
```bash
$ source venv/bin/activate
$ pip3 install flask
```

- ### Install from zypper package
```bash
$ sudo dnf update
$ sudo dnf install python3
$ sudo dnf install python3-flask
```
**activate venv**
```bash
$ source venv/bin/activate
$ pip3 install flask
```

### flask name output
**app.py**
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('result.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome!</h1>
    <form method="POST" action="/process">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**templates/result.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

**run project**
```bash
$ python3 app.py
```
**open browser**
```
http://localhost:5000/
```
```
http://127.0.0.1:5000/
```
