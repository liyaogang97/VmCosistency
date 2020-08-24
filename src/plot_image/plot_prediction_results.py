from exec_kernel_prediction import kernel_prediction
from exec_linpack_prediction import linpack_prediction
from exec_specjbb2005_prediction import specjbb2005_prediction
from exec_ycsb_redis_prediction import ycsb_redis_prediction
import matplotlib.pyplot as plt

kernel_r2_list, kernel_MAPE_list = kernel_prediction()
specjbb2005_r2_list, specjbb2005_MAPE_list = specjbb2005_prediction()
ycsb_redis_r2_list, ycsb_redis_MAPE_list = ycsb_redis_prediction()

name_list = ['linux kernel compilation', 'SPECjbb2005', 'YCSB-Redis']
coordinate_list = list(range(len(name_list)))
total_width, n = 0.6, 3
width = total_width / n

linear_r2_list = []
random_r2_list = []
decision_r2_list = []

r2_list = []
r2_list.append(kernel_r2_list)
r2_list.append(specjbb2005_r2_list)
r2_list.append(ycsb_redis_r2_list)

for list_element in r2_list:
    linear_r2_list.append(list_element[0])
    random_r2_list.append(list_element[1])
    decision_r2_list.append(list_element[2])

plt.bar(coordinate_list, linear_r2_list, width=width, label="Linear Regression", facecolor='dimgrey')
for index in range(len(coordinate_list)):
    coordinate_list[index] = coordinate_list[index] + width
plt.bar(coordinate_list, random_r2_list, width=width, label="Random Forest", fc='black', tick_label=name_list)
for index in range(len(coordinate_list)):
    coordinate_list[index] = coordinate_list[index] + width
plt.bar(coordinate_list, decision_r2_list, width=width, label="Decision Tree", fc='slategray')
plt.ylim(0.2, 1.1)
plt.legend(loc="lower center", frameon=False, ncol=4, bbox_to_anchor=(0.5, -0.15))
plt.ylabel("Coefficient of Determination")
plt.savefig("r2.png")
# plt.show()

plt.cla()
#
#
linear_MAPE_list = []
random_MAPE_list = []
decision_MAPE_list = []

MAPE_list = []
MAPE_list.append(kernel_MAPE_list)
MAPE_list.append(specjbb2005_MAPE_list)
MAPE_list.append(ycsb_redis_MAPE_list)

for list_element in MAPE_list:
    linear_MAPE_list.append(list_element[0])
    random_MAPE_list.append(list_element[1])
    decision_MAPE_list.append(list_element[2])

plt.bar(coordinate_list, linear_MAPE_list, width=width, label="Linear Regression", facecolor='dimgrey')
for index in range(len(coordinate_list)):
    coordinate_list[index] = coordinate_list[index] + width
plt.bar(coordinate_list, random_MAPE_list, width=width, label="Random Forest", fc='black', tick_label=name_list)
for index in range(len(coordinate_list)):
    coordinate_list[index] = coordinate_list[index] + width
plt.bar(coordinate_list, decision_MAPE_list, width=width, label="Decision Tree", fc='slategray')
# plt.ylim(0.2, 1.1)
plt.legend(loc="lower center", frameon=False, ncol=4, bbox_to_anchor=(0.5, -0.15))
plt.ylabel("MAPE")
plt.savefig("MAPE.png")
