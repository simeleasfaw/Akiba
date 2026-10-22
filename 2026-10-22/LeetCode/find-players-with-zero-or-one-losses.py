class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losers = {}
        for winner, loser in matches:
            if winner not in losers:
                losers[winner] = 0
            if loser not in losers:
                losers[loser] = 0
            losers[loser] += 1

        count_notloser = []
        count_loser = []

        for i in losers:
            if losers[i] == 0:
                count_notloser.append(i)
            elif losers[i] == 1:
                count_loser.append(i)

        return [sorted(count_notloser), sorted(count_loser)]
