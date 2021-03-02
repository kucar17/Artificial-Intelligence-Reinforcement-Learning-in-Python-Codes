import numpy as np
import random
import os
import time
import matplotlib.pyplot as plt

numOfPlays = 750
#results = np.zeros(numOfPlays)
#wins = 0
#losses = 0
#winList = [0]
#winRateList = [0]
totalResultList = []

bandit_means = [1.5, 2.5, 3.5]

#epsilon = 0 for pure Greedy Algorithm, an epsilon value greater than zero would result with Epsilon - Greedy Algorithm, such as;
epsilon = 0.15
exploreCount = 0

class Bandit:

    def __init__(self, m):

        self.m = m
        self.m_estimate = 0
        self.N = 0
        #self.win_count = 0

    def pull(self):
        
        rate = random.uniform(self.m, 1)
        return rate
        
        """
        if rate < self.p:

            return 1

        else:

            return 0
        """

    def update(self, result):
        
        self.N += 1

        self.m_estimate = (1/self.N) * ((self.N-1) * self.m_estimate + result)

def findMaxIndex(list):

    max_value = max(list)
    max_index = list.index(max_value)
    return max_index        

bandit1 = Bandit(bandit_means[0])
bandit2 = Bandit(bandit_means[1])
bandit3 = Bandit(bandit_means[2])

i = 0

# PLAY BEGINS
totalResultList.append(0)

while i < numOfPlays:

    print("PLAYING...")

    epsilonCheck = random.uniform(0, 1)

    estimatesList = [bandit1.m_estimate, bandit2.m_estimate, bandit3.m_estimate]

    choice = findMaxIndex(estimatesList)

    if epsilonCheck > epsilon:

        if choice == 0:
            print("You chose Bandit1!")
            result = bandit1.pull()
            bandit1.update(result)
        elif choice == 1:
            print("You chose Bandit2!")
            result = bandit2.pull()
            bandit2.update(result)
        else:
            print("You chose Bandit3!")
            result = bandit3.pull()
            bandit3.update(result)
    
    else:

        epsilonCheckCheck = random.uniform(0, 1)
        exploreCount += 1

        if epsilonCheckCheck >= 0.66:
            print("You chose exploration and chose Bandit1!")
            result = bandit1.pull()
            bandit1.update(result)
        
        elif 0.33 <= epsilonCheckCheck < 0.66:
            print("You chose exploration and chose Bandit2!")
            result = bandit2.pull()
            bandit2.update(result)

        else:
            print("You chose exploration and chose Bandit2!")
            result = bandit3.pull()
            bandit3.update(result)

    i += 1
    totalResultListToAppend = totalResultList[-1] + result
    totalResultList.append(totalResultListToAppend)
    """
    if result == 1:
        print("You won!")
        wins += 1
        winList.append(winList[-1] + 1)
    else:
        print("You lost!")
        losses += 1
        winList.append(winList[-1] + 0)
    """
    print("You get", str(result)+"!")

    #totalWins = bandit1.win_count + bandit2.win_count + bandit3.win_count
    #winRate = totalWins / i
    #winRateList.append(winRate)

    # Clearing the screen output once, in order to print out the ultimate results of the algorithm:
    os.system('cls')

print("Times played: ", numOfPlays)
#print("Number of wins:", wins)
#print("Number of losses:", losses)
#print("Win ratio:", winRate)
print(" ")

print("Number of times played with Bandit1:", bandit1.N)
#print("Number of times won with Bandit1:", bandit1.win_count)
print("Bandit1 mean estimate:", bandit1.p_estimate)
print(" ")

print("Number of times played with Bandit2:", bandit2.N)
#print("Number of times won with Bandit2:", bandit2.win_count)
print("Bandit2 mean estimate:", bandit2.p_estimate)
print(" ")

print("Number of times played with Bandit3:", bandit3.N)
#print("Number of times won with Bandit3:", bandit3.win_count)
print("Bandit3 mean estimate:", bandit3.p_estimate)
print(" ")

print("Number of times explore is chosen:", exploreCount)
print("Number of times exploit is chosen:", numOfPlays - exploreCount)

plt.plot(totalResultList)
plt.grid(True)
plt.show()

