def water_jug_dfs(jug1,jug2,target):
    visited=set()
    result=[]
    def dfs(x,y,path):
        if (x,y) in visited:
            return False
        visited.add((x,y))
        path.append((x,y))
        if x == target:
            result.extend(path)
            return True
        next_states = [
            (jug1,y),   
            (x,jug2),   
            (0,y),      
            (x,0),      
            (x-min(x,jug2-y),y+min(x,jug2-y)),  
            (x+min(y,jug1-x),y-min(y,jug1-x))   
        ]
        for nx, ny in next_states:
            if dfs(nx,ny,path.copy()): 
                return True
        return False
    if dfs(0,0,[]):
        print("Solution is found\n")
        print("Optimal steps (DFS):\n")
        for i, state in enumerate(result):
            print(f"Step {i}: {state}")
        print("\nTotal steps =", len(result)-1)
    else:
        print("Solution is not found")

if __name__ == "__main__":
    j1=int(input("Enter Jug1 capacity: "))
    j2=int(input("Enter Jug2 capacity: "))
    target=int(input("Enter target: "))
    water_jug_dfs(j1,j2,target)
