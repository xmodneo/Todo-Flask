from flask import Flask,render_template,jsonify,request,redirect
import pyrebase

app = Flask("__main__")

Config = {
  "apiKey": "AIzaSyCATdKnexsHVROwiTXqBtYvCPF6x71l2yI",
  "authDomain": "flaskpython-623ba.firebaseapp.com",
  "databaseURL": "https://flaskpython-623ba-default-rtdb.firebaseio.com",
  "projectId": "flaskpython-623ba",
  "storageBucket": "flaskpython-623ba.appspot.com",
  "messagingSenderId": "222307411334",
  "appId": "1:222307411334:web:14ea47e777c698bafcf807",
  "measurementId": "G-BE2ZN5C19S"
}

firebase = pyrebase.initialize_app(Config)

db = firebase.database()

@app.route("/",methods = ["GET","POST"])
def func():
    if request.method == "POST":
        if request.form["submit"] == "add":
            name = request.form["name"]
            db.child("todoapp").child(name).push(name)
            todoapp = db.child("todoapp").get().val()
            lis = []
            for i in todoapp.values():
                m = list(i.values())
                lis.append(m[0])
            return render_template("index.html", to = lis)
        elif request.form["submit"] == "del":
            name = request.form["name"]
            db.child("todoapp").child(name).remove()
            todoapp = db.child("todoapp").get().val()
            if todoapp == None:
                return render_template("index.html")
            else:
                lis = []
                for i in todoapp.values():
                    m = list(i.values())
                    print(m)
                    lis.append(m[0])
                return render_template("index.html", to = lis)
    elif request.method == 'GET':
        todoapp = db.child("todoapp").get().val()
        if todoapp == None:
                return render_template("index.html")
        else:
            lis = []
            for i in todoapp.values():
                m = list(i.values())
                lis.append(m[0])
            return render_template("index.html", to = lis)      
    return render_template("index.html")

@app.route('/delete/<id>')
def delete_task(id):
    db.child("todoapp").child(id).remove()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)