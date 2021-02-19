from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']
        self.colorsIphone = ['Black', 'White']
        self.colorsSamsung = ['Blue', 'White']
        self.colorsNokia = ['Yellow', 'Blue']
        self.availableIphones = 1
        self.availableSamsungs = 2
        self.availableNokias = 3

    @intent_handler('want.to.buy.a.phone.intent')
    def handle_want_to_buy_a_phone_intent(self):
        self.speak_dialog('welcome')
        selection = self.ask_selection(self.phones, 'which.phone.do.you.want')
        self.speak_dialog('confirm.phone.choice', {'phone': selection})

        if selection == "iPhone":
            if self.availableIphones > 0:
                self.availableIphones =- 1
                self.speak_dialog('iphone.costs')
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
                    self.stop

        elif selection == "Samsung":
            if self.availableSamsungs > 0:
                self.availableSamsungs =- 1
                self.speak_dialog('samsung.costs')
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
                    self.stop
        
        elif selection == "Nokia":
            if self.availableNokias > 0:
                self.availableNokias =- 1
                self.speak_dialog('nokia.costs')
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
                    self.stop
        
        else:
            self.speak_dialog('error')


    def stop(self):
        pass

def create_skill():
    return ItmProjektSmartphone()
