import pymysql
from pymysql.cursors import DictCursor
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
dict_cursor = db.cursor(DictCursor)
cursor = db.cursor()
cursor_DictCursor = db.cursor(DictCursor)

select_cpu_number_category = "select distinct cpu_number from pi5000 where server_type=%(server_type)s"

select_frequency_category = "select distinct cpu_frequency from pi5000 where server_type=%(server_type)s and cpu_number=%(cpu_number)s "

select_record = "select * from pi5000 where server_type=%(server_type)s and cpu_number=%(cpu_number)s and cpu_frequency=%(cpu_frequency)s and memory_count=%(memory_count)s"

select_server_type_category = "select distinct server_type from pi5000 "
cursor.execute(select_server_type_category)
server_type_category = cursor.fetchall()
print(server_type_category)

first_image_frequency_x = [12, 13, 15, 16, 17, 19, 20, 21]
first_image_vcpu_count = [8]
line_color = ['dimgrey', 'black', 'silver']
line_marker = ['v', '^', 's', 'p']

figure = plt.figure(figsize=(5, 5))

for cpu_count_index in range(0, len(first_image_vcpu_count)):
    ax = Subplot(figure, 1, 1, 1)
    figure.add_subplot(ax)
    values = {}
    values["memory_count"] = "4"
    line_list = []
    server_type_list = []
    for server_type_index in range(0, len(server_type_category) - 1):
        values["server_type"] = server_type_category[server_type_index][0]
        server_type_list.append(server_type_category[server_type_index][0])
        # ax = axes[int(cpu_count_index / 2), cpu_count_index % 2]
        values["cpu_number"] = first_image_vcpu_count[cpu_count_index]
        result = []
        for cpu_frequency_index in range(0, len(first_image_frequency_x)):
            values["cpu_frequency"] = first_image_frequency_x[cpu_frequency_index]
            cursor_DictCursor.execute(select_record, values)
            select_result = cursor_DictCursor.fetchall()
            # print(select_result)
            result.append(float(select_result[0]['real']))
            # print()
            # print()
        line = ax.plot(np.array(first_image_frequency_x) / 10.0, result, color=line_color[server_type_index],
                       marker='v', lw=2)[0]
        line_list.append(line)

        plt.sca(ax)
        # plt.figure(figsize=(10, 10))
        plt.xlabel("CPU Frequency(GHz)", fontsize=0.5)
        plt.ylabel("Runtime(s)")
        # 设置上边和右边无边框
        ax.axis['right'].set_visible(False)
        ax.axis['top'].set_visible(False)
        ax.axis['left'].set_axisline_style('->')
        ax.axis['bottom'].set_axisline_style('->')

        ax.set_xticks(np.array(first_image_frequency_x) / 10.0)
        ax.set_title('the number of VCPU is ' + str(first_image_vcpu_count[cpu_count_index]))

server_dict = {}
server_dict['6230'] = '#3'
server_dict['8269'] = '#2'
server_dict['8260'] = '#1'

label_list=[]
for server in server_type_list:
    label_list.append(server_dict[server])

print(label_list)
figure.legend(line_list, labels=label_list, frameon=False, ncol=1, bbox_to_anchor=(1, 0.8))
figure.savefig("pi5000.png")
# plt.show()
