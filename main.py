# coding=utf-8
import logging

from flask import Flask, request, render_template
import time

app = Flask(__name__)

logging.basicConfig(
                    level    = logging.INFO,
                    format   = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
                    datefmt  = '%Y-%m-%d %A %H:%M:%S',
                    filename = "log/apple.log",
                    filemode = 'w')

@app.route("/order", methods=["GET", "POST"])
def get_sum():
    name = request.form.get("input-name")
    address = request.form.get("input-address")
    phone = request.form.get("input-number")
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    if(name!=None and address!=None and phone!=None):
        bast = int(request.cookies.get("bast-score").strip())
        rate = 1.0
        if (bast > 0 and bast < 1):
            rate = (100 - bast / 10) / 100
            if (rate < 0.7):
                rate = 0.7
        else:
            rate = 1.0
        with open("result/"+now_time+name,"w") as fw:
            fw.write(name+"+"+str(time.time())+"\t"+address+"\t"+str(bast)+"\t"+str(rate)+"\t"+str(phone)+"\t"+now)
        obj = dict()
        obj['name']=name
        obj['address']=address
        obj['phone']=phone
        obj['bast']=bast
        logging.info("填写成功!{},{},{}".format(name,address,phone))
        return render_template("finalOrder.html", data=obj)
    else:
        logging.info("填写未成功！{},{},{}".format(name,address,phone))
        return render_template("info.html")


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