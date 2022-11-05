# coding=utf-8
from flask import Flask, request, jsonify, render_template, make_response
import urllib
import time

app = Flask(__name__)


@app.route("/order", methods=["GET", "POST"])
def get_sum():
    name = request.form.get("input-name")
    address = request.form.get("input-address")
    phone = request.form.get("input-number")
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    bast = int(request.cookies.get("bast-score").strip())
    print(type(bast))
    rate = 1.0
    if(bast>0 and bast<1):
        rate = (100 - bast / 10) / 100
        if (rate < 0.7):
            rate = 0.7
    else:
        rate= 1.0
    with open("result/"+str(now_time)+name,"w") as fw:
        fw.write(name+"+"+str(time.time())+"\t"+address+"\t"+str(bast)+"\t"+str(rate)+"\t"+str(phone)+"\t"+now)
    obj = dict()
    obj['name']=name
    obj['address']=address
    obj['phone']=phone
    obj['bast']=bast
    return render_template("finalOrder.html",data=obj)

@app.route('/info')
def address():
    return render_template("info.html")

@app.route('/')
def index():
    data = {'nickname': 'Miguel'}  # fake user
    return render_template("index.html",u=data)

if __name__ == "__main__":
    #app.config["JSON_AS_ASCII"] = False
    app.run(host="0.0.0.0", port=8888)