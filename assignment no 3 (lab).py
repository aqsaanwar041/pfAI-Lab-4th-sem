
from typing import Tuple, List, Optional, Set
CAP1 = 4  
CAP2 = 3  
GOAL = 2  

State = Tuple[int, int]         
Action = Tuple[str, State]      

def successors(state: State) -> List[Action]:
    x, y = state
    actions: List[Action] = []

    if x < CAP1:
        actions.append(("Fill Jug1", (CAP1, y)))

    if y < CAP2:
        actions.append(("Fill Jug2", (x, CAP2)))

    if x > 0:
        actions.append(("Empty Jug1", (0, y)))

    if y > 0:
        actions.append(("Empty Jug2", (x, 0)))

    if x > 0 and y < CAP2:
        transfer = min(x, CAP2 - y)
        actions.append(("Pour Jug1->Jug2", (x - transfer, y + transfer)))
    if y > 0 and x < CAP1:
        transfer = min(y, CAP1 - x)
        actions.append(("Pour Jug2->Jug1", (x + transfer, y - transfer)))

    return actions

def dfs_search(start: State) -> Optional[List[Action]]:
    visited: Set[State] = set()

    def dfs(current: State, path: List[Action]) -> Optional[List[Action]]:
        if current in visited:
            return None
        visited.add(current)

        x, y = current
        if x == GOAL or y == GOAL:
            return path  

        for action_desc, new_state in successors(current):

            if new_state in visited:
                continue
            new_path = path + [(action_desc, new_state)]
            result = dfs(new_state, new_path)
            if result is not None:
                return result
        return None

    return dfs(start, [])  

def print_solution(start: State, solution: List[Action]) -> None:
    print(f"Start state: {start}")
    step = 1
    for action_desc, state in solution:
        print(f"Step {step}: {action_desc}  ->  {state}")
        step += 1
    final_state = solution[-1][1] if solution else start
    print(f"\nGoal reached at: {final_state}")

if __name__ == "__main__":
    start_state = (0, 0)
    solution = dfs_search(start_state)
    if solution:
        print_solution(start_state, solution)
    else:
        print("No solution found.")
