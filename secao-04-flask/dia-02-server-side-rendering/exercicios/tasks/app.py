from flask import Flask, render_template, request
from models.Task import Task

app = Flask(__name__)
app.static_folder = "views/static"
app.template_folder = "views/templates"

tasks = [
    Task(1, "Fazer compras"),
    Task(2, "Estudar para a prova"),
    Task(3, "Limpar a casa"),
]


@app.route('/', methods=['GET', 'POST'])
def tasks_view():
    if request.method == 'POST':
        title = request.form['title']
        new_task = Task(len(tasks) + 1, title)
        tasks.append(new_task)

    return render_template('index.html', tasks=tasks)


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True

    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run()
