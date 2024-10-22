from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return 'working on trigonometry rn'

if __name__ == '__main__':
    app.run()
