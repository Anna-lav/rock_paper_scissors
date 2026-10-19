import random

OPTIONS = ("камень", "ножницы", "бумага")
RESULTS_FILE = "results.txt"


class ScoreBoard:
    """Подсчёт очков: победы игрока и компьютера."""

    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def update(self, result):
        """Обновляет счёт по результату раунда.

        result: 'player', 'computer' или 'draw'
        """
        if result == "player":
            self.player_wins += 1
        elif result == "computer":
            self.computer_wins += 1

    def display(self):
        """Показывает текущий счёт."""
        print(f"Счёт — Вы: {self.player_wins} | Компьютер: {self.computer_wins}")

    def save(self, filename=RESULTS_FILE):
        """Сохраняет результаты в файл."""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Игра окончена. Счёт — Вы: {self.player_wins} | Компьютер: {self.computer_wins}\n")


def get_computer_choice():
    """Случайный выбор компьютера."""
    return random.choice(OPTIONS)


def get_player_choice():
    """Запрашивает выбор у пользователя.

    Возвращает корректный выбор или None при выходе (ввод "0").
    Неверный ввод — повторяет запрос.
    """
    while True:
        choice = input("Ваш ход (камень / ножницы / бумага, 0 — выход): ").lower().strip()
        if choice == "0":
            return None
        if choice in OPTIONS:
            return choice
        print(f"Ошибка: '{choice}' не подходит. Попробуйте снова.")


def determine_winner(player, computer):
    """Определяет победителя.

    Возвращает 'player', 'computer' или 'draw'.
    """
    if player == computer:
        return "draw"
    if (player == "камень" and computer == "ножницы") or \
       (player == "ножницы" and computer == "бумага") or \
       (player == "бумага" and computer == "камень"):
        return "player"
    return "computer"


def main():
    """Основной игровой цикл."""
    print("=== Камень - Ножницы - Бумага ===")
    board = ScoreBoard()

    while True:
        player = get_player_choice()
        if player is None:
            break

        computer = get_computer_choice()
        print(f"Вы: {player} | Компьютер: {computer}")

        result = determine_winner(player, computer)
        if result == "draw":
            print("Ничья!")
        elif result == "player":
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")

        board.update(result)
        board.display()
        print()

    board.save()
    print(f"Счёт сохранён в файл {RESULTS_FILE}")
    print("Игра окончена!")


if __name__ == "__main__":
    main()