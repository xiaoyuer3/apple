# coding=utf-8
from flask import Flask, request, jsonify, render_template
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    # 这里是demo，实际这么返回响应字符串是不规范的
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082)