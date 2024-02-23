from datetime import date


POSITIONS = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']


def positions():
    return print(','.join(POSITIONS))


def title():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program\n")


def get_game_date():
    game_date = date(2024, 3, 21)
    return game_date


def days_till_game():
    today = date.today()
    game_date2 = get_game_date() - today
    return game_date2


def display_lineup(players):
    if players is None:
        return print("No players")
    else:
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player[0]}, {player[1]}, {player[2]}, {player[3]}, {player[4]}\n")


def add_player(players):
    first_name = input("Enter player first name: ")
    last_name = input("Enter player last name: ")
    pos = get_pos()
    atBats = get_atBats()
    hits = get_hits()
    player = [first_name, last_name, pos, atBats, hits]
    players.append(player)
    print(f"{first_name} {last_name} was added")


def get_pos():
    player_pos = input("Position: ").capitalize()
    while True:
        if player_pos not in POSITIONS:
            print("Invalid")
            player_pos = input("Position: ").capitalize()
        else:
            return player_pos


def get_atBats():
    print("blank")


def get_hits():
    print("blank")


def rem_player():
    print("blank")


def move_player():
    print("blank")


def edit_pos():
    print("blank")


def edit_stats():
    print("blank")


def main():
    print('=' * 50)
    print(f"{'Baseball Team Manager':15}")
    print()
    print("CURRENT DATE: {}".format(date.today()))
    print("GAME DATE: {}".format(get_game_date()))
    print("DAYS UNTIL GAME {}".format(days_till_game()))
    print()
    title()
    positions()
    print('=' * 50)
    players = []
    while True:
        option = int(input("Menu Option: "))
        if option == 1:
            display_lineup(players)
        elif option == 2:
            add_player(players)
        elif option == 3:
            rem_player()
        elif option == 4:
            move_player()
        elif option == 5:
            edit_pos()
        elif option == 6:
            edit_stats()
        elif option == 7:
            break
        else:
            print("Invalid")

    print("Bye!")


if __name__ == "__main__":
    main()
