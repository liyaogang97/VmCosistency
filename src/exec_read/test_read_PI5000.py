from read_PI5000 import read_PI5000
import pymysql

# path = input("请输入文件路径:   ")

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table pi5000")

read_PI5000(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\6230\micro_benchmark_6230\\micro_benchmark_6230_vm\\PI5000\\",
    "6230")
print("6230 finised")
read_PI5000(
    "C:\\Users\\liyaogang\\Desktop\\虚拟机一致性\\实验数据\\8260\\micro_benchmark_8260\\micro_benchmark_8260_vm\\PI5000\\",
    "8260")
print("8260 finised")
read_PI5000(
    "E:\\虚拟机一致性\\实验数据\\8269\\micro_benchmark_8269\\micro_benchmark_8269_vm\\PI5000\\",
    "8269")
print("8269 finised")

read_PI5000("E:\\虚拟机一致性\\实验数据\\shugaung\\micro_benchmark_shuguang\\PI5000_shuguang\\PI5000_shuguang_vm\\", "shuguang")
print("shuguang finised")
