from flask import Flask, request

import pipeline

app = Flask(__name__)

@app.route('/articles', methods=['POST'])
def postArticles():
    data = request.json
    res=pipeline.processArticle(data)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # run our Flask app