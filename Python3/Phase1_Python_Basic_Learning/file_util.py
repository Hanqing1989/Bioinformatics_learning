"""
文件处理相关的工具模块
"""

def print_file_info(file_name):
    """
    将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    file=None
    try:
        file=open(file_name,'r')
        content=file.read()
        print('文件的全部内容如下：')
        print(content)
    except Exception as error:
        print(f'程序出现异常，原因是：{error}')
    finally:
        if file:  # 如果变量是None，表示False，如果有任何内容，就是True
                file.close()


def append_to_file(file_name,data):
     """
     将指定的数据追加到指定的文件中
     :param file_name: 指定的文件路径
     :param data: 制定的数据
     :return: None
     """
     file=open(file_name,'a',encoding='UTF-8') # 编码格式不能省，否则添加数据时，换行符无法起作用
     file.write(data)
     file.write('\n')
     file.close()
