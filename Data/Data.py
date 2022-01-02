import os
import pandas as pd

class MyData:
    @staticmethod
    def get_data():
        temp_path = os.path.abspath(__file__)[:-12]
        data = pd.read_excel(temp_path+'AutomationInfo.xlsx', dtype=str)
        tests_data = []
        moreInfos = []
        # splits more info text file to list per person in str
        for line in open(temp_path+'moreInfo.txt', 'r').readlines():
            if line.strip('\n') == str(len(moreInfos) + 1):
                moreInfos.append('')
            else:
                moreInfos[len(moreInfos) - 1] = moreInfos[len(moreInfos) - 1] + line
        # create dictonary per person and joins info from text
        for i in range(data.shape[0]):
            temp_dic = data.iloc[i].to_dict()
            temp_dic["More Info"] = moreInfos[i]
            if temp_dic['Submit'].lower() == ('no' or False or 'false' or 0):
                temp_dic['Submit'] = 0
            else:
                temp_dic['Submit'] = 1
            tests_data.append(temp_dic)
            return tests_data
