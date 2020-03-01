import win32api
from win32con import FILE_ATTRIBUTE_HIDDEN

# 格式化文件名，文件名过长时用...替代


def formatFileName(name):
    if len(name.encode('gbk')) > 45:
        name = name[0:-3] + '...'
    return name


# 初始化json文件，并保持打开状态
def initFile(file_path):
    with open(file_path, 'w+', encoding='utf-8') as f:
        f.write('{"文件名称":"备注内容"}')
        f.close()
    win32api.SetFileAttributes(file_path, FILE_ATTRIBUTE_HIDDEN)