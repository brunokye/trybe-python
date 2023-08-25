from flask import Blueprint, render_template, request, redirect
from models.projectModel import ProjectModel
from models.querys import _project_id, _task_id

project_controller = Blueprint('project', __name__)


def _get_project_or_task(id):
    project = ProjectModel.find(id)
    return [task.to_dict() for task in project]


def _format_date(date):
    splited = date.split('-')
    splited.reverse()
    return '/'.join(splited)


def _save_task(req, id_projeto, nome_projeto):
    deadline = {
        'idProjeto': int(id_projeto),
        'nome': nome_projeto,
        'atividade': req.get('nome'),
        'status': req.get('status'),
        'completionPercentage': req.get('percentage'),
        'descriptionTask': req.get('description'),
        'deadline': _format_date(req.get('deadline')),
        'responsible': req.get('responsible')
    }
    task = ProjectModel(deadline)
    task.save()


@project_controller.route("/")
@project_controller.route("/projects")
def home():
    projects = ProjectModel.separate_projects()
    return render_template("home.html", projects=projects)


@project_controller.route("/projects/<id>")
def project(id):
    project = _get_project_or_task(_project_id(id))
    return render_template("project.html", project=project)


@project_controller.route("/task/<id>")
def task(id):
    task = _get_project_or_task(_task_id(id))
    return render_template("task.html", task=task[0])


@project_controller.route(
    "/task/<id_projeto>/form",
    methods=['GET', 'POST']
)
def new_task(id_projeto):
    if request.method == 'POST':
        project = _get_project_or_task(_project_id(id_projeto))
        _save_task(request.form, id_projeto, project[0]['nome'])
        return redirect("http://127.0.0.1:8000/", code=302)
    if id_projeto.isnumeric():
        return render_template('taskForm.html')
    return render_template('notFound.html'), 404
