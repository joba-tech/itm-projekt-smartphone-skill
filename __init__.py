from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']
        self.colorsIphone = ['Black', 'White']
        self.colorsSamsung = ['Blue', 'White']
        self.colorsNokia = ['Yellow', 'Blue']
        self.smartphoneSelection

    @intent_handler('want.to.buy.a.phone.intent')
    def handle_want_to_buy_a_phone_intent(self):
        self.speak_dialog('welcome')
        smartphoneSelection = self.ask_selection(self.phones, 'which.phone.do.you.want')
        self.speak_dialog('confirm.phone.choice', {'phone': selection})

        if smartphoneSelection == "iphone":
            self.speak_dialog('iphone.costs')
        elif smartphoneSelection == "samsung":
            self.speak_dialog('samsung.costs')
        elif smartphoneSelection == "nokia":
            self.speak_dialog('nokia.costs')
        else:
            self.speak_dialog('error')

def create_skill():
    return ItmProjektSmartphone()