import subprocess
import matplotlib.pyplot as plt
import time

from model import run as run_model
from exp import run as run_exp


program1 = "python exp.py"
program2 = "python model.py"

results_program1 = []
results_program2 = []

# Запускаем программы и считываем результаты
for _ in range(500):
    results_program1.append(run_exp())
    results_program2.append(run_model())

# Строим график
plt.figure(figsize=(12, 6))
plt.plot(results_program1, label="Without using the developed model")
plt.plot(results_program2, label="Using the developed model")
plt.xlabel("Experiment number")
plt.ylabel("The volume of information received by a group of agents")
plt.title("Graph of the values ​​of the volume of information received by a group of agents")
plt.legend()
plt.show()
