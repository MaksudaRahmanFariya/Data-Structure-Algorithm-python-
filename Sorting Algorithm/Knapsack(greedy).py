class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
def fractionalKnapsack(w,arr):
    arr.sort(key=lambda x : (x.profit/x.weight), reverse = True)
    # Result(value in Knapsack)
    finalvalue = 0.0
    for item in arr:
        if item.weight <= w:
            w -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * w /item.weight
            break
    return finalvalue


if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)



