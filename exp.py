import numpy as np
import random


# Create a map in the form of a matrix 40x40
def run():
    map_size = 40
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

    # Function for agent movement on the map
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

    # Simulation of agents' passage on the map
    for agent in agents:
        visited_positions = set()  # to track visited positions
        moves = ["вверх", "вниз", "влево", "вправо"]

        for _ in range(20):  # do 20 steps for each agent
            move_direction = random.choice(moves)
            new_x, new_y = move_agent(agent, move_direction)

            if (
                new_x,
                new_y,
            ) not in visited_positions:  # check that the position has not been visited
                agent["x"], agent["y"] = new_x, new_y
                agent["r"] -= 1  # reduce resources
                agent["inf"] += 1  # increasing the amount of information

                visited_positions.add((new_x, new_y))
            else:
                agent["x"], agent["y"] = new_x, new_y
                agent["r"] -= 1  # reduce resources

                visited_positions.add((new_x, new_y))

    # Displaying information about agents
    # Output information about agents and the sum of resources and information of all agents
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
