from read_SPECjbb2005 import read_SPECjbb2005
import pymysql

# path = input("请输入文件路径:   ")

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table specjbb2005")

read_SPECjbb2005(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\6230\\SPECjbb2005_6230\\SPECjbb2005_6230_vm\\",
    "6230")
read_SPECjbb2005(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\8260\\SPECjbb2005_8260\\SPECjbb2005_8260_vm\\",
    "8260")
read_SPECjbb2005(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\8269\\SPECjbb2005_8269\\SPECjbb2005_8269_vm\\",
    "8269")
