#!/usr/bin/python


class Am_I_A_Pizza_Or_Burger:
    def __init__(self, what_Am_I = 'pizza'):
        self.what_Am_I = what_Am_I


    def am_I_a_burger(self):
        if self.what_Am_I == 'burger':
            return True
        else:
            return False

    def am_I_a_pizza(self):
        if self.what_Am_I == 'pizza':
            return True
        else:
            return False

    def amIaSportsCar(self):
        if self.what_Am_I == 'sportscar':
            return True
	else:
            return False

if __name__ == '__main__':
    what_am_i = Am_I_A_Pizza_Or_Burger('pizza')
    print(what_am_i.am_I_a_burger())
    print(what_am_i.am_I_a_pizza())
    print(what_am_i.amIaSportsCar())

