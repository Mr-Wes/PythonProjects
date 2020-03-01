# 自动提交代码到github
# 前提：已配置好用户名，密码，ssh等设置

import os
from git import Repo

paths = ('D:\programworkspace\AndroidProjects',
'D:\programworkspace\CProjects',
'D:\programworkspace\JavaProjects',
'D:\programworkspace\PythonProjects')	# 定义元组，其中存放代码仓库的路径


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("-----------")
        print(root)   #os.walk()所在目录
        print(dirs)   #os.walk()所在目录的所有目录名
        print(files)   #os.walk()所在目录的所有非目录文件名
        print(" ")

def test_tree():
    pass


if __name__ == "__main__":
    count = 0
    while count<len(paths):
        os.chdir(paths[count]) # 切换目录
        # 检查树的状态
        # add.
        # 合并
        # 切换目录
        # 提交
        # 切换目录
        repo = git.Repo(paths[count])
        print(repo.git.status())
        count+=1

    
