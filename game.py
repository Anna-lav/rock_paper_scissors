import random

OPTIONS = ("камень", "ножницы", "бумага")


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
        print()

    print("Игра окончена!")


if __name__ == "__main__":
    main()