import yaml

hand_sanitizers_list = ["Sagrotan"]


def get_config(file_name):
    '''This is the configuaration file
     It takes the file name and returns the load data
    '''
    with open(file_name, 'r', encoding='UTF-8') as stream:
        config = yaml.safe_load(stream)
    return config
