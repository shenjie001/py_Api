import requests
import json
from py_Api.commonClass.DB import sqlClass
from py_Api.commonClass.readConfig import  readConfig
from py_Api.commonClass.C_except import comperaExcept
from py_Api.commonClass.readExcel import doExcel
class http(object):
    def sendHttp(URL,params,header,timeout):
        #try:
        if params=='':
            return
        else:
            Xparams = json.loads(params)
            print("请求地址："+URL)
            print("请求参数："+params)
            response = requests.post(url=URL, params=Xparams, headers=header, timeout=timeout)
            return response
        #except:
           #print("请求失败")



    def getHttp(URL):
        response=requests.get(URL)
        return response


    def getToken(str1):
     if str1 is None:
         return
     else:
        dic=json.loads(str1)
        token=dic["data"]["token"]
        return token


    def respons(reponses,Except):
        if reponses is None:
            print('实际结果为：null')
            comperaExcept.compera(reponses, Except)
        else:
            print("实际结果为：")
            print(reponses.text)
            print('预期结果为：' + Except + '')
            comperaExcept.compera(reponses, Except)
            str1=str(reponses.text)
            if 'token'in str1:
                token=http.getToken(str1)
                print("获取到token:"+token)
                return token
            else:
                token=''
                return token


    def HttpTest(Data):
        params = doExcel.retrunParam(Data)
        num = len(Data)
        sql = doExcel.retrunSql(Data)
        Except = doExcel.retrunExcept(Data)
        url=doExcel.retrunUrl(Data)
        timeout = 1.0
        header = {'Content-Type': 'application/json'}
        i = 1
        token=''
        while i <= num:
            try:
                if (len(sql[i]) > 0):
                    sqlClass.dosql(sql[i])
                    params[i]=doExcel.paramsToken(params[i],token)
                    N_url=doExcel.doUrl(url[i])
                    respones = http.sendHttp(N_url, params[i], header, 1)
                    TOKEN=http.respons(respones,Except[i])#########通过临时变量接受,如果为空的话就用上次请求的token############
                    if(TOKEN==""):
                        token=token
                    else:
                        token=TOKEN
                    i = i + 1
                    print('---------------------------------------------------')
                    print('本次请求结束，等待下个请求........\n\n\n')
                else:
                    params[i]=doExcel.paramsToken(params[i],token)
                    N_url=doExcel.doUrl(url[i])
                    respones = http.sendHttp(N_url, params[i], header, 1)
                    TOKEN=http.respons(respones,Except[i])
                    if(TOKEN==""):
                        token=token
                    else:
                        token=TOKEN
                    i = i + 1
                    print('---------------------------------------------------')
                    print('本次请求结束，等待下个请求........\n\n\n')
            except:
                print('执行出错，测试失败，请检查用例')
                print('预期结果为：' + Except[i] + '')
                print('---------------------------------------------------')
                print('本次请求结束，等待下个请求........\n\n\n')
                i = i + 1
                continue

    def testHttp(caseName, db, sql, url, params, Except):
        sqlClass.ExcuteSql(db,sql)
        caseName = caseName
        Except = Except
        header = {'Content-Type': 'application/json'}
        print('用例名称：' + caseName)
        respone = http.sendHttp(url, params, header, 15)
        print("实际结果为："+respone.text)
        print("预期结果为："+Except)
        return respone























