from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):

    @intent_handler('initial.intent')
    def handle_set_phone_wish(self):
        phone_wish = self.get_response('which.phone.do.you.want')
        self.speak_dialog('confirm.phone.wish'. {'phone': phone_wish })


def create_skill():
    return ItmProjektSmartphone()

