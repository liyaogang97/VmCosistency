from read_fio_read import read_fio_read
import pymysql

# path = input("请输入文件路径:   ")


db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table fio_read")

read_fio_read(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\6230\micro_benchmark_6230\\micro_benchmark_6230_vm\\fio_read\\",
    "6230")
print("6230 finised")
read_fio_read(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\8260\\micro_benchmark_8260\\micro_benchmark_8260_vm\\fio_read\\",
    "8260")
print("8260 finised")
read_fio_read(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\8269\\micro_benchmark_8269\\micro_benchmark_8269_vm\\fio_read\\",
    "8269")
print("8269 finised")
