from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('first.step.intent')
    def handle_first_step_intent(self):
        phone_choice = self.get_response('which.phone.do.you.want')
        self.speak_dialog('confirm.phone.choice', {'phone': phone_choice})


def create_skill():
    return ItmProjektSmartphone()