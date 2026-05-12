import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Крест и ноль")
# текст
font = pygame.font.SysFont("Arial", 32)
big_font = pygame.font.SysFont("Arial", 64)

# Загрузка фона
player = pygame.image.load("загрузка.jpg")
player = pygame.transform.scale(player, (600, 600))

# Переменные
state = "menu"
board = [0] * 9
turn = 1
score_x = 0
score_o = 0
rounds = 0

# Кнопки
play_button = pygame.Rect(200, 250, 200, 70)
back_button = pygame.Rect(20, 530, 120, 50)

# проверка победителя.
def check_winner():
    win_coords = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_coords:
        if board[a] != 0 and board[a] == board[b] == board[c]:
            return board[a]
    if 0 not in board:
        return "Draw"
    return None

# сброс раунда
def reset_round():
    global board, turn
    board = [0] * 9
    turn = 1


running = True
while running:
    # 1. ОТРИСОВКА
    #счет
    screen.blit(player, (0, 0))

    if state == "menu":
        pygame.draw.rect(screen, (255, 0, 0), play_button)
        pygame.draw.rect(screen, (0, 0, 0), play_button, 3)
        text = font.render("ИГРАТЬ", True, (0, 0, 0))
        screen.blit(text, (245, 265))  # Исправили plit -> blit

    elif state == "game":
        # Счет
        text_o = font.render(f"O: {score_o}", True, (0, 0, 255))
        text_x = font.render(f"X: {score_x}", True, (255, 0, 0))
        screen.blit(text_o, (20, 20))  # Исправили bilt -> blit
        screen.blit(text_x, (500, 20))

        # Игровое поле
        board_rect = pygame.Rect(150, 150, 300, 300)
        pygame.draw.rect(screen, (0, 0, 0), board_rect, 2)
        # Линии сетки
        pygame.draw.line(screen, (0, 0, 0), (250, 150), (250, 450), 2)
        pygame.draw.line(screen, (0, 0, 0), (350, 150), (350, 450), 2)
        pygame.draw.line(screen, (0, 0, 0), (150, 250), (450, 250), 2)
        pygame.draw.line(screen, (0, 0, 0), (150, 350), (450, 350), 2)

        # Отрисовка фигур
        for i in range(9):
            x = 150 + (i % 3) * 100
            y = 150 + (i // 3) * 100
            if board[i] == 1:
                pygame.draw.line(screen, (255, 0, 0), (x + 20, y + 20), (x + 80, y + 80), 5)
                pygame.draw.line(screen, (255, 0, 0), (x + 80, y + 20), (x + 20, y + 80), 5)
            elif board[i] == 2:
                pygame.draw.circle(screen, (0, 0, 255), (x + 50, y + 50), 40, 5)

        # Кнопка меню
        pygame.draw.rect(screen, (200, 200, 200), back_button)
        back_text = font.render("Меню", True, (0, 0, 0))
        screen.blit(back_text, (35, 535))

        if rounds >= 3:
            final_text = "Игра окончена!"
            msg = big_font.render(final_text, True, (0, 0, 0))
            screen.blit(msg, (120, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if state == "menu":
                if play_button.collidepoint(pos):
                    state = "game"
                    score_x = score_o = rounds = 0
                    reset_round()

            elif state == "game":
                # Клик Меню
                if back_button.collidepoint(pos):
                    state = "menu"

                # Клик игровому полю
                if rounds < 3 and board_rect.collidepoint(pos):
                    col = (pos[0] - 150) // 100
                    row = (pos[1] - 150) // 100
                    idx = row * 3 + col

                    if board[idx] == 0:
                        board[idx] = turn
                        winner = check_winner()
                        if winner:
                            if winner == 1:
                                score_x += 1
                            elif winner == 2:
                                score_o += 1
                            rounds += 1
                            if rounds < 3: reset_round()
                        else:
                            turn = 2 if turn == 1 else 1

    pygame.display.update()

pygame.quit()