from game import Street, Enemy, Friend, Item
def main():
    arena_lviv = Street("Arena Lviv")
    arena_lviv.set_description("Always full when Ukrainian national team plays.")

    ukraina_stadium = Street("Ukraina Stadium")
    ukraina_stadium.set_description("Karpaty lost once again...")

    kozelnytska = Street("UCU on Kozelnytska street")
    kozelnytska.set_description("A proof that CS students can be as successful as priests")

    silpo = Street("Silpo")
    silpo.set_description("You can buy literally anything here!")

    atb = Street("ATB")
    atb.set_description("Works around the clock and everything is almost free.")

    fest_republic = Street("FEST! Republic")
    fest_republic.set_description("The parties here hit hard!")

    high_castle = Street("Vysokyi Zamok")
    high_castle.set_description("Don't forget to take a photo here(if your legs are still alive)")

    lnu_university = Street("Ivana Franka University")
    lnu_university.set_description("There are like 20 thousand students here. It's crazy...")

    rynok_square = Street("Rynok Square")
    rynok_square.set_description("Too many cafés to keep you wallet full.")

    svoboda = Street("Svoboda Avenue")
    svoboda.set_description("Beautiful every time you walk here.")

    levandivka = Street("Levandivka")
    levandivka.set_description("Get what you need and get out of here fast.")

    arena_lviv.link_room(atb, '1')
    arena_lviv.link_room(lnu_university, '2')

    lnu_university.link_room(arena_lviv, '1')
    lnu_university.link_room(fest_republic, '2')

    ukraina_stadium.link_room(lnu_university, '1')
    ukraina_stadium.link_room(fest_republic, '2')

    fest_republic.link_room(ukraina_stadium, '1')
    fest_republic.link_room(levandivka, '2')

    levandivka.link_room(fest_republic, '1')
    levandivka.link_room(high_castle, '2')

    high_castle.link_room(levandivka, '1')
    high_castle.link_room(kozelnytska, '2')

    kozelnytska.link_room(high_castle, '1')
    kozelnytska.link_room(svoboda, '2')

    svoboda.link_room(kozelnytska, '1')
    svoboda.link_room(silpo, '2')

    silpo.link_room(svoboda, '1')
    silpo.link_room(rynok_square, '2')

    rynok_square.link_room(silpo, '1')
    rynok_square.link_room(atb, '2')

    atb.link_room(rynok_square, '1')
    atb.link_room(arena_lviv, '2')



    karpaty_football_shirt = Item("Karpaty football shirt")
    karpaty_football_shirt.set_description("Has no value, but is precious to some in Lviv.")
    arena_lviv.set_item(karpaty_football_shirt)

    book = Item("book")
    book.set_description("Can help with educating foolish people")
    rynok_square.set_item(book)

    pravda_beer = Item("Pravda beer")
    pravda_beer.set_description("It will always make you tell the truth")
    fest_republic.set_item(pravda_beer)

    ucu_local_card = Item("LOKAL card")
    ucu_local_card.set_description("A secret pass to the treasure box(with half a price).")
    kozelnytska.set_item(ucu_local_card)

    mivina = Item("mivina")
    mivina.set_description("Magical piece of food that saves everyone in need.")
    atb.set_item(mivina)

    clothes = Item("clothes")
    clothes.set_description("Essential for all people, but some still don't dress properly.")

    student = Friend("Student", "No money, no food, no time...")
    student.set_conversation("Sometimes I wonder when people sleep...")
    student.set_weakness("mivina")
    student.set_trade("clothes")
    lnu_university.set_character(student)

    lotr = Enemy("Lotr", "Loves sunflower seeds, Adidas trousers and football fights")
    lotr.set_conversation("I was wondering, maybe you have a mobila on yourself?")
    lotr.set_weakness("Karpaty football shirt")
    ukraina_stadium.set_character(lotr)

    zbui = Enemy("Zbui", "I may look like a suspicious guy and I am")
    zbui.set_conversation("I don't know why people find a guy in a hoodie in the summer as weird")
    zbui.set_weakness("book")
    levandivka.set_character(zbui)


    laydak = Enemy("Laydak", "This is my home, for real.")
    laydak.set_conversation("Home is where your heart lives, so I live right here.")
    laydak.set_weakness("clothes")
    high_castle.set_character(laydak)

    batyar = Enemy("Batyar", "He is much more confident than you think he is")
    batyar.set_conversation("Who does not love drinking?!")
    batyar.set_weakness("Pravda beer")
    svoboda.set_character(batyar)


    silpo_cashier = Enemy("Silpo cashier", "I am almost Svyatyi Mykolai's angel.")
    silpo_cashier.set_conversation("You can't get a discount here, even if you are from UCU!")
    silpo_cashier.set_weakness("LOKAL card")
    silpo.set_character(silpo_cashier)

    current_room = arena_lviv
    dead = False
    lives = 2
    backpack = []

    while dead == False:
        current_room.get_details()
        current_character = current_room.get_character()
        current_item = current_room.get_item()

        if current_character:
            current_character.describe()

        if current_item:
            current_item.describe()

        command = input("> ")

        if command in ["1", "2"]:
            current_room = current_room.move(command)
        elif command == "talk":
            if current_character:
                current_character.talk()
            else:
                print('It is silent here...')
        elif command == "fight":
            if current_character and isinstance(current_character, Friend):
                print("Why fight a friend? Be nice to people.")
            if current_character and isinstance(current_character, Enemy):
                print("Choose your weapon:")
                print(backpack)
                fight_with = input()
                if fight_with in backpack:

                    if current_character.fight(fight_with):
                        print("Congrats, you won!")
                        current_room.character = None
                        if current_character.get_defeated() == 5:
                            print("You are the winner of the game!")
                            dead = True
                    else:
                        if lives == 2:
                            lives -= 1
                            print("You lost the fight but not the war.")
                            print("Two more lives. Be careful!")
                        elif lives == 1:
                            lives -= 1
                            print("You lost the fight but not the war.")
                            print("One more life. Be really careful!")
                        else:
                            print("You lost the war.")
                            print("This is the end, hold your breath and count to ten...")
                            dead = True
                else:
                    print(f"You don't have a {fight_with} to fight_with")
            elif not current_character:
                print("It's all peaceful, no one wants to fight.")
        elif command == "take":
            if current_item:
                print(f"Congrats, {current_item.get_name()} is now in your backpack.")
                backpack.append(current_item.get_name())
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        elif command == 'backpack':
            print(backpack)
        elif command == 'trade' and isinstance(current_character, Friend):
            print(backpack)
            exchange = input("Choose the item to trade: ")
            if exchange in backpack:
                if exchange == current_character.weakness:
                    print(f'You exchanged {exchange} for {current_character.trade_item()}')
                    backpack.remove(exchange)
                    backpack.append(current_character.trade_item())
                    current_room.character = None
                else:
                    print(f"{current_character.name} doesn't want {exchange}")
            else:
                print("You don't have this item")
        elif command == 'trade' and not current_character:
            print("Look around: there is no one to trade with.")
        elif command == 'trade' and not isinstance(current_character, Friend):
            print(f"{current_character.name} doesn't want to trade!")
        elif command == '--help' or command == '--h':
            print("""
            You can fight, talk and trade with characters.
            fight: fight with enemies
            talk: talk with characters
            trade: trade with characters
            take: take item in your backpack
            backpack: look what you have in your backpack.
            help, --help, -h: help
            """)
        else:
            print("I don't know how to " + command)
main()
