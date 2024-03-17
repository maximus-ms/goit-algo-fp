import heapq

items = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350},
}

def greedy_algorithm(budget):
    remain_budget = budget
    res = []
    effective_q = [ (val["cost"]/val["calories"], name) for name, val in items.items() ]
    heapq.heapify(effective_q)

    calories = 0
    while remain_budget and effective_q:
        item = heapq.heappop(effective_q)[1]
        cost = items[item]["cost"]
        if cost <= remain_budget:
            remain_budget -= cost
            res.append(item)
            calories += items[item]["calories"]

    return calories, res

K = None
def dynamic_programming(budget):
    global K
    if K is None:
        names = list(items.keys())
        values = list(items.values())
        total_cost = sum( i["cost"] for i in items.values() )
        n = len(items)
        K_ = [[(0, []) for _ in range(total_cost + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            p_i = i - 1
            for budget in range(1, total_cost + 1):
                res = K_[p_i][budget]
                prev_cost = values[p_i]["cost"]
                if prev_cost <= budget:
                    v = K_[p_i][budget - prev_cost][0] + values[p_i]["calories"]
                    if res[0] < v:
                        res_names = list(K_[p_i][budget - prev_cost][1])
                        res_names.append(names[p_i])
                        res = (v, res_names)
                K_[i][budget] = res
        K = K_[n]

    return K[budget]

if __name__ == "__main__":
    # Lets compare greedy_algorithm() and dynamic_programming()
    total_cost = sum( i["cost"] for i in items.values() )
    print("Total cost:", total_cost)
    for budget in range(5, total_cost, 5):
        r1 = greedy_algorithm(budget)
        r2 = dynamic_programming(budget)
        if r2[0] != r1[0]:
            print(f"Budget: {budget}")
            print(f"Greedy alg:   {r1[0]} ({', '.join(r1[1])})")
            print(f"Dynamic prog: {r2[0]} ({', '.join(r2[1])})")

