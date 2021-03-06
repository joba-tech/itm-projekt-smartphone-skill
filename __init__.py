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
        if selection == "iPhone":
            if self.availableIphones > 0:
                self.speak_dialog('iphone.costs', {'costs': self.cart[0][2]})
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.availableIphones =- 1
                    self.cart[0][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[0][0], 'number': self.cart[0][1]})
                    checkout_question = self.ask_yesno('checkout.question')
                    if checkout_question == 'yes':
                        self.handle_checkout_intent()
                    else:
                        self.speak_dialog('goodbye')    
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
        elif selection == "Samsung":
            if self.availableSamsungs > 0:
                self.availableSamsungs =- 1
                self.speak_dialog('samsung.costs', {'costs': self.cart[1][2]})
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[1][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[1][0], 'number': self.cart[1][1]})
                    checkout_question = self.ask_yesno('checkout.question')
                    if checkout_question == 'yes':
                        self.handle_checkout_intent()
                    else:
                        self.speak_dialog('goodbye')   
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
        elif selection == "Nokia":
            if self.availableNokias > 0:
                self.availableNokias =- 1
                self.speak_dialog('nokia.costs', {'costs': self.cart[2][2]})
                add_to_cart = self.ask_yesno('add.to.cart.question')
                if add_to_cart == 'yes':
                    self.cart[2][1] += 1
                    self.speak_dialog('cart.entries', {'phones': self.cart[2][0], 'number': self.cart[2][1]})
                    checkout_question = self.ask_yesno('checkout.question')
                    if checkout_question == 'yes':
                        self.handle_checkout_intent()
                    else:
                        self.speak_dialog('goodbye')                                   
                elif add_to_cart == 'no':
                    self.handle_want_to_buy_a_phone_intent()
            else:
                wants_alternativphone = self.ask_yesno('not.available')
                if wants_alternativphone == 'yes':
                    self.handle_want_to_buy_a_phone_intent()
                elif wants_alternativphone == 'no':
                    self.speak_dialog('goodbye')
        else:
            self.speak_dialog('error')
        self.stop

    @intent_handler('how.much.does.a.phone.cost.intent')
    def handle_ask_for_price_intent(self, message):
        self.speak_dialog('welcome')
        selected_phone = message.data.get('phone')
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

    @intent_handler('shopping.cart.intent')
    def handle_shopping_cart_intent(self):
        self.speak_dialog('welcome')
        self.speak_dialog('shopping.cart.status', {'phone1_name': self.cart[0][0], 'phone1_number': self.cart[0][1], 'phone2_name': self.cart[1][0], 'phone2_number': self.cart[1][1], 'phone3_name': self.cart[2][0], 'phone3_number': self.cart[2][1]})
        checkout_question = self.ask_yesno('checkout.question')
        if checkout_question == 'yes':
            self.handle_checkout_intent()
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

    @intent_handler('checkout.intent')
    def handle_checkout_intent(self):
        self.speak_dialog('shopping.cart.status', {'phone1_name': self.cart[0][0], 'phone1_number': self.cart[0][1], 'phone2_name': self.cart[1][0], 'phone2_number': self.cart[1][1], 'phone3_name': self.cart[2][0], 'phone3_number': self.cart[2][1]})
        cart_total = (self.cart[0][1] * self.cart[0][2]) + (self.cart[1][1] * self.cart[1][2]) + (self.cart[2][1] * self.cart[2][2])
        self.speak_dialog('shopping.cart.total', {'total': cart_total})
        home_street = self.get_response('what.is.your.street.address')            
        home_number = self.get_response('what.is.your.house.number')
        home_zip = self.get_response('what.is.your.zip.code')
        home_town = self.get_response('what.is.your.hometown')
        address_check = self.ask_yesno('address.check', {'street': home_street, 'number': home_number, 'zip': home_zip, 'town': home_town})
        if address_check == 'yes':
            self.speak_dialog('thank.you.for.purchase')
            self.speak_dialog('goodbye')
            self.cart = [["iPhones",0,999], ["Samsungs",0,699], ["Nokias",0,1]]
        else:
            self.handle_checkout_intent()
        self.stop
    
    def stop(self):
        pass

def create_skill():
    return ItmProjektSmartphone()
