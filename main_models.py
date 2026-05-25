from models import Person, Bank

def main():
    masha = Person('masha')
    alex = Person('   alex')
    borys = Person('Borys')

    aval = Bank('aval')
    universal = Bank('universal')

    borys_account_in_aval = aval.open_account(borys)
    pass


main()

