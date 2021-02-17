from mycroft import MycroftSkill, intent_file_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('smartphone.projekt.itm.intent')
    def handle_smartphone_projekt_itm(self, message):
        self.speak_dialog('smartphone.projekt.itm')


def create_skill():
    return ItmProjektSmartphone()

