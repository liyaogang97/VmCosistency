import pymysql
from pymysql.cursors import DictCursor
import matplotlib.pyplot as plt
import numpy as np

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
dict_cursor = db.cursor(DictCursor)
cursor = db.cursor()

select_cpu_number_category = "select distinct cpu_number from stream where server_type=%(server_type)s"
# values = {"type": "8260"}
# cursor.execute(select_cpu_number_category, values)
# cpu_number_category = cursor.fetchall()
# print(cpu_number_category)

select_frequency_category = "select distinct cpu_frequency from stream where server_type=%(server_type)s and cpu_number=%(cpu_number)s "

# values = {"type": "8260"}
# cursor.execute(select_frequency_category, values)
# frequency_category = cursor.fetchall()
# print(frequency_category)

select_record = "select * from stream where server_type=%(server_type)s and cpu_number=%(cpu_number)s and cpu_frequency=%(cpu_frequency)s"


select_server_type_category = "select distinct server_type from stream "
cursor.execute(select_server_type_category)
server_type_category = cursor.fetchall()
print(server_type_category)

for server_type in server_type_category:
    values = {}
    values["server_type"] = server_type[0]
    cursor.execute(select_cpu_number_category, values)
    cpu_number_category = cursor.fetchall()
    # print(str(server_type[0])+"    "+str(cpu_number_category))
    for cpu_number in cpu_number_category:
        values["cpu_number"] = cpu_number[0]
        cursor.execute(select_frequency_category, values)
        cpu_frequency_category = cursor.fetchall()
        print(str(server_type) + "    " + str(cpu_frequency_category))
        for cpu_frequency in cpu_frequency_category:
            values["cpu_frequency"] = cpu_frequency[0]
            # print(values)
            dict_cursor.execute(select_record, values)
            records = dict_cursor.fetchall()
            triad = 0.0
            for record in records:
                # print(record)
                triad = triad + float(record["triad"])
            if len(records) > 0:
                triad = triad / len(records)
            print(str(server_type[0]) + "    " + str(cpu_number[0]) + "    " + str(cpu_frequency[0]) + "    " + str(
                triad))
    #         break
    #     break
    # break
