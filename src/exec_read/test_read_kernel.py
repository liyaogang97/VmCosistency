from read_kernel import read_kernel
import pymysql

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table kernel")

read_kernel("E:\\虚拟机一致性\\实验数据\\8260\\kernelResult_8260\\kernelResult_8260_pm\\", "8260")
read_kernel("E:\\虚拟机一致性\\实验数据\\6230\\kernelResult_6230\\kernelResult_6230_pm\\", "6230")
read_kernel("E:\\虚拟机一致性\\实验数据\\8269\\kernelResult_8269\\kernelResult_8269_pm\\", "8269")
