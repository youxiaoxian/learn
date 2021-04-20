from test04.page.add_department import AddDepartment


class Contact:
    def goto_add_department(self):
        '''
        跳转到添加部门弹窗
        :return:
        '''
        return AddDepartment()

    def get_department_list(self):
        '''
        获取部门列表
        :return:
        '''
        pass