from typing import Union


class T3:
    def __init__(self, player1: str, player2: str):
        self.board = [["ongoing"] * 3 for i in range(3)]
        self.player1 = player1
        self.player2 = player2
        self.pmap = {player1: "X", player2: "O"}
        self.game_status = "ongoing"
        self.translation_table = {"X": "X", "O": "O", "ongoing": "*"}

    def move(self, player, row, col):
        if not (0 <= row <= 2 and 0 <= col <= 2):
            return False

        if self.game_status != "ongoing":
            return False
        if self.board[row][col] == "ongoing":
            self.board[row][col] = self.pmap[player]
            self.update_game_status(player)
            return True
        return False

    def cell_status(self, row, col):
        return self.board[row][col]

    def update_game_status(self, player):
        self.game_status = get_game_status(self, self.pmap[player])

        if self.game_status == "O" or self.game_status == "X":
            self.board = [[self.game_status] * 3 for i in range(3)]
        elif self.game_status == "draw":
            # Game is draw reset the game.
            self.reset_game()

        return self.game_status

    def reset_game(self):
        self.board = [["ongoing"] * 3 for i in range(3)]
        self.game_status = "ongoing"
        return True

    def get_row_str(self, row):
        return (
            f" {self.translation_table[self.board[row][0]]} | {self.translation_table[self.board[row][1]]} | "
            f"{self.translation_table[self.board[row][2]]} "
        )


class MetaT3:
    def __init__(self, player1: str, is_p1_ai: bool, player2: str, is_p2_ai: bool):
        self.board = [[T3(player1, player2) for _ in range(3)] for _ in range(3)]
        self.player1 = player1
        self.player2 = player2
        self.is_p1_ai = is_p1_ai
        self.is_p2_ai = is_p2_ai
        self.pmap = {player1: "X", player2: "O"}
        self.game_status = "ongoing"

    def move(self, player, meta_row, meta_col, row, col):
        if not (0 <= meta_row <= 2 and 0 <= meta_col <= 2):
            return False
        if self.game_status != "ongoing":
            return False
        if self.board[meta_row][meta_col].game_status == "ongoing":
            return self.board[meta_row][meta_col].move(player, row, col)
        return False

    def cell_status(self, row, col):
        return self.board[row][col].game_status

    def update_game_status(self, player):
        self.game_status = get_game_status(self, self.pmap[player])

        return self.game_status

    def pretty_print(self):
        print()
        print(
            f"Player 1: {self.player1} Symbol: {self.pmap[self.player1]} AI: {self.is_p1_ai}"
        )
        print(
            f"Player 2: {self.player2} Symbol: {self.pmap[self.player2]} AI: {self.is_p2_ai}"
        )
        print(f"Game Status: {self.game_status}")
        print()
        for m_row in range(3):
            for row in range(3):
                print(
                    f":{self.board[m_row][0].get_row_str(row)}:{self.board[m_row][1].get_row_str(row)}:{self.board[m_row][2].get_row_str(row)}:"
                )
            print(".....................................")


def get_game_status(game: Union[T3, MetaT3], player: str):
    # check if won in any row.
    for i in range(3):
        if (
            game.cell_status(i, 0)
            == game.cell_status(i, 1)
            == game.cell_status(i, 2)
            == player
        ):
            return player

    # check if won in any column.
    for i in range(3):
        if (
            game.cell_status(0, i)
            == game.cell_status(1, i)
            == game.cell_status(2, i)
            == player
        ):
            return player

    # check if won in any diagonal.
    if (
        game.cell_status(0, 0)
        == game.cell_status(1, 1)
        == game.cell_status(2, 2)
        == player
    ):
        return player

    if (
        game.cell_status(0, 2)
        == game.cell_status(1, 1)
        == game.cell_status(2, 0)
        == player
    ):
        return player

    # If any move can be made then game is still ongoing.
    for row in range(3):
        for col in range(3):
            if game.cell_status(row, col) == "ongoing":
                return "ongoing"

    return "draw"
