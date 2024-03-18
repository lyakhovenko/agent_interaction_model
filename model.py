import numpy as np
import random
import matplotlib.pyplot as plt

# Создаем карту в виде матрицы 10x10
map_size = 20
map_matrix = np.zeros((map_size, map_size))

# Инициализируем агентов
agents = []
for _ in range(10):
    agent = {
        'x': random.randint(0, map_size - 1),
        'y': random.randint(0, map_size - 1),
        'r': 100,
        'inf': 0
    }
    agents.append(agent)

# Функция для движения агента по карте
def move_agent(agent, move_direction):
    new_x, new_y = agent['x'], agent['y']

    if move_direction == 'вверх' and agent['x'] > 0:
        new_x -= 1
    elif move_direction == 'вниз' and agent['x'] < map_size - 1:
        new_x += 1
    elif move_direction == 'влево' and agent['y'] > 0:
        new_y -= 1
    elif move_direction == 'вправо' and agent['y'] < map_size - 1:
        new_y += 1

    return new_x, new_y

# Функция для движения агента с учетом других агентов и посещенных точек
def move_agent_with_other_agents_and_visited(agent, agents_positions, last_move_direction, visited_positions, s):
    neighbors = [(agent['x']-1, agent['y']), (agent['x']+1, agent['y']), (agent['x'], agent['y']-1), (agent['x'], agent['y']+1)]

    # Составляем список доступных направлений для движения, исключая шаги в сторону других агентов на расстоянии s
    moves = ['вверх', 'вниз', 'влево', 'вправо']
    possible_moves = [move for move in moves if move != last_move_direction]

    for x, y in neighbors:
        if (x, y) in agents_positions:  # Проверяем позиции других агентов
            dx = x - agent['x']
            dy = y - agent['y']
            if dx < 0 and 'вверх' in possible_moves:
                possible_moves.remove('вверх')
            if dx > 0 and 'вниз' in possible_moves:
                possible_moves.remove('вниз')
            if dy < 0 and 'влево' in possible_moves:
                possible_moves.remove('влево')
            if dy > 0 and 'вправо' in possible_moves:
                possible_moves.remove('вправо')

    # Исключаем направления, ведущие к уже посещенным точкам
    for x, y in visited_positions:
        dx = x - agent['x']
        dy = y - agent['y']
        if dx < 0 and 'вверх' in possible_moves:
            possible_moves.remove('вверх')
        if dx > 0 and 'вниз' in possible_moves:
            possible_moves.remove('вниз')
        if dy < 0 and 'влево' in possible_moves:
            possible_moves.remove('влево')
        if dy > 0 and 'вправо' in possible_moves:
            possible_moves.remove('вправо')

    if not possible_moves:
        move_direction = random.choice(moves)
        new_x, new_y = move_agent(agent, move_direction)
        return new_x, new_y, move_direction
        #return agent['x'], agent['y'], last_move_direction  # Если все направления заблокированы, агент стоит на месте
    else:
        move_direction = random.choice(possible_moves)
        new_x, new_y = move_agent(agent, move_direction)
        return new_x, new_y, move_direction

# Имитация прохождения агентов по карте с учетом других агентов
agents_positions = set()  # для отслеживания позиций агентов
for agent in agents:
    visited_positions = set()  # для отслеживания посещенных позиций
    last_move_direction = None

    for _ in range(20):  # делаем 20 шагов для каждого агента
        new_x, new_y, last_move_direction = move_agent_with_other_agents_and_visited(agent, agents_positions, last_move_direction, visited_positions, 4)

        if (new_x, new_y) not in visited_positions:  # проверяем, что позиция не была посещена
            agent['x'], agent['y'] = new_x, new_y
            agent['r'] -= 1  # уменьшаем ресурсы
            agent['inf'] += 1  # увеличиваем количество информации

            visited_positions.add((new_x, new_y))
        else:
            agent['x'], agent['y'] = new_x, new_y
            agent['r'] -= 1  # уменьшаем ресурсы
            visited_positions.add((new_x, new_y))

    agents_positions.add((agent['x'], agent['y']))

# Выводим информацию об агентах и сумму ресурсов и информации всех агентов
resources_sum = 0
information_sum = 0
for idx, agent in enumerate(agents):
    resources_sum += agent['r']
    information_sum += agent['inf']


print(information_sum)

