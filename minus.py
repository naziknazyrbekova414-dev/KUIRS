import pygame
import sys

pygame.init()
s=w, h=800, 600
color =14, 150, 114


def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_win(board, player):
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
        (0, 4, 8), (2, 4, 6)  # Диагонали
    ]
    for coord in win_coords:
        if board[coord[0]] == board[coord[1]] == board[coord[2]] == player:
            return True
    return False


def main():
    board = [" " for _ in range(9)]
    current_player = "X"

    print("Добро пожаловать в Крестики-нолики!")
    print("Используйте цифры от 1 до 9, чтобы сделать ход.")

    for turn in range(9):
        print_board(board)

        while True:
            try:
                move = int(input(f"Игрок {current_player}, ваш ход (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("Эта ячейка занята или введено неверное число. Попробуйте снова.")
            except ValueError:
                print("Ошибка! Введите число от 1 до 9.")

        if check_win(board, current_player):
            print_board(board)
            print(f"Поздравляем! Игрок {current_player} победил!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("Ничья!")


if __name__ == "__main__":
    main()