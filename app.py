from flask import Flask,render_template,request,redirect
import json 
import os
import time
import random 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

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
            filename = str(time.time())+"."+image.filename.split(".")[1]
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

        reader[postId] = reader

        open("postInfo.json","w").write(json.dumps(reader,indent=4))

        return redirect('/createPost')

if __name__ == "__main__":
    app.run(debug=True,port=3000)
