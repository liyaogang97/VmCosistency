import linecache
import os
import re
import pymysql


def findMaxValue(array):
    maxValue = array[0]

    for value in array:
        if (maxValue > value):
            maxValue = value
    return maxValue


def findMinValue(array):
    minValue = array[0]
    for value in array:
        if (minValue < value):
            minValue = value
    return minValue


def read_ycsb_redis(path, type):
    db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
    cursor = db.cursor()

    # 获取内存目录
    l = os.listdir(path)
    memArray = []
    for e in l:
        e = str(e)
        if (e.find("G") != -1):
            memArray.append(e)

    for mem in memArray:
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
            resultLoadArray = []
            resultRunArray = []

            for e in l:
                e = str(e)
                if (e.find("load") != -1):
                    resultLoadArray.append(e)
                if (e.find("run") != -1):
                    resultRunArray.append(e)

            for result in resultLoadArray:
                # 正则表达式匹配
                L = re.findall(r"\d+\.?\d*", result)
                L = list(map(float, L))
                frequency = L[0]

                filePath = path + "\\" + mem + "\\" + cpu + "\\" + result
                lines = linecache.getlines(filePath)
                for line in lines:
                    # lineArray = line.split()
                    # print(lineArray[0])
                    if (line.find("OVERALL") != -1 and line.find("RunTime") != -1):
                        runTime = float(line.split()[2])

                    if (line.find("OVERALL") != -1 and line.find("Throughput")):
                        throughput = float(line.split()[2])

                    if (line.find("INSERT") != -1 and line.find("Average") != -1):
                        averagelatency = float(line.split()[2])

                    if (line.find("INSERT") != -1 and line.find("95th") != -1):
                        insert_95th = float(line.split()[2])

                    if (line.find("INSERT") != -1 and line.find("99th") != -1):
                        insert_99th = float(line.split()[2])
                # print("type"+str(type))
                # print("cpuCount"+str(cpuCount))
                # print("frequency"+str(frequency))
                # print("memCount"+str(memCount))
                # print("runTime"+str(runTime))
                # print("throughput"+str(throughput))
                # print("averagelatency"+str(averagelatency))
                # print(insert_95th)
                # print(insert_99th)
                cursor.execute('insert into ycsb_load_redis values (%s,%f,%f,%f,%f,%f,%f,%f,%f)' % (
                    repr(type), cpuCount, frequency, memCount, runTime, throughput, averagelatency, insert_95th,
                    insert_99th))
                db.commit()

            for result in resultRunArray:
                # 正则表达式匹配
                L = re.findall(r"\d+\.?\d*", result)
                L = list(map(float, L))
                frequency = L[0]

                filePath = path + "\\" + mem + "\\" + cpu + "\\" + result
                lines = linecache.getlines(filePath)
                runTimeArray = []
                throughputArray = []
                read_averagelatencyArray = []
                read_95thArray = []
                read_99thArray = []
                write_averagelatencyArray = []
                write_95thArray = []
                write_99thArray = []
                for line in lines:
                    # lineArray = line.split()
                    # print(lineArray[0])

                    if (line.find("OVERALL") != -1 and line.find("RunTime") != -1):
                        runTimeArray.append(float(line.split()[2]))

                    if (line.find("OVERALL") != -1 and line.find("Throughput")):
                        throughputArray.append(float(line.split()[2]))

                    if (line.find("READ") != -1 and line.find("95th") != -1):
                        read_95thArray.append(float(line.split()[2]))

                    if (line.find("READ") != -1 and line.find("99th") != -1):
                        read_99thArray.append(float(line.split()[2]))

                    if (line.find("READ") != -1 and line.find("Average") != -1):
                        read_averagelatencyArray.append(float(line.split()[2]))

                    if (line.find("UPDATE") != -1 and line.find("95th") != -1):
                        write_95thArray.append(float(line.split()[2]))

                    if (line.find("UPDATE") != -1 and line.find("99th") != -1):
                        write_99thArray.append(float(line.split()[2]))

                    if (line.find("UPDATE") != -1 and line.find("Average") != -1):
                        write_averagelatencyArray.append(float(line.split()[2]))

                runTime = findMinValue(runTimeArray)
                throughput = findMaxValue(throughputArray)
                read_95th = findMinValue(read_95thArray)
                read_99th = findMinValue(read_99thArray)
                read_averagelatency = findMinValue(read_averagelatencyArray)
                write_95th = findMinValue(write_95thArray)
                write_99th = findMinValue(write_99thArray)
                write_averagelatency = findMinValue(write_averagelatencyArray)

                cursor.execute('insert into ycsb_run_redis values (%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)' % (
                    repr(type), cpuCount, frequency, memCount, runTime, throughput, read_averagelatency, read_95th,
                    read_99th,
                    write_averagelatency, write_95th,
                    write_99th))
                db.commit()
    db.close()
