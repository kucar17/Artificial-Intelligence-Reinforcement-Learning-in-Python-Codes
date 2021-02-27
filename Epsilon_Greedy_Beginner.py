import numpy as np
import random
import os
import time
import matplotlib.pyplot as plt

numOfPlays = 500
results = np.zeros(numOfPlays)
wins = 0
losses = 0
winList = [0]
winRateList = [0]

bandit_probs = [0.2, 0.4, 0.6]
epsilon = 0.15

class Bandit:

    def __init__(self, p):

        self.p = p
        self.p_estimate = 0
        self.N = 0
        self.win_count = 0

    def pull(self):
        
        rate = random.uniform(0, 1)

        if rate > self.p:

            return 1

        else:

            return 0

    def update(self, result):
        
        self.N += 1
        self.p_estimate = wins / self.N

        if result == 0:
            self.win_count += 0
            self.p_estimate = self.win_count / self.N

        if result == 1:
            self.win_count += 1
            self.p_estimate = self.win_count / self.N

def findMaxIndex(list):

    max_value = max(list)
    max_index = list.index(max_value)
    return max_index        

bandit1 = Bandit(bandit_probs[0])
bandit2 = Bandit(bandit_probs[1])
bandit3 = Bandit(bandit_probs[2])

i = 0

# PLAY BEGINS

while i < numOfPlays:

    epsilonCheck = random.uniform(0, 1)

    estimatesList = [bandit1.p_estimate, bandit2.p_estimate, bandit3.p_estimate]

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

        if epsilonCheckCheck > 0.5:
            print("You chose exploration and chose Bandit2!")
            result = bandit2.pull()
            bandit2.update(result)
        
        else:
            print("You chose exploration and chose Bandit3!")
            result = bandit3.pull()
            bandit3.update(result)

    i += 1

    if result == 1:
        print("You won!")
        wins += 1
        winList.append(winList[-1] + 1)
    else:
        print("You lost!")
        losses += 1
        winList.append(winList[-1] + 0)

    print("Number of wins:", wins)
    print("Number of losses:", losses)

    totalWins = bandit1.win_count + bandit2.win_count + bandit3.win_count
    winRate = totalWins / i
    winRateList.append(winRate)

    #time.sleep(0.2)
    os.system('cls')

print("Number of wins:", wins)
print("Number of losses:", losses)
print(" ")

print("Number of times played with Bandit1:", bandit1.N)
print("Number of times won with Bandit1:", bandit1.win_count)
print("Bandit1 win estimate:", bandit1.p_estimate)
print(" ")

print("Number of times played with Bandit2:", bandit2.N)
print("Number of times won with Bandit2:", bandit2.win_count)
print("Bandit2 win estimate:", bandit2.p_estimate)
print(" ")

print("Number of times played with Bandit3:", bandit3.N)
print("Number of times won with Bandit3:", bandit3.win_count)
print("Bandit3 win estimate:", bandit3.p_estimate)

print(" ")

plt.plot(winRateList)
plt.show()
plt.grid(True)