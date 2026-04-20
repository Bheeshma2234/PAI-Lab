states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9

reward = {"Low": 10, "Medium": 5, "High": -10}

V = {s: 0 for s in states}

for _ in range(20):
    new_V = V.copy()

    for s in states:
        values = []
        
        for a in actions:
            
            values.append(reward[s] + gamma * V[s])
        
        new_V[s] = max(values)

    V = new_V

print("Optimal State Values for Traffic Control:")
print(V)
