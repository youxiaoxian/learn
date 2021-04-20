from test04.page.main_page import MainPage


class TestAddDepartment:
    def test_add_department(self):
        main_page=MainPage()
        main_page.goto_contact().goto_add_department().add_department_success().get_department_list()
