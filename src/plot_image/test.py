from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot  # 注意Subplot第一字母大写

plt.plot([1,2,3,4],[2,3,4,5])
plt.xlabel("x",fontsize=100)
plt.show()
#
# # a=figure(figsize=(10,2)) # 建立一个figure
# a = plt.figure()
#
# ax = Subplot(a, 211)
# a.add_subplot(ax)  # 将Subplot建立的坐标轴添加到figure a上
#
# ax.axis['right'].set_visible(False)
# ax.axis['top'].set_visible(False)
# ax.axis['left'].set_axisline_style('->')  # 给y轴加一个箭头
# ax.axis['bottom'].set_axisline_style('->')  # 给x轴加一个箭头
#
# ax = Subplot(a, 2, 1, 2)
# a.add_subplot(ax)  # 将Subplot建立的坐标轴添加到figure a上
#
# ax.axis['right'].set_visible(False)
# ax.axis['top'].set_visible(False)
# ax.axis['left'].set_axisline_style('->')  # 给y轴加一个箭头
# ax.axis['bottom'].set_axisline_style('->')  # 给x轴加一个箭头
# show()
