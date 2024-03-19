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
plt.plot(results_program1, label="Без использования модели")
plt.plot(results_program2, label="С использованием разработанной моделью")
plt.xlabel("Номер эксперимента")
plt.ylabel("Объем полученой информации")
plt.title("График значений объема полученной информации группой агентов")
plt.legend()
plt.savefig("test.png")
# plt.show()
