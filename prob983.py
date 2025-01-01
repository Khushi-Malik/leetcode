"""983. Minimum Cost For Tickets"""

def mincostTickets(self, days: list[int], costs: list[int]) -> int:
    """1 day pass: cost[0]
    7 day pass: cost[1]
    30 day pass: cost[2]
    """
    # dp[i] minimum cost to travel till day i
    # base case: dp[0] no cost to travel before day 1

    travel_days = set(days)
    last_day = max(days)

    dp = [0]*(last_day+1)

    for i in range(0, last_day+1):
        if i not in travel_days:
            dp[i]=dp[i-1]
        else:
            cost1day = costs[0] + dp[i-1]
            if i >= 7:
                cost7day = costs[1] + dp[i-7]
            else:
                cost7day = costs[1]
            if i >= 30:
                cost30day = costs[2] + dp[i-30]
            else:
                cost30day = costs[2]
            
            dp[i] = min(cost1day, cost7day, cost30day)

    return dp[last_day]





