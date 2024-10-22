from flask import Flask, request
from vectormath import cosine_sim
app = Flask(__name__)

@app.route('/')
def greet():
    return 'working on trigonometry rn'

@app.route('/cosinesim', methods=['POST'])
def cosinesim():
    if request.method == 'POST':
        if request.is_json:
            json_data = request.get_json()
            x = json_data.get('vector1')
            y = json_data.get('vector2')
            return cosine_sim(x, y)
        return "400, only json accepted"
    return "invalid http method"

if __name__ == '__main__':
    app.run()
