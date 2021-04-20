from test04.page.base import Base
from test04.page.contact import Contact


class MainPage(Base):
    def goto_contact(self):
        '''
        跳转到通讯录页面
        :return:
        '''
        return Contact()
