from flask import Flask, request
from vectormath import cosine_sim, cosine_dist, euclidean_dist
app = Flask(__name__)

@app.route('/')
def greet():
    return 'working on trigonometry rn'

@app.route('/cosinedist', methods=['POST'])
def cosinedist():
# accepts 2 vectors x and y from user
    if request.method == 'POST':
        if request.is_json:
            json_data = request.get_json()
            x = json_data.get('vector1')
            y = json_data.get('vector2')
            return cosine_dist(x, y)
        return "400, only json accepted"
    return "invalid http method"

@app.route('/cosinesim', methods=['POST'])
def cosinesim():
# accepts 2 vectors x and y from user
    if request.method == 'POST':
        if request.is_json:
            json_data = request.get_json()
            x = json_data.get('vector1')
            y = json_data.get('vector2')
            return cosine_sim(x, y)
        return "400, only json accepted"
    return "invalid http method"

@app.route('/euclideandist', methods=['POST'])
def cosinedist():
# accepts 2 vectors x and y from user
    if request.method == 'POST':
        if request.is_json:
            json_data = request.get_json()
            x = json_data.get('vector1')
            y = json_data.get('vector2')
            return euclidean_dist(x, y)
        return "400, only json accepted"
    return "invalid http method"

if __name__ == '__main__':
    app.run()

# supports only if len(x) == len(y)
# class needs to be implemented