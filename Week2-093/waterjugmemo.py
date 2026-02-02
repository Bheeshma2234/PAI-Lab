def water_jug_memo(jug1,jug2,target):
    memo = {}  
    def solve(x,y):
        if (x,y) in memo:
            return memo[(x,y)]
        if x == target:
            memo[(x,y)]=[(x,y)]
            return memo[(x,y)]
        memo[(x,y)] = None  
        next_states = [
            (jug1,y),                             
            (x,jug2),                             
            (0,y),                               
            (x,0),                                
            (x-min(x,jug2-y),y+min(x,jug2-y)),  
            (x+min(y,jug1-x),y-min(y,jug1-x))   
        ]
        for nx,ny in next_states:
            if (nx,ny) not in memo or memo[(nx,ny)] is None:
                path = solve(nx,ny)
                if path:
                    memo[(x,y)]=[(x,y)]+path
                    return memo[(x,y)]

        return None
    path = solve(0,0)
    if path:
        print("Solution is found\n")
        print("Optimal path (states only):\n")
        for i, state in enumerate(path):
            print(f"Step {i}: {state}")
        print("\nTotal steps =", len(path) - 1)
    else:
        print("Solution is not found")
if __name__ == "__main__":
    j1=int(input("Enter Jug1 capacity: "))
    j2=int(input("Enter Jug2 capacity: "))
    target=int(input("Enter target (in Jug1): "))
    water_jug_memo(j1,j2,target)
