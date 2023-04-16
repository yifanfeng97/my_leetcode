class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        while 'R' in senate and 'D' in senate:
            power_R, power_D = 0, 0
            cur = ''
            for w in senate:
                if w == 'R':
                    if power_D == 0:
                        cur += 'R'
                        power_R += 1
                    else:
                        power_D -= 1
                else:
                    if power_R == 0:
                        cur += 'D'
                        power_D += 1
                    else:
                        power_R -= 1
            cur = cur.replace('D', '', power_R)
            cur = cur.replace('R', '', power_D)
            senate = cur
        if 'R' in senate:
            return "Radiant"
        else:
            return "Dire"
        
if __name__ == "__main__":
    # print(Solution().predictPartyVictory("RRDDD"))
    # print(Solution().predictPartyVictory("DDRRR"))
    # print(Solution().predictPartyVictory("DRRD"))
    # print(Solution().predictPartyVictory("DRDRDRDRRDRD"))
    print(Solution().predictPartyVictory("DRRDRDRDRDDRDRDR"))