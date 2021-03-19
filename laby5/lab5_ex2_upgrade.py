import numpy as np

def bday(guests):
    f = open("upgrade.txt", "w")
    f.write("Checking for "+str(guests)+" people BDay at the same day \n")

    people = 366
    n = 500

    for p in range(2, people + 1):
        success = 0
        for room in range(n):
            counter = 0
            A = np.random.randint(1, 365, (p))
            A.sort()
            for i in range(p - 1):
                if A[i] == A[i + 1]:
                    counter += 1
                    if counter == guests-1:  # 2 for 3 people, 3 for 4 people etc.
                        success += 1
                        break
                else:
                    counter = 0

        f.write(str(p) + ") for these many people in the room, probability: " + str(
            success / n) + "\n")

    f.close()
bday(5)