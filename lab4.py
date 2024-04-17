def knapsack(weights, values, capacity):
    memo = {}

    def knapsack_helper(index, remaining_capacity):
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]

        if index == 0 or remaining_capacity == 0:
            return 0

        if weights[index - 1] > remaining_capacity:
            result = knapsack_helper(index - 1, remaining_capacity)
        else:
            include = values[index - 1] + knapsack_helper(index - 1, remaining_capacity - weights[index - 1])
            exclude = knapsack_helper(index - 1, remaining_capacity)
            result = max(include, exclude)

        memo[(index, remaining_capacity)] = result
        return result

    return knapsack_helper(len(weights), capacity)

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))
