from flask import Flask,render_template,request,redirect
import json 
import os
import time
import random 
from login import Faraday
app = Flask(__name__)


@app.route('/')
def index():
    f = int(open("f.txt","r").read())
    try:
        allPosts = json.loads(open("postInfo.json","r").read())
    except Exception as e:

        allPosts = None
    return render_template('index.html',allPosts=allPosts,f=f)

@app.route('/createPost',methods=['POST','GET'])
def createPost():
    if request.method == 'GET':
        
        return render_template('create.html')
    if request.method == "POST":
        images = request.files.getlist('images[]')
        data = {
            "images":[]
        }
        for image in images:
            filename = str(random.randint(1,32423532345))+"."+image.filename.split(".")[1]
            filename = image.filename.replace(" ","")
            data["images"].append(filename)
            image.save(os.path.join('static',filename))
            
        postTitle = request.form.get('title')
        data["title"] = postTitle
        randoms = ["A","B","C","d","D"]

        postId = random.choice(randoms)+str(random.randint(100,1000000))+random.choice(randoms)

        try:
            reader = open("postInfo.json","r").read()
            reader = json.loads(reader)
        except:
            reader = {}

        reader[postId] = data

        open("postInfo.json","w").write(json.dumps(reader,indent=4))

        return redirect('/createPost')

@app.route("/post/<pid>")
def postSettings(pid):
    try:
        data= json.loads(open("postInfo.json","r").read())[pid]
    except:
        return "404"
    title = data["title"]
    images = data["images"]
    return render_template("post.html",images=images,title=title)

@app.route("/accountManager",methods=["POST","GET"])
def accountManager():
    try:
        data= json.loads(open("s1.json","r").read())
    except:
        data = {}
    return render_template("accounts.html",data=data)


@app.route("/login_with_twitter")
def login_with_twitter():
    username = request.args.get("u")
    password = request.args.get("p")
    email = request.args.get("e")
    phonenumber = request.args.get("ph")

    faraday = Faraday()
    out = faraday.login(username,password,email,phonenumber,"s1")
    return out

@app.route("/frequency")
def setFrequency():
    f = request.args.get("f")
    open("f.txt","w").write(f)
    return {"SCC":True}
if __name__ == "__main__":
    app.run(debug=True,port=3000)
