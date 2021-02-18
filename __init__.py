from mycroft import MycroftSkill, intent_file_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']

    @intent_handler('initial.intent')
    def handle_set_phone_wish(self):
        self.speak_dialog('which.phone.do.you.want')
        selection = self.ask_selection(self.phones, 'smartphones')
        self.speak_dialog('you.bought', {'phone': selection})

def create_skill():
    return ItmProjektSmartphone()

