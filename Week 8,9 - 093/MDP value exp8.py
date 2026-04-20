import numpy as np

size = 4
goal = (3, 3)
trap = (1, 1)
gamma = 0.9
theta = 0.0001

actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

V = np.zeros((size, size))

def get_next_state(state, action):
    i, j = state
    if action == 'UP':
        i = max(i - 1, 0)
    elif action == 'DOWN':
        i = min(i + 1, size - 1)
    elif action == 'LEFT':
        j = max(j - 1, 0)
    elif action == 'RIGHT':
        j = min(j + 1, size - 1)
    return (i, j)

def get_reward(state):
    if state == goal:
        return 0
    elif state == trap:
        return -10
    else:
        return -1

while True:
    delta = 0
    new_V = np.copy(V)

    for i in range(size):
        for j in range(size):
            state = (i, j)

            if state == goal or state == trap:
                continue

            values = []
            for action in actions:
                next_state = get_next_state(state, action)
                reward = get_reward(next_state)
                values.append(reward + gamma * V[next_state])

            new_V[i, j] = max(values)
            delta = max(delta, abs(new_V[i, j] - V[i, j]))

    V = new_V

    if delta < theta:
        break

print("Optimal Value Function:")
print(V)
