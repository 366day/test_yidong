import csv,pytest,os
import pandas as pd


if __name__ == '__main__':
    # pytest.main(['-q', '../PageObject/LoginPage/LoginPage.py', '--alluredir=../Report/json'])
    # os.system('allure generate ../Report/json -o ../Report/Allure-Report --clean')

    file=open("D:\company\project\dyx\web_ZhiNengYunWei\ConfigFile\ConfigFile.csv","r")
    table=csv.reader(file)
    num=0
    for row in table:
        num=num+1
        if num>1 and row[5]=="YES":
            ScriptDir=row[1]
            ScriptName=row[2]
            TestCaseName=row[3]
            print(row[2],":",row[0])
            pytest.main(['-q',ScriptDir+'//'+ScriptName,'--alluredir=../Report/json'])
    os.system('allure generate ../Report/json -o ../Report/Allure-Report --clean')