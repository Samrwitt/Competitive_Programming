from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        all_players = set()
        
        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            losses[loser] = losses.get(loser, 0) + 1
        
        zero_losses = []
        one_loss = []
        
        for player in all_players:
            if losses.get(player, 0) == 0:
                zero_losses.append(player)
            elif losses.get(player, 0) == 1:
                one_loss.append(player)
        
        zero_losses.sort()
        one_loss.sort()
        
        return [zero_losses, one_loss]