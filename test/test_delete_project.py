from model.project import Project
import random
from test.test_add_project import random_string


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(random_string(5), random_string(15)))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.project_name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
