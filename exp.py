import numpy as np
import random


# Создаем карту в виде матрицы 10x10
def run():
    map_size = 20
    map_matrix = np.zeros((map_size, map_size))

    # Инициализируем агентов
    agents = []
    for _ in range(10):
        agent = {
            "x": random.randint(0, map_size - 1),
            "y": random.randint(0, map_size - 1),
            "r": 100,
            "inf": 0,
        }
        agents.append(agent)

    # Функция для движения агента по карте
    def move_agent(agent, move_direction):
        new_x, new_y = agent["x"], agent["y"]

        if move_direction == "вверх" and agent["x"] > 0:
            new_x -= 1
        elif move_direction == "вниз" and agent["x"] < map_size - 1:
            new_x += 1
        elif move_direction == "влево" and agent["y"] > 0:
            new_y -= 1
        elif move_direction == "вправо" and agent["y"] < map_size - 1:
            new_y += 1

        return new_x, new_y

    # Имитация прохода агентов по карте
    for agent in agents:
        visited_positions = set()  # для отслеживания посещенных позиций
        moves = ["вверх", "вниз", "влево", "вправо"]

        for _ in range(20):  # делаем 20 шагов для каждого агента
            move_direction = random.choice(moves)
            new_x, new_y = move_agent(agent, move_direction)

            if (
                new_x,
                new_y,
            ) not in visited_positions:  # проверяем, что позиция не была посещена
                agent["x"], agent["y"] = new_x, new_y
                agent["r"] -= 1  # уменьшаем ресурсы
                agent["inf"] += 1  # увеличиваем количество информации

                visited_positions.add((new_x, new_y))
            else:
                agent["x"], agent["y"] = new_x, new_y
                agent["r"] -= 1  # уменьшаем ресурсы

                visited_positions.add((new_x, new_y))

    # Выводим информацию об агентах
    # Выводим информацию об агентах и сумму ресурсов и информации всех агентов
    resources_sum = 0
    information_sum = 0

    for idx, agent in enumerate(agents):
        # print(f"Агент {idx + 1}:")
        # print(f"Конечные координаты агента: ({agent['x']}, {agent['y']})")
        # print(f"Оставшиеся ресурсы у агента: {agent['r']}")
        # print(f"Количество информации собранное агентом: {agent['inf']}\n")

        resources_sum += agent["r"]
        information_sum += agent["inf"]

    # print(f"Сумма оставшихся ресурсов всех агентов: {resources_sum}")
    # print(f"Сумма собранной информации всеми агентами без использования модели: {information_sum}")
    return information_sum
