class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost, reverse=True)

        value = 0

        for i in range(len(cost)):
            if i % 3 != 2:
                value += cost[i]

        return value