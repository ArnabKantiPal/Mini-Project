
import random
import matplotlib.pyplot as plt
j = 1
Array = []
List_of_parameter_Alpha = []
Flip_Count = []

for i in range(100):
    magnetic_moment = random.randrange(-1 ,2 ,2)
    Array.append(magnetic_moment)

print(f"After randomly assigning a constant magnetic moment to each atom in the one dimensional lattice we got: - \n{Array}\n ")

def energy_calculation(Arr):
    E_pre_total = 0
    for element in range(0, len(Arr)):
        if(element + 1 < len(Arr)):
            E_pre_total = Arr[element - 1] * Arr [element] * j + Arr[element] * Arr[element + 1] * j + E_pre_total
        else:
            E_pre_total = Arr[element] * Arr[0] * j + Arr[element] * Arr[element -1] * j + E_pre_total
    E_total = E_pre_total * (1 / 2)
    print(f"Total energy of the one dimension lattice system is:- {E_total}")
    return E_total

def alpha_calculaion(Arr):
    Alpha = 0
    for i in range(0, len(Arr)):
        Alpha = Alpha + Arr[i]
    Alpha = Alpha / len(Arr)
    return Alpha

def Flip_random():
    random_index = random.randint(0, 100)
    print(f"The random position where we are going to flip the direction of magnetic moment :- {random_index}")
    Array[random_index - 1] = -1 * Array[random_index - 1]
    print(f"After flipping the magnetic moment of the array is : - {Array}")
    print(f"After flipping the alpha of the array is : - {alpha_calculaion(Array)}")
    return random_index

energy_initial = energy_calculation(Array)
k = 1
for i in range(20):
    print("start of the iteration")
    random_index = Flip_random()
    energy_final = energy_calculation(Array)
    Alpha = alpha_calculaion(Array)
    List_of_parameter_Alpha.append(Alpha)
    Flip_Count.append(i)
    if (energy_final <= energy_initial):
        print(
            "Since the energy after arrangement is less than equal to the arrangement earlier so we are Accepting the flip")
        energy_initial = energy_final
        print(Array)
        k = k + 1
    else:
        print(
            f"Since the energy of the arrangement after flipping the magnetic moment at position {random_index} is greater than the energy earlier, so we are rejecting the flip")
        Array[random_index] = -1 * Array[random_index]
        print(Array)
    print("end of a iteration \n")

x = Flip_Count
y = List_of_parameter_Alpha
plt.plot(x, y)
plt.xlabel('Flip Count')
plt.ylabel('Values of energy after accepting each flip')
plt.title('variation of total energy after each flip of magnetic moment')
plt.grid(True)
plt.show()

