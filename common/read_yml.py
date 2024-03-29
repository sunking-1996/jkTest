import yaml
import os
def readyml(yamlPath):
    '''读取yaml文件内容
    参数path: 相对路径，起始路径：项目的根目录
    realPath: 文件的真实路径,绝对路径地址 '''
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    d = yaml.load(f,Loader=yaml.FullLoader)
    # 用load方法转字典
    print("读取的测试文件数据：%s"%d)
    return d
if __name__ == '__main__':
    readyml("test_data.yml")
