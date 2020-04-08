import os
import shutil

# 获取桌面路径
desktop = os.path.join(os.path.expanduser('~'),'Desktop')
# print(desktop)

# 输入存放桌面文件的文件夹名字
name = input('请输入清理后的文件夹名字 ：')

clean = os.path.join(desktop,name)

# 判断路径是否存在
isExists = os.path.exists(clean)

if isExists == False:
    # 创建文件夹
    os.mkdir(clean)

# 获取桌面上的所有文件
filename_lst = os.listdir(desktop)
# print(filename_lst)

for file in filename_lst:
    # 拼接获得文件路径
    file_path = os.path.join(desktop,file)
    # 判断是否为文件类型
    if not os.path.isfile(file_path):
        continue
    elif os.path.isfile(file_path):
        # 分割文件名和拓展名
        file_expand = os.path.splitext(file)[1]
        file_expand = file_expand[1:]
        
        # 创建以文件类型为标识的文件夹（即拓展名为文件夹名称）
        expand_file_name = os.path.join(clean,file_expand)
        
        # 判断文件夹名称是否存在
        if not os.path.exists(expand_file_name):
            os.mkdir(expand_file_name)
        
        # 移动文件到相应的文件夹中
        shutil.move(file_path,expand_file_name)
