from numpy import random
from collections import defaultdict

MATH_PROB = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def dice_rolls_try(num=10000):
    a = list(random.randint(1, 7, num))
    b = list(random.randint(1, 7, num))
    res = defaultdict(int)
    for i in range(num):
        res[a[i] + b[i]] += 1
    return res


def calc_monte_carlo_probabilities(data):
    factor = sum(i for i in data.values()) / 100
    keys = sorted(list(data.keys()))
    res = {}
    for k in keys:
        res[k] = data[k] / factor
    return res


if __name__ == "__main__":
    for n in (1000, 10000, 100000):
        data = dice_rolls_try(n)
        mc_prob = calc_monte_carlo_probabilities(data)

        print(f"\nMonte Carlo, {n} iterations")
        print(f"|----------------------------------------|")
        print(f"| Result | Math prob |  MC prob  | Error |")
        print(f"|--------|-----------|-----------|-------|")
        for k in MATH_PROB.keys():
            p1 = MATH_PROB[k]
            p2 = mc_prob[k]
            print(f"|{k:^8}|{p1:^11}|{p2:^11}|{abs(p1-p2):^7.3f}|")
