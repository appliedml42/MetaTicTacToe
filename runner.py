from games import MetaT3
import random


def setup_game():
    is_p1_ai = input("Is player 1 an AI? ") == "yes"
    if is_p1_ai:
        player1 = "openAI"
        print(f"Player 1 is an AI with the name {player1}")
    else:
        player1 = input("What is player 1's name? ")
        print(f"Player 1 a human with the name {player1}")

    is_p2_ai = input("Is player 2 an AI? ") == "yes"
    if is_p2_ai:
        player2 = "DeepMind"
        print(f"Player 2 is an AI with the name {player2}")
    else:
        player2 = input("What is player 1's name? ")
        print(f"Player 2 a human with the name {player2}")

    game = MetaT3(player1, is_p1_ai, player2, is_p2_ai)

    return game, player1, is_p1_ai, player2, is_p2_ai


def execute_move(game: MetaT3, player: str, is_p_ai: bool):
    while True:
        m_row, m_col, row, col = get_ai_move() if is_p_ai else get_player_move(player)
        if game.move(player, m_row, m_col, row, col):
            game.pretty_print()
            game.update_game_status(player)
            return m_row, m_col, row, col
        elif not is_p_ai:
            print(f"Darn! {player} invalid move try again")


def play_game(player1: str, is_p1_ai: bool, player2: str, is_p2_ai: bool, game: MetaT3):
    while True:
        m_row, m_col, row, col = execute_move(game, player1, is_p1_ai)
        print(f"Last Move by {player1} game:({m_row}, {m_col}) cell:({row}, {col})")
        if game.game_status != "ongoing":
            print("GAME IS FINISHED!!")
            break

        m_row, m_col, row, col = execute_move(game, player2, is_p2_ai)
        print(f"Last Move by {player2} game:({m_row}, {m_col}) cell:({row}, {col})")
        if game.game_status != "ongoing":
            print("GAME IS FINISHED!!")
            break


def get_ai_move():
    m_row = random.randint(0, 2)
    m_col = random.randint(0, 2)
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    return m_row, m_col, row, col


def get_player_move(player):
    print(f"{player} Lets select game")
    m_row = int(input(f"Enter Game row? "))
    m_col = int(input(f"Enter Game col? "))

    print(f"{player} Lets select cell to play in game ({m_row}, {m_col})")
    row = int(input(f"Enter cell row? "))
    col = int(input(f"Enter cell col? "))

    return m_row, m_col, row, col


if __name__ == "__main__":
    game, player1, is_p1_ai, player2, is_p2_ai = setup_game()
    play_game(player1, is_p1_ai, player2, is_p2_ai, game)
    game.pretty_print()
