from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']
        self.availableIphones = 1
        self.availableSamsungs = 2
        self.availableNokias = 3
        self.cart = [["iPhones",0], ["Samsungs",0], ["Nokias",0]]

    @intent_handler('want.to.buy.a.phone.intent')
    def handle_want_to_buy_a_phone_intent(self):
        self.speak_dialog('welcome')
        selection = self.ask_selection(self.phones, 'which.phone.do.you.want')
        #debug self.speak_dialog('confirm.phone.choice', {'phone': selection})

        if selection == "iPhone":
            if self.availableIphones > 0:
                self.availableIphones =- 1
                self.speak_dialog('iphone.costs')
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[0][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[0][0], 'number': self.cart[0][1]})
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
                    self.stop
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if add_to_cart == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
                    self.stop

        elif selection == "Samsung":
            if self.availableSamsungs > 0:
                self.availableSamsungs =- 1
                self.speak_dialog('samsung.costs')
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[1][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[1][0], 'number': self.cart[1][1]})
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
                    self.stop
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
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[2][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[2][0], 'number': self.cart[2][1]})
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
                    self.stop
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
                    self.stop
        
        else:
            self.speak_dialog('error')

    @intent_handler('ask.for.price.intent')
    def ask_for_price_intent(self, message):
        self.speak_dialog('welcome')
        selected_phone = message.data.get('phone')
        #debug self.speak_dialog('confirm.phone.choice', {'phone': selected_phone})
        if selected_phone is not None:
            if selected_phone == "iphone":
                self.speak_dialog('iphone.costs')
            elif selected_phone == "samsung":
                self.speak_dialog('samsung.costs')
            elif selected_phone == "nokia":
                self.speak_dialog('nokia.costs')
            else:
                self.speak_dialog('error')

    @intent_handler('shopping.cart.intent')
    def shopping_cart(self, message):
        self.speak_dialog('welcome')

def create_skill():
    return ItmProjektSmartphone()
