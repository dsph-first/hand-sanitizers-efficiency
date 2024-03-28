import yaml
import pandas as pd
 
 
SANITIZERS = ['Sagrotan']
 
 
class Config:
    def __init__(self, path) -> None:
        if path == "":
            return None
        self._path = path
        self.__read_config()
        self.sanitizers = self._config['supported_sanitizers']
        self._init_df = pd.read_excel(self._config['data_path'])
        self._init_ques_df = pd.read_excel(self._config['questionaries'])

 
    def get_supported_sanitizers(self):
        return self.__supported_sanitizers(self.sanitizers)
 
    def sanitizers(self):
        return self.sanitizers
 
    def get_init_df(self):
        return self._init_df
    
    def get_init_ques_df(self):
        return self._init_ques_df
 
    def __read_config(self):
        with open(self._path, 'r', encoding='UTF-8') as stream:
            self._config = yaml.safe_load(stream)
 
    def __supported_sanitizers(self, lst):
        res_dict = {}
        for i in range(0, len(lst), 1):
            res_dict[lst[i]] = True
        return res_dict
 