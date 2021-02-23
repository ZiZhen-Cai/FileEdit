import os

# 遍历文件、文件夹
def walkFile(path):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    file_list = []
    dir_list = []
    for root,dirs,files in os.walk(path):
        # 遍历所有文件
        for f in files:
            file_list.append(f)
            #完整路径
            #print(os.path.join(root,f))
        # 遍历所有文件夹
        for d in dirs:
            dir_list.append(d)
            #完整路径
            #print(os.path.join(root,d))

    return file_list,dir_list


def ChangeFileName(path):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    for root,dirs,files in os.walk(path):
        # 遍历所有文件
        #for f in files:
            #print(os.path.join(root,f))
        
        # 遍历所有文件夹,子文件夹重命名
        for d in dirs:
            replace_name = '【鼠绘汉化】海贼王OnePiece'
            if replace_name in d:
                os.rename(os.path.join(root,d), os.path.join(root,d.replace(replace_name,"")))  




if __name__ == '__main__':
    path = "E:\CZZ\Media\hhh\【鼠绘汉化】海贼王OnePiece漫画526-977"
    ChangeFileName(path)
