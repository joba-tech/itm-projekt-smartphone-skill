from mycroft import MycroftSkill, intent_handler


class ItmProjektSmartphone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.phones = ['iPhone', 'Samsung', 'Nokia']
        self.availableIphones = 1
        self.availableSamsungs = 2
        self.availableNokias = 3
        self.cart = [["iPhones", 0, 999], ["Samsungs", 1, 699], ["Nokias", 2, 1]]

    @intent_handler('want.to.buy.a.phone.intent')
    def handle_want_to_buy_a_phone_intent(self):
        self.speak_dialog('welcome')
        selection = self.ask_selection(self.phones, 'which.phone.do.you.want')
        #debug self.speak_dialog('confirm.phone.choice', {'phone': selection})

        if selection == "iPhone":
            if self.availableIphones > 0:
                self.availableIphones =- 1
                self.speak_dialog('iphone.costs', {'costs': self.cart[0][2]})
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[0][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[0][0], 'number': self.cart[0][1]})
                    checkout_question = self.ask_yesno('chechout.question')
                    if checkout_question == 'yes':
                        self.handle_chechout_intent()
                    else:
                        self.speak_dialog('goodbye')
                        self.stop
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
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
                self.speak_dialog('samsung.costs', {'costs': self.cart[1][2]})
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[1][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[1][0], 'number': self.cart[1][1]})
                    checkout_question = self.ask_yesno('chechout.question')
                    if checkout_question == 'yes':
                        self.handle_chechout_intent()
                    else:
                        self.speak_dialog('goodbye')
                        self.stop
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
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
                self.speak_dialog('nokia.costs', {'costs': self.cart[2][2]})
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[2][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[2][0], 'number': self.cart[2][1]})
                    checkout_question = self.ask_yesno('chechout.question')
                    if checkout_question == 'yes':
                        self.handle_chechout_intent()
                    else:
                        self.speak_dialog('goodbye')
                        self.stop               
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
                    self.stop
        
        else:
            self.speak_dialog('error')
            self.stop

        self.stop

    @intent_handler('how.much.is.the.fish.intent')
    def handle_ask_for_price_intent(self, message):
        self.speak_dialog('welcome')
        selected_phone = message.data.get('phone')
        #debug self.speak_dialog('confirm.phone.choice', {'phone': selected_phone})
        if selected_phone is not None:
            if selected_phone == "iphone":
                self.speak_dialog('iphone.costs', {'costs': self.cart[0][2]})
            elif selected_phone == "samsung":
                self.speak_dialog('samsung.costs', {'costs': self.cart[1][2]})
            elif selected_phone == "nokia":
                self.speak_dialog('nokia.costs', {'costs': self.cart[2][2]})
            else:
                self.speak_dialog('error')
                self.stop
        self.stop

    @intent_handler('shopping.cart.intent')
    def handle_shopping_cart_intent(self):
        self.speak_dialog('welcome')
        self.speak_dialog('shopping.cart.status', {'phone1_name': self.cart[0][0], 'phone1_number': self.cart[0][1], 'phone2_name': self.cart[1][0], 'phone2_number': self.cart[1][1], 'phone3_name': self.cart[2][0], 'phone3_number': self.cart[2][1]})
        checkout_question = self.ask_yesno('chechout.question')
        if checkout_question == 'yes':
            self.handle_chechout_intent()
        else:
            self.speak_dialog('goodbye')
            self.stop

    @intent_handler('delete.shopping.cart.intent')
    def handle_delete_shopping_cart_intent(self):
        self.speak_dialog('welcome')
        delete_shopping_cart = self.ask_yesno('are.you.sure.cart')
        if delete_shopping_cart == 'yes':
            self.cart = [["iPhones",0,999], ["Samsungs",0,699], ["Nokias",0,1]]
            self.speak_dialog('confirm.deltion')
        else:
            self.speak_dialog('goodbye')
            self.stop

    @intent_handler('hello.there.intent')
    def handle_hello_there_intent(self):
        self.speak_dialog('general.kenobi')
        self.stop

    @intent_handler('checkout.intent')
    def handle_chechout_intent(self):
        shopping_cart_total = self.cart[0][2] + self.cart[1][2] + self.cart[2][2]
        self.speak_dialog(shopping_cart_total)
        self.stop



def create_skill():
    return ItmProjektSmartphone()
