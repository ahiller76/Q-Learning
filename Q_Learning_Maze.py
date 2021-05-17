### Aaron Hiller, Kit Sloan

import numpy as np
import matplotlib.pyplot as plt


steps = 5000
#                   L  R  U  D
States = np.array([[1, 2, 1, 5],
                   [1, 3, 2, 6],
                   [2, 4, 3, 7],
                   [3, 4, 4, 8],
                   [5, 6, 1, 9],
                   [5, 7, 2, 10],
                   [6, 8, 3, 11],
                   [7, 8, 4, 12],
                   [9, 10, 5, 13],
                   [9, 11, 6, 14],
                   [10, 12, 7, 15],
                   [11, 12, 8, 16],
                   [13, 14, 9, 13],
                   [13, 15, 10, 14],
                   [14, 16, 11, 15],
                   [15, 16, 12, 16]])

# Initialize arrays
Q = np.zeros((States.shape[0],States.shape[1]), dtype = float)
P = np.zeros(States.shape[1], dtype = float)
Q_hist = np.zeros((steps,States.shape[0],States.shape[1]), dtype = float)
Q_9_1 = []
Q_9_2 = []
Q_9_3 = []
Q_9_4 = []

# Define learning gains
tao = 0.99
ata = 0.2
beta = 0.4

# Initialize the state at 1
s = 1
s_vect = [s]

for i in range(steps):

    sum = 0
    for a in range(States.shape[1]):
        sum = sum + np.exp(Q[s-1][a]/tao)

    for a in range(States.shape[1]):
        P[a] = np.exp(Q[s-1][a]/tao)/sum

    rand = np.random.rand()

    if rand <= P[0]:
        a = 0                                                   # Move Left
    elif rand <= (P[0]+P[1]):
        a = 1                                                   # Move Right
    elif rand <= (P[0]+P[1]+P[2]):
        a = 2                                                   # Move Up
    else:
        a = 3                                                   # Move Down

    newS = States[s-1][a]

    if newS == 12:
        r = 20
    elif newS == 7 or newS == 14:
        r = -10
    else:
        r = 0

    maxQ = Q[newS-1].max()

    Q[s-1][a] = (1-ata)*Q[s-1][a]+ata*(r+beta*maxQ)
    s_vect.append(newS)
    if newS == 12:
        print("----------------------------------");
        print("The goal is reached! The path is:")
        print(s_vect)
        s_vect = [1]
        print("")
        print("Return to the start position.")
        s = 1
    else:
        s = newS

    tao = tao * .999
    if tao < .04:
        tao = .04
    Q_hist[i] = Q
    Q_9_1.append(Q_hist[i][8][0])
    Q_9_2.append(Q_hist[i][8][1])
    Q_9_3.append(Q_hist[i][8][2])
    Q_9_4.append(Q_hist[i][8][3])

t = np.linspace(1,steps, steps)
plt.plot(t,Q_9_1, label = 'Q(9,1)')
plt.plot(t,Q_9_2 , label = 'Q(9,2)')
plt.plot(t,Q_9_3, label = 'Q(9,3)')
plt.plot(t,Q_9_4,label = 'Q(9,4)')
plt.legend()
plt.show()