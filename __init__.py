from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']
        self.colorsIphone = ['Black', 'White']
        self.colorsSamsung = ['Blue', 'White']
        self.colorsNokia = ['Yellow', 'Blue']

    @intent_handler('want.to.buy.a.phone.intent')
    def handle_want_to_buy_a_phone_intent(self):
        self.speak_dialog('welcome')
        selection = self.ask_selection(self.phones, 'which.phone.do.you.want')
        self.speak_dialog('confirm.phone.choice', {'phone': selection})

    def converse(self, utterances, lang):
        if utterances and self.voc_match(utterances[0], 'iphone'):
            self.speak_dialog('iphone.costs')
            return True
        if utterances and self.voc_match(utterances[0], 'samsung'):
            self.speak_dialog('samsung.costs')
            return True
        if utterances and self.voc_match(utterances[0], 'nokia'):
            self.speak_dialog('nokia.costs')
            return True
        else:
            self.speak_dialog('error')
            return False

def create_skill():
    return ItmProjektSmartphone()