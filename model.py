import numpy as np
import random
import matplotlib.pyplot as plt

# Create a map in the form of a matrix 40x40
def run():
    map_size = 40
    map_matrix = np.zeros((map_size, map_size))
    
    # Initializing agents
    agents = []
    for _ in range(10):
        agent = {
            'x': random.randint(0, map_size - 1),
            'y': random.randint(0, map_size - 1),
            'r': 100,
            'inf': 0
        }
        agents.append(agent)
    
    # Function for agent movement on the map
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
    
    # Function for agent movement taking into account other agents and visited points
    def move_agent_with_other_agents_and_visited(agent, agents_positions, last_move_direction, visited_positions, s):
        neighbors = [(agent['x']-1, agent['y']), (agent['x']+1, agent['y']), (agent['x'], agent['y']-1), (agent['x'], agent['y']+1)]
    
        # Make a list of available directions for movement, excluding steps towards other agents at a distance s
        moves = ['вверх', 'вниз', 'влево', 'вправо']
        possible_moves = [move for move in moves if move != last_move_direction]
    
        for x, y in neighbors:
            if (x, y) in agents_positions:  # Checking the positions of other agents
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
    
        # Exclude directions leading to already visited points
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
    
    # Simulation of agents passing through the map taking into account other agents
    agents_positions = set()  # to track agent positions
    for agent in agents:
        visited_positions = set()  # to track visited positions
        last_move_direction = None
    
        for _ in range(20):  
            new_x, new_y, last_move_direction = move_agent_with_other_agents_and_visited(agent, agents_positions, last_move_direction, visited_positions, 4)
    
            if (new_x, new_y) not in visited_positions:  # check that the position has not been visited
                agent['x'], agent['y'] = new_x, new_y
                agent['r'] -= 1  # reduce resources
                agent['inf'] += 1  # increasing the amount of information
    
                visited_positions.add((new_x, new_y))
            else:
                agent['x'], agent['y'] = new_x, new_y
                agent['r'] -= 1  # уменьшаем ресурсы
                visited_positions.add((new_x, new_y))
    
        agents_positions.add((agent['x'], agent['y']))
    
    # Output information about agents and the sum of resources and information of all agents
    resources_sum = 0
    information_sum = 0
    for idx, agent in enumerate(agents):
        resources_sum += agent['r']
        information_sum += agent['inf']
    
    
    return information_sum
