import random

enemies = ['Математический монстр', 'Грамматический дракон', 'Исторический злодей']

items = {
    'Карандаш': 'Позволяет решать математические головоломки.',
    'Книга': 'Дает знания о грамматике и литературе.',
    'Словарь': 'Помогает разгадать исторические загадки.'
}

collected_items = set()

def describe_player(player_name, player_health, player_items):
    print(f"{player_name} (Здоровье: {player_health})")
    print("Имеет следующие предметы:")
    for item in player_items:
        print(f"- {item}: {items[item]}")

def battle_enemy(player_name, player_health):
    enemy = random.choice(enemies)
    print(f"Вы встретили {enemy}!")
    enemy_health = random.randint(20, 50)
    while player_health > 0 and enemy_health > 0:
        print(f"{player_name} (Здоровье: {player_health}) против {enemy} (Здоровье: {enemy_health})")
        choice = input("Выберите действие: 1 - Атаковать, 2 - Сбежать: ")
        if choice == '1':
            player_damage = random.randint(10, 20)
            enemy_damage = random.randint(5, 15)
            print(f"Вы нанесли {player_damage} урона {enemy}!")
            print(f"{enemy} нанес {enemy_damage} урона вам!")
            player_health -= enemy_damage
            enemy_health -= player_damage
        elif choice == '2':
            print(f"Вы сбежали от {enemy}!")
            return player_health
    if player_health <= 0:
        print("Вы проиграли в битве. Игра окончена.")
        exit()
    else:
        print(f"Вы победили {enemy}!")
        return player_health

def find_health_kit(player_name, player_health):
    print("Вы нашли аптечку и восстановили здоровье!")
    player_health += random.randint(10, 30)
    return player_health

def end_game(player_name):
    print(f"Поздравляем, {player_name}! Вы успешно завершили задачи в школе и закончили игру.")
    exit()

def main():
    player_name = input("Введите имя игрока: ")
    player_health = 100
    player_items = []

    print(f"Добро пожаловать, {player_name}! Вы отправляетесь в школу.")

    tasks_completed = 0

    while True:
        describe_player(player_name, player_health, player_items)
        print("1 - Идти дальше")
        print("2 - Собрать предмет")
        print("3 - Проверить инвентарь")
        print("4 - Найти аптечку")
        choice = input("Выберите действие: ")

        if choice == '1':
            player_health = battle_enemy(player_name, player_health)
        elif choice == '2':
            item = random.choice(list(items.keys()))
            print(f"Вы нашли {item}! {items[item]}")
            collected_items.add(item)
        elif choice == '3':
            print("Инвентарь:")
            for item in collected_items:
                print(f"- {item}: {items[item]}")
        elif choice == '4':
            player_health = find_health_kit(player_name, player_health)

        if tasks_completed == 3:
            end_game(player_name)

if __name__ == "__main__":
    main()