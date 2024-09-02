from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()


    def delete_project_by_name(self, project_name):
        wd = self.app.wd
        self.open_project_page()
        project_elements = wd.find_elements_by_xpath(f"//a[text()='{project_name}']")
        if not project_elements:
            return
        project_elements[0].click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()


    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("My View").click()
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def change_field_value(self, project_name, text):
        wd = self.app.wd
        # if project_name is not None:
        wd.find_element_by_name(project_name).click()
        wd.find_element_by_name(project_name).clear()
        wd.find_element_by_name(project_name).send_keys(text)


    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.project_name)
        self.change_field_value("description", project.description)
        wd.find_element_by_name("status").click()
        wd.find_element_by_xpath("//option[text()='obsolete']").click()
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_xpath("//option[text()='private']").click()


    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project_list = []
        for row in wd.find_elements_by_css_selector("tr.row-1, tr.row-2"):
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text.strip()
            project_list.append(Project(project_name=name))
        return project_list
