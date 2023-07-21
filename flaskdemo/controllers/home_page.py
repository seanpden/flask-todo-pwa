from flaskdemo import app
from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import Session
from flaskdemo.models.Todo import Todo
from flaskdemo.models.Base import Base, engine


@app.route("/")
def main_page():
    session = Session(engine)
    Base.metadata.create_all(engine)
    data = session.query(Todo).all()
    complete = session.query(Todo).filter(Todo.status == True)  # noqa: E712
    incomplete = session.query(Todo).filter(Todo.status == False)  # noqa: E712
    return render_template(
        "index.html", data=data, complete=complete, incomplete=incomplete
    )


@app.route("/manifest.json")
def server_manifest():
    return app.send_static_file("manifest.json")


@app.route("/sw.js")
def serve_sw():
    return app.send_static_file("sw.js")


@app.post("/add")
def add():
    title = request.form["task_title"]
    assignee = request.form["assignee"]
    status = False
    new_todo = Todo(title=title, assignee=assignee, status=status)
    with Session(engine) as session:
        session.add_all([new_todo])
        session.commit()
    return redirect(url_for("main_page"))


@app.get("/update/<int:todo_id>")
def update(todo_id):
    with Session(engine) as session:
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        todo.status = not todo.status
        session.commit()
    return redirect(url_for("main_page"))


@app.get("/edit_red/<int:todo_id>")
def edit_red(todo_id):
    with Session(engine) as session:
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
    return render_template("edit_todo.html", todo=todo)


@app.post("/edit/<int:todo_id>")
def edit(todo_id):
    with Session(engine) as session:
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        title = request.form["task_title"]
        if title:
            todo.title = request.form["task_title"]
        assignee = request.form["assignee"]
        if assignee:
            todo.assignee = request.form["assignee"]
        session.commit()
    return redirect(url_for("main_page"))


@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    with Session(engine) as session:
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        session.delete(todo)
        session.commit()
    return redirect(url_for("main_page"))


@app.route("/foobar")
def foobar():
    return {"foo": "bar"}


@app.route("/fizzbuzz")
def fizzbuzz():
    return {"fizz": "buzz"}
