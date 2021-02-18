from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('first.step.intent')
    def handle_first_step_intent(self, message):
        self.speak_dialog("welcome")

def create_skill():
    return ItmProjektSmartphone()

