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

        if selection == "iPhone":
            self.speak_dialog('iphone.costs')
        elif selection == "Samsung":
            self.speak_dialog('samsung.costs')
        elif selection == "Nokia":
            self.speak_dialog('nokia.costs')
        else:
            self.speak_dialog('error')

def create_skill():
    return ItmProjektSmartphone()