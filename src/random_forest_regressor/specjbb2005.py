from sklearn.ensemble import RandomForestRegressor
import pymysql
from pymysql.cursors import DictCursor
import numpy as np
import openpyxl
import math
from openpyxl.styles import PatternFill
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# 列表中元素的数据类型为字典
list_regressor_data = []
db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
# 查询返回字典值
cursor = db.cursor(DictCursor)
cursor.execute('select * from specjbb2005')
# 查询后的字段名称可以有cursor.description
# for col in cursor.description:
#     print(col)
specjbb2005_recordings = cursor.fetchall()

for specjbb2005_recording in specjbb2005_recordings:
    regressor_data = {}
    # 内存
    stream_select_sql = "select * from stream where cpu_number=" + str(
        specjbb2005_recording['cpu_number']) + " and cpu_frequency=" + str(
        specjbb2005_recording['cpu_frequency']) + " and memory_count=" + str(
        specjbb2005_recording['memory_count']) + " and type=" + str(specjbb2005_recording['type'])
    cursor.execute(stream_select_sql)
    stream_select_result = cursor.fetchall()
    # 磁盘I/O读
    fio_read_select_sql = "select * from fio_read where cpu_number=" + str(
        specjbb2005_recording['cpu_number']) + " and cpu_frequency=" + str(
        specjbb2005_recording['cpu_frequency']) + " and memory_count=" + str(
        specjbb2005_recording['memory_count']) + " and type=" + str(specjbb2005_recording['type'])
    cursor.execute(fio_read_select_sql)
    fio_read_select_result = cursor.fetchall()
    # 磁盘I/O写
    fio_write_select_sql = "select * from fio_write where cpu_number=" + str(
        specjbb2005_recording['cpu_number']) + " and cpu_frequency=" + str(
        specjbb2005_recording['cpu_frequency']) + " and memory_count=" + str(
        specjbb2005_recording['memory_count']) + " and type=" + str(specjbb2005_recording['type'])
    cursor.execute(fio_write_select_sql)
    fio_write_select_result = cursor.fetchall()

    linpack_select_sql = "select * from linpack where cpu_number=" + str(
        specjbb2005_recording['cpu_number']) + " and cpu_frequency=" + str(
        specjbb2005_recording['cpu_frequency']) + " and memory_count=" + str(
        specjbb2005_recording['memory_count']) + " and type=" + str(specjbb2005_recording['type'])
    cursor.execute(linpack_select_sql)
    linpack_select_result = cursor.fetchall()

    # CPU计算
    pi5000_select_sql = "select * from pi5000 where cpu_number=" + str(
        specjbb2005_recording['cpu_number']) + " and cpu_frequency=" + str(
        specjbb2005_recording['cpu_frequency']) + " and memory_count=" + str(
        specjbb2005_recording['memory_count']) + " and type=" + str(specjbb2005_recording['type'])
    cursor.execute(pi5000_select_sql)
    pi5000_select_result = cursor.fetchall()

    if (len(stream_select_result) == 1 and len(linpack_select_result) == 1 and len(fio_read_select_result) == 1 and len(
            fio_write_select_result) == 1 and len(pi5000_select_result) == 1):
        regressor_data.update(stream_select_result[0])
        regressor_data.update(fio_read_select_result[0])
        regressor_data.update(fio_write_select_result[0])
        regressor_data.update(specjbb2005_recording)
        regressor_data.update(pi5000_select_result[0])
        regressor_data.update(linpack_select_result[0])
        list_regressor_data.append(regressor_data)

attributes = ["type", "cpu_number", "user", "triad", "thrput"]
print(len(attributes))

train_data = []
train_data_target = []
test_data = []
test_data_target = []
#
# for regressor_data in list_regressor_data:
#     data = []
#     for attribute in attributes:
#         data.append(regressor_data[attribute])
#     if data[0] == "6230" or data[0] == "8269":
#         train_data.append(data)
#         train_data_target.append(data[-1])
#     else:
#         test_data.append(data)
#         test_data_target.append(data[-1])

datasets = []
for regressor_data in list_regressor_data:
    data = []
    for attribute in attributes:
        data.append(regressor_data[attribute])
    datasets.append(data)

np_datasets = np.array(datasets)
train_data, test_data, train_data_target, test_data_target = train_test_split(np_datasets,
                                                                              np_datasets[:, len(attributes) - 1:],
                                                                              test_size=0.3)

print(len(train_data))
print(len(test_data))

np_train_data = np.array(train_data)
np_test_data = np.array(test_data)

# rfr = RandomForestRegressor(n_estimators=180, oob_score=True)

# print(attributes[1:len(attributes) - 1])
# rfr.fit(np_train_data[:, 1:len(attributes) - 1], train_data_target)
# predict_result = rfr.predict(np_test_data[:, 1:len(attributes) - 1])

# test_data_target = np.array(test_data_target)
# print(type(predict_result))
# np.array(test_data_target)
# print(type(test_data_target))
# print(metrics.roc_auc_score(test_data_target, predict_result))
# print(predict_result)

# param_n_estimators = [{'n_estimators': range(100, 500, 20), 'max_features': [1, 2, 3]},
#                       {'bootstrap': [False], 'n_estimators': range(100, 500, 20), 'max_features': [1, 2, 3]}]
# gridsearch = GridSearchCV(estimator=RandomForestRegressor(), param_grid=param_n_estimators,
#                           scoring='neg_mean_squared_error', cv=5)
# gridsearch.fit(np_train_data[:, 1:len(attributes) - 1], train_data_target)
# # gridsearch.grid_scores_
# print(gridsearch.best_params_)
# print(gridsearch.best_score_)

clf = Ridge(alpha=1.0, fit_intercept=True)
clf.fit(np_train_data[:, 1:len(attributes) - 1], train_data_target)
predict_result = clf.predict(np_test_data[:, 1:len(attributes) - 1])
print("score   " + str(clf.score(np_test_data[:, 1:len(attributes) - 1], test_data_target)))

row = 1
col = 1
workbook = openpyxl.Workbook()
sheet = workbook.active
for column_name in attributes:
    sheet.cell(row, col, column_name)
    col += 1
sheet.cell(row, col, "预测值")
col += 1
sheet.cell(row, col, "预测误差百分比")
col += 1
sheet.cell(row, col, "预测误差")

for index in range(0, len(test_data)):
    row += 1
    for col in range(0, len(test_data[index])):
        # print(test_data[index])
        sheet.cell(row, col + 1, test_data[index][col])
        col = len(test_data[index]) + 1
        sheet.cell(row, col, predict_result[index][0])
        # print(predict_result[index])
        error = predict_result[index][0] - float(test_data[index][-1])
        errorPercent = error / float(test_data[index][-1]) * 100
        col += 1
        # print(errorPercent)
        fill = PatternFill("solid", fgColor="1874CD")
        sheet.cell(row, col, errorPercent)
        col += 1
        sheet.cell(row, col, error)

        if math.fabs(errorPercent) > 10:
            sheet.cell(row, col).fill = fill
            sheet.cell(row, col - 1).fill = fill

workbook.save("specjbb2005_data.xlsx")
