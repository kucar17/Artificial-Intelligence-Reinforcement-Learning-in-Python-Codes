import numpy as np
import random
import os
import time
import matplotlib.pyplot as plt

numOfPlays = 500
individualResults = []
resultList = []
meanList = []

bandit_means = [1.5, 2.5, 3.5]

#epsilon = 0 for pure Greedy Algorithm, an epsilon value greater than zero would result with Epsilon - Greedy Algorithm, such as;
epsilon = 0.15
exploreCount = 0

class Bandit:

    def __init__(self, m):

        self.m = m
        self.m_estimate = 0
        self.N = 0

    def pull(self):
        
        rate = np.random.randn() + self.m
        return rate
        
    def update(self, result):
        
        self.N += 1

        self.m_estimate = (1 - 1.0/self.N) * self.m_estimate + 1.0/self.N * result

def findMaxIndex(list):

    max_value = max(list)
    max_index = list.index(max_value)
    return max_index        

bandit1 = Bandit(bandit_means[0])
bandit2 = Bandit(bandit_means[1])
bandit3 = Bandit(bandit_means[2])

i = 0

# PLAY BEGINS

while i < numOfPlays:

    print("."*i)
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
    individualResults.append(result)
    resultList.append(sum(individualResults))
    meanList.append(resultList[-1]/i)
    print("You get", str(result)+"!")

    # Clearing the screen output once, in order to print out the ultimate results of the algorithm:
    os.system('cls')

print("Times played:", numOfPlays)
print("Total reward collected:", resultList[-1])
print("Average reward collected on each try:", resultList[-1]/numOfPlays)
print(" ")

print("Number of times played with Bandit1:", bandit1.N)
print("Bandit1 mean estimate:", bandit1.m_estimate)
print(" ")

print("Number of times played with Bandit2:", bandit2.N)
print("Bandit2 mean estimate:", bandit2.m_estimate)
print(" ")

print("Number of times played with Bandit3:", bandit3.N)
print("Bandit3 mean estimate:", bandit3.m_estimate)
print(" ")

print("Number of times explore is chosen:", exploreCount)
print("Number of times exploit is chosen:", numOfPlays - exploreCount)

plt.plot(meanList)
plt.plot(np.ones(i) * bandit_means[0])
plt.plot(np.ones(i) * bandit_means[1])
plt.plot(np.ones(i) * bandit_means[2])
plt.grid(True)
plt.xscale("log")
plt.show()

