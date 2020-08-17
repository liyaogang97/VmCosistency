import linecache
import pymysql
import os
import re


def read_PI5000(path, type):
    db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
    cursor = db.cursor()

    # 获取内存目录
    # l = os.listdir(path)
    # memArray = ["4G"]
    # for e in l:
    #     e = str(e)
    #     if (e.find("G") != -1):
    #         memArray.append(e)

    mem = "4G"
    l = os.listdir(path + "\\" + mem)

    # 获取CPU目录
    cpuArray = []
    for e in l:
        e = str(e)
        if (e.find("C") != -1):
            cpuArray.append(e)

    # 正则化获取内存大小
    L = re.findall(r"\d+\.?\d*", mem)
    L = list(map(float, L))
    memCount = L[0]

    for cpu in cpuArray:
        # 正则化获取CPU数量
        L = re.findall(r"\d+\.?\d*", cpu)
        L = list(map(float, L))
        cpuCount = L[0]

        # 获取result文件名字
        l = os.listdir(path + "\\" + mem + "\\" + cpu)
        resultArray = []
        for e in l:
            e = str(e)
            if (e.find("result") != -1 and e.find("txt") == -1):
                resultArray.append(e)

        for result in resultArray:
            real_time_total = 0
            user_time_total = 0
            sys_time_total = 0
            # print(resultArray)
            # 正则表达式匹配
            L = re.findall(r"\d+\.?\d*", result)
            L = list(map(float, L))
            frequency = L[0]
            # print("frequency"+str(frequency))

            for index in range(0, int(cpuCount)):
                filePath = path + "\\" + mem + "\\" + cpu + "\\" + result + "\\" + "cpu_" + str(
                    index) + ".txt"
                lines = linecache.getlines(filePath)

                print(cpu)
                print(frequency)
                print(index)

                real_time = lines[-3].split()[1]
                m_index = real_time.index("m")
                s_index = real_time.index("s")
                # print(real_time[0:m_index])
                # print(real_time[m_index + 1:s_index])
                real_time_total += 60 * int(real_time[0: m_index]) + float(real_time[m_index + 1:s_index])

                user_time = lines[-2].split()[1]
                m_index = user_time.index("m")
                s_index = user_time.index("s")
                # print(user_time)
                # print(user_time[0:m_index])
                # print(user_time[m_index + 1:s_index])
                user_time_total += 60 * int(user_time[0:m_index]) + float(user_time[m_index + 1: s_index])

                sys_time = lines[-1].split()[1]
                m_index = sys_time.index("m")
                s_index = sys_time.index("s")
                sys_time_total += 60 * int(sys_time[0: m_index]) + float(sys_time[m_index + 1: s_index])

            real_time_total = real_time_total / int(cpuCount)
            user_time_total = user_time_total / int(cpuCount)
            sys_time_total = sys_time_total / int(cpuCount)
            reciprocal_real_time_total = 1000.0 / float(real_time_total)
            reciprocal_user_time_total = 1000.0 / float(user_time_total)
            # reciprocal_sys_time_total = 1000.0 / float(sys_time_total)

            for memCount in [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]:
                cursor.execute('insert into pi5000 values (%s,%f,%f,%f,%f,%f,%f,%f,%f)' % (
                    type, cpuCount, frequency, memCount, real_time_total, reciprocal_real_time_total, user_time_total,
                    reciprocal_user_time_total, sys_time_total))
                db.commit()
    db.close()
