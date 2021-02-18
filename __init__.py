from mycroft import MycroftSkill, intent_file_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('initial.intent')
    def handle_set_phone_wish(self):
        phone_wish = self.get_response('initial.dialog')
        self.speak_dialog('confirm.phone.wish'. {'phone': phone_wish })


def create_skill():
    return ItmProjektSmartphone()

