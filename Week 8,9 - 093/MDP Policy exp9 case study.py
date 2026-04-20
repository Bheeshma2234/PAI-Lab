states = ["Idle", "Working"]
actions = ["Work", "Charge"]
gamma = 0.9

reward = {
    "Idle": {"Work": 5, "Charge": 2},
    "Working": {"Work": 3, "Charge": 4}
}

policy = {s: "Work" for s in states}
V = {s: 0 for s in states}

for _ in range(10):

    new_V = V.copy()
    for s in states:
        a = policy[s]
        new_V[s] = reward[s][a] + gamma * V[s]
    V = new_V

    for s in states:
        work_value = reward[s]["Work"] + gamma * V[s]
        charge_value = reward[s]["Charge"] + gamma * V[s]

        if work_value > charge_value:
            policy[s] = "Work"
        else:
            policy[s] = "Charge"

print("Optimal Warehouse Robot Policy:")
print(policy)

print("State Values:")
print(V)
