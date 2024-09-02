from model.project import Project
import random
import string


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    new_project = Project(project_name=random_string(5), description=random_string(15))
    app.project.create(new_project)
    new_projects = app.soap.get_project_list()
    assert len(new_projects) == len(old_projects)


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
