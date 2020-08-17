from read_linpack import read_linpack
import pymysql

# path = input("请输入文件路径:   ")


db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table linpack")

read_linpack(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\6230\micro_benchmark_6230\\micro_benchmark_6230_vm\\linpack\\",
    "6230")
print("6230 finised")
read_linpack(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\8260\\micro_benchmark_8260\\micro_benchmark_8260_vm\\linpack\\",
    "8260")
print("8260 finised")
read_linpack(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\8269\\micro_benchmark_8269\\micro_benchmark_8269_vm\\linpack\\",
    "8269")
print("8269 finised")
read_linpack("E:\\虚拟机一致性\\实验数据\\shugaung\\micro_benchmark_shuguang\\linpack_shuguang\\linpack_shuguang_vm\\",
             "shuguang")
print("shuguang finised")
