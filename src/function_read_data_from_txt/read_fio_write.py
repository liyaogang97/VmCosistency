import linecache
import os
import re
import pymysql


def read_fio_write(path, type):
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
        print(mem)
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
                if (e.find("result") != -1):
                    resultArray.append(e)

            for result in  resultArray:

                # 正则表达式匹配
                L = re.findall(r"\d+\.?\d*", result)
                L = list(map(float, L))
                frequency = L[0]

                filePath = path + "\\" + mem + "\\" + cpu + "\\" + result
                lines = linecache.getlines(filePath)
                for line in lines:
                    lineArray = line.split()
                    if (len(lineArray) > 0 and lineArray[0].strip() == "write:"):
                        IOPS_first = lineArray[1].index("=")
                        IOPS_second = lineArray[1].index("k")
                        BW_first = lineArray[2].index("=")
                        BW_second = lineArray[2].index("M")
                        IOPS = lineArray[1][IOPS_first+1:IOPS_second]
                        BW = lineArray[2][BW_first+1:BW_second]
                        cursor.execute('insert into fio_write values (%s,%f,%f,%f,%f,%f)' % (
                            type, cpuCount, frequency,float(memCount), float(IOPS), float(BW)))
                        db.commit()
    db.close()
