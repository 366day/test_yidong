""" yaml调用封装 """
import yaml

def get_yaml(filename):
    data_file = '../yidong_web/IP_Intelligent_system/data/' + filename
    with open(data_file,encoding='utf-8') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


