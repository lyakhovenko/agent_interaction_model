import subprocess
import matplotlib.pyplot as plt


program1 = "python exp.py"
program2 = "python model.py"

results_program1 = []
results_program2 = []

# Запускаем программы и считываем результаты
for _ in range(500):
    process1 = subprocess.Popen(program1, shell=True, stdout=subprocess.PIPE)
    output1 = process1.communicate()[0].decode()
    #results_program1.extend(map(int, output1))
    results_program1.append(int(output1))

    process2 = subprocess.Popen(program2, shell=True, stdout=subprocess.PIPE)
    output2 = process2.communicate()[0].decode()
    #results_program2.extend(map(int, output2))
    results_program2.append(int(output2))

# Строим график
plt.figure(figsize=(12, 6))
plt.plot(results_program1, label='Без использования модели')
plt.plot(results_program2, label='С использованием разработанной моделью')
plt.xlabel('Номер эксперимента')
plt.ylabel('Объем полученой информации')
plt.title('График значений объема полученной информации группой агентов')
plt.legend()
plt.show()