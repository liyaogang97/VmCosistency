from read_cloudsuite_in_memory_analytics import read_cloudsuite_in_memory_analytics
import pymysql

db = pymysql.connect("localhost", "root", "me521..", "vmconsistency")
cursor = db.cursor()
cursor.execute("truncate table in_memory_analytics")

read_cloudsuite_in_memory_analytics(
    "E:\系统组\虚拟机一致性\实验数据\\6230\cloudsuite-In-Memory-Analytics_all\cloudsuite-In-Memory-Analytics_vm", "6230")
read_cloudsuite_in_memory_analytics("E:\系统组\虚拟机一致性\实验数据\\8260\cloudsuite_all\cloudsuite-In-Memory-Analytics_vm", "8260")
read_cloudsuite_in_memory_analytics(
    "E:\系统组\虚拟机一致性\实验数据\\8269\cloudsuite-In-Memory-Analytics_all\cloudsuite-In-Memory-Analytic_vm", "8269")
