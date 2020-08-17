from read_ycsb_redis import read_ycsb_redis
import pymysql

# path = input("请输入文件路径:   ")

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table ycsb_redis")

read_ycsb_redis(
    "E:\虚拟机一致性\\实验数据\\8260\\ycsb_redis_8260\\ycsb_redis_8260_vm\\",
    "8260")
read_ycsb_redis(
    "E:\\虚拟机一致性\\实验数据\\6230\\ycsb_redis_6230\\ycsb_redis_6230_vm\\",
    "6230")
