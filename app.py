
from flask import Flask, render_template, request, redirect #Render_template is for embedding a html
from flask_sqlalchemy import SQLAlchemy #This is the package for database
from datetime import datetime

app = Flask(__name__)#INITALIZE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"  #This is for the database
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno}  - {self.title}"
    



@app.route('/', methods = ["POST","GET"])
def hello_wprld():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo =Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/update/<int:srno>', methods=['GET','POST'])
def update(srno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(srno=srno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(srno=srno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:srno>')
def delete(srno):
    todo = Todo.query.filter_by(srno=srno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")



if __name__ == "__main__":
    app.run(port= 5000,debug=True)
    