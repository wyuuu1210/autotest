import os


# 当前文件的绝对路径
file_path = os.path.abspath(__file__)
# print(file_path)

# 获取当前文件的目录路经
dir_path = os.path.dirname(__file__)
# print(dir_path)

# 获取项目路径
project_path = os.path.dirname(dir_path)
# print(project_path)

# yaml配置文件地址
conf_path = os.path.join(dir_path, "conf.yaml")
# print(yaml_path)

# 测试数据data文件路径
data_path = os.path.join(project_path, "data")

# test_log目录路经
test_log_path = os.path.join(project_path, "test_log")

# 测试报告路经
report_path = os.path.join(project_path,"reports")
# print(report_path)

# 测试用例路经
testcase_path = os.path.join(project_path, "testcase")
# print(testcase_path)
