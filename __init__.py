from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']
        self.colors.iphone = ['Black', 'White']
        self.colors.Samsung = ['Blue', 'White']
        self.colors.Nokia = ['Yellow', 'Blue']

    @intent_handler('want.to.buy.a.phone.intent')
    def handle_want_to_buy_a_phone_intent(self):
        self.speak_dialog('welcome')
        selection = self.ask_selection(self.phones, 'which.phone.do.you.want')
        self.speak_dialog('confirm.phone.choice', {'phone': selection})

        def iphone():
            self.speak("Choose a color for your iPhone")

        def samsung():
            self.speak("Choose a color for your Samsung")

        def nokia():
            self.speak("Chosse a color for your Nokia")

        def numbers_to_choice(numbers):
            switcher = {
                1: iphone,
                2: samsung,
                3: nokia
            }

def create_skill():
    return ItmProjektSmartphone()