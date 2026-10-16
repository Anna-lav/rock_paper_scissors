import random


def get_player_choice():
    """Запрашивает выбор у игрока: камень, ножницы или бумага."""
    choice = input("Ваш выбор (камень, ножницы, бумага): ").lower().strip()
    return choice


def get_computer_choice():
    """Случайный выбор компьютера."""
    return random.choice(["камень", "ножницы", "бумага"])


def determine_winner(player, computer):
    """Определяет победителя по классическим правилам."""
    if player == computer:
        return "Ничья!"
    if (
        (player == "камень" and computer == "ножницы")
        or (player == "ножницы" and computer == "бумага")
        or (player == "бумага" and computer == "камень")
    ):
        return "Вы выиграли!"
    return "Компьютер выиграл!"


def main():
    """Основной цикл игры."""
    print("=== Камень-Ножницы-Бумага ===")
    while True:
        player = get_player_choice()
        if player not in ("камень", "ножницы", "бумага"):
            print("Неверный выбор. Попробуйте ещё раз.")
            continue
        computer = get_computer_choice()
        print(f"Компьютер выбрал: {computer}")
        print(determine_winner(player, computer))
        if input("Сыграть ещё раз? (да/нет): ").lower() != "да":
            break
    print("Спасибо за игру!")


if __name__ == "__main__":
    main()