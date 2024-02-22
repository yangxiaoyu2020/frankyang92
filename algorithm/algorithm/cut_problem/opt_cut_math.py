import pulp


def solve_cutting_stock(items, bin_capacities):
    # Initialize the problem as an ILP problem
    prob = pulp.LpProblem("Cutting Stock Problem", pulp.LpMinimize)

    # Define decision variables
    x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)
         for i in range(len(items))
         for j in range(len(bin_capacities))}

    # Objective function: minimize the number of bins used
    prob += pulp.lpSum(x[i, j] for i in range(len(items)) for j in range(len(bin_capacities)))

    # Capacity constraints for each bin
    for j, capacity in enumerate(bin_capacities):
        for i in range(len(items)):
            prob += x[i, j] * items[i] <= capacity

    # Solve the ILP problem
    prob.solve()

    # Extract solution
    used_items = [(i, j) for i in range(len(items)) for j in range(len(bin_capacities)) if x[i, j].varValue == 1]
    num_bins_used = int(pulp.value(prob.objective))

    return num_bins_used, used_items


# Example usage
if __name__ == "__main__":
    items = [4231] * 300
    bin_capacities = [50002]

    num_bins_used, used_items = solve_cutting_stock(items, bin_capacities)
    print("Number of bins used:", num_bins_used)
    print("Items used:", used_items)
