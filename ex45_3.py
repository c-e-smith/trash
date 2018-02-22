from sys import exit
import random
import os


class Game(object):

    def exit_game():
        print("\nYou've exited the game.\n")
        exit()

    def start_game(self, level_choice):
        try:
            os.remove("./mastermind_board.txt")
        except:
            pass
        print("\nWelcome to the game!")
        print("Who do I have the pleasure of challenging today?\n")
        self.level_choice = level_choice
        player = input("name > ")
        decision = True
        while decision:
            print(f"Pick a level {player}.")
            level_choice = input("> ")
            if level_choice=='1':
                return 'level_one'
            elif level_choice=='2':
                return 'level_two'
            elif level_choice=='3':
                return 'level_three'
            else:
                print("\nTry 1, 2, or 3.")


class Level(object):

    def piece_dict(self):
        pieces = open("mastermind_pieces.txt")
        pieces.seek(0)
        piece_dict = {}
        n = 0
        for piece in pieces:
            n+=1
            piece_dict[n] = piece.strip("[,],\n")

        code_number_1 = random.choice(list(piece_dict.keys()))
        code_number_2 = random.choice(list(piece_dict.keys()))
        code_number_3 = random.choice(list(piece_dict.keys()))
        code_number_4 = random.choice(list(piece_dict.keys()))
        hidden_number_code = code_number_1, code_number_2, code_number_3, code_number_4
        code_color_1 = piece_dict[code_number_1]
        code_color_2 = piece_dict[code_number_2]
        code_color_3 = piece_dict[code_number_3]
        code_color_4 = piece_dict[code_number_4]
        hidden_color_code = code_color_1, code_color_2, code_color_3, code_color_4
        return hidden_color_code

    def piece_list(self):
        pieces = open("mastermind_pieces.txt")
        pieces.seek(0)
        piece_list = []
        for piece in pieces:
            piece_list.append(piece.strip("[,],\n"))
        return piece_list


class Level1(Level):

    def welcome(self):
        print("Level 1:\n")

    def round(self, current_turn):
        self.current_turn = current_turn
        self.current_turn += 1
        print(f"Round {self.current_turn}")

    def play(self, color_1, color_2, color_3, color_4):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_4 = color_4
        piece_list = Level.piece_list(1)
        non_color = True
        while non_color:
            self.color_1 = input("1. > ")
            if self.color_1.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_2 = input("2. > ")
            if self.color_2.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_3 = input("3. > ")
            if self.color_3.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_4 = input("4. > ")
            if self.color_4.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        print(f"\nYou guessed {self.color_1}, {self.color_2}, {self.color_3}, {self.color_4}.\n")
        Level1.board_write(self)

    def board_write(self):
        board_file = open("mastermind_board.txt", 'a+')
        # board_file.seek(self.current_turn)
        print(board_file.seek(self.current_turn))
        line = f"{self.current_turn} | {self.color_1} | {self.color_2} | {self.color_3} | {self.color_4}\n"
        board_file.write(line)
        board_file.close()
        Level2.board_read(self)

    def board_read(self):
        print("Here's the board:\n")
        board_file = open("mastermind_board.txt")
        print(board_file.read())
        board_file.close()
        Level2.round(self, self.current_turn)
        Level2.play(self, 1, 2, 3, 4)


class Level2(Level):

    def welcome(self):
        print("Level 2:\n")

    def round(self, current_turn):
        self.current_turn = current_turn
        self.current_turn += 1
        print(f"Round {self.current_turn}")

    def play(self, color_1, color_2, color_3, color_4):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_4 = color_4
        piece_list = Level.piece_list(1)
        non_color = True
        while non_color:
            self.color_1 = input("1. > ")
            if self.color_1.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_2 = input("2. > ")
            if self.color_2.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_3 = input("3. > ")
            if self.color_3.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_4 = input("4. > ")
            if self.color_4.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        print(f"\nYou guessed {self.color_1}, {self.color_2}, {self.color_3}, {self.color_4}.\n")
        Level2.board_write(self)

    def board_write(self):
        board_file = open("mastermind_board.txt", 'a+')
        # board_file.seek(self.current_turn)
        print(board_file.seek(self.current_turn))
        line = f"{self.current_turn} | {self.color_1} | {self.color_2} | {self.color_3} | {self.color_4}\n"
        board_file.write(line)
        board_file.close()
        Level2.board_read(self)

    def board_read(self):
        print("Here's the board:\n")
        board_file = open("mastermind_board.txt")
        print(board_file.read())
        board_file.close()
        Level2.round(self, self.current_turn)
        Level2.play(self, 1, 2, 3, 4)


class Level3(Level):

    def welcome(self):
        print("Level 3:\n")

    def round(self, current_turn):
        self.current_turn = current_turn
        self.current_turn += 1
        print(f"Round {self.current_turn}")

    def play(self, color_1, color_2, color_3, color_4):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_4 = color_4
        piece_list = Level.piece_list(1)
        non_color = True
        while non_color:
            self.color_1 = input("1. > ")
            if self.color_1.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_2 = input("2. > ")
            if self.color_2.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_3 = input("3. > ")
            if self.color_3.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        non_color = True
        while non_color:
            self.color_4 = input("4. > ")
            if self.color_4.lower() in piece_list:
                non_color = False
            else:
                print("\nTry yellow, blue, red, green, orange or purple.")
        print(f"\nYou guessed {self.color_1}, {self.color_2}, {self.color_3}, {self.color_4}.\n")
        Level3.board_write(self)

    def board_write(self):
        board_file = open("mastermind_board.txt", 'a+')
        # board_file.seek(self.current_turn)
        print(board_file.seek(self.current_turn))
        line = f"{self.current_turn} | {self.color_1} | {self.color_2} | {self.color_3} | {self.color_4}\n"
        board_file.write(line)
        board_file.close()
        Level3.board_read(self)

    def board_read(self):
        print("Here's the board:\n")
        board_file = open("mastermind_board.txt")
        print(board_file.read())
        board_file.close()
        Level3.round(self, self.current_turn)
        Level3.play(self, 1, 2, 3, 4)


class GameMap(object):

    levels = {
        'game': Game(),
        'level_one': Level1(),
        'level_two': Level2(),
        'level_three': Level3(),
    }


run_game = GameMap.levels['game']
print("")
print(dir(run_game))
print("")
print(run_game.__class__)
print("")
start_level = run_game.start_game(1)
print(start_level)
print("")
start_level_go = GameMap.levels[start_level]
print(start_level_go)
print("")
print(dir(start_level_go))
print("")
stored_color_code = start_level_go.piece_dict()
print(stored_color_code)
print("")
start_turn = start_level_go.welcome()
start_turn = start_level_go.round(0)
start_turn = start_level_go.play(1, 2, 3, 4)

# def color_check():
#     piece_list_check = Level.piece_list(1)
#     if color_1 not in piece_list_check:
#         print("fix")
#     if color_2 not in piece_list_check:
#         print("fix")
#     if color_3 not in piece_list_check:
#         print("fix")
#     if color_4 not in piece_list_check:
#         print("fix")

# run_game.start_game(1)

# print(dir(run_game))
#
