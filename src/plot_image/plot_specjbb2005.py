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

select_cpu_number_category = "select distinct cpu_number from specjbb2005 where server_type=%(server_type)s"

select_frequency_category = "select distinct cpu_frequency from specjbb2005 where server_type=%(server_type)s and cpu_number=%(cpu_number)s "

select_record = "select * from specjbb2005 where server_type=%(server_type)s and cpu_number=%(cpu_number)s and cpu_frequency=%(cpu_frequency)s and memory_count=%(memory_count)s"

select_server_type_category = "select distinct server_type from specjbb2005 "
cursor.execute(select_server_type_category)
server_type_category = cursor.fetchall()
print(server_type_category)

first_image_frequency_x = [12, 13, 15, 16, 17, 19, 20, 21]
first_image_vcpu_count = [4, 6, 8, 10, 12, 14]
line_color = ['dimgrey', 'black', 'slategray']
line_marker = ['v', '^', 's', 'p']

figure = plt.figure(figsize=(10, 10))
# fig, axes = plt.subplots(int(len(first_image_vcpu_count) / 2), 2)
# ax=axisartist.Subplot(fig,2,2,1)
# fig.add_axes(ax)
# ax.axis["bottom"].set_axisline_style("-|>", size = 1.5)
# ax.axis["left"].set_axisline_style("->", size = 1.5)
for cpu_count_index in range(0, len(first_image_vcpu_count)):
    ax = Subplot(figure, int(len(first_image_vcpu_count) / 2), 2, cpu_count_index + 1)
    figure.add_subplot(ax)
    values = {}
    values["memory_count"] = "4"
    for server_type_index in range(0, len(server_type_category)):
        values["server_type"] = server_type_category[server_type_index][0]
        # ax = axes[int(cpu_count_index / 2), cpu_count_index % 2]
        values["cpu_number"] = first_image_vcpu_count[cpu_count_index]
        result = []
        for cpu_frequency_index in range(0, len(first_image_frequency_x)):
            values["cpu_frequency"] = first_image_frequency_x[cpu_frequency_index]
            cursor_DictCursor.execute(select_record, values)
            print(values)
            select_result = cursor_DictCursor.fetchall()
            print(select_result)
            result.append(float(select_result[0]['thrput']))
            print()
            print()
        ax.plot(first_image_frequency_x, result, color=line_color[server_type_index],
                marker='v')

        # 设置上边和右边无边框
        ax.axis['right'].set_visible(False)
        ax.axis['top'].set_visible(False)
        ax.axis['left'].set_axisline_style('->')
        ax.axis['bottom'].set_axisline_style('->')

        ax.set_xticks(np.array(first_image_frequency_x))
        ax.set_xlabel("GHz")
        ax.set_ylabel("MB/s")
        ax.set_title('the number of VCPU is ' + str(first_image_vcpu_count[cpu_count_index]))

    print(result)

plt.show()
