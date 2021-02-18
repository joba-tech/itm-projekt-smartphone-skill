from mycroft import MycroftSkill, intent_file_handler


from mycroft import MycroftSkill, intent_file_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('first.step.intent')
    def handle_test(self, message):
        self.speak_dialog('welcome')


def create_skill():
    return ItmProjektSmartphone()