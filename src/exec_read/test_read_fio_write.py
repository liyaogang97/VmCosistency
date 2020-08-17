from read_fio_write import read_fio_write
import pymysql

# path = input("请输入文件路径:   ")

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table fio_write")

read_fio_write(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\6230\micro_benchmark_6230\\micro_benchmark_6230_vm\\fio_write\\",
    "6230")
read_fio_write(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\8260\\micro_benchmark_8260\\micro_benchmark_8260_vm\\fio_write\\",
    "8260")
read_fio_write(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\8269\\micro_benchmark_8269\\micro_benchmark_8269_vm\\fio_write\\",
    "8269")
