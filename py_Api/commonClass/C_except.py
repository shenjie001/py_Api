import string
import json


class comperaExcept:
    def compera(relust,myExcept):
        if relust is None or myExcept is None:
            print("结果与预期不一致，测试失败")
            flag=False
            return flag
        if myExcept == '1':
            print("此条用例通过")
            flag=True
            return flag
        else:
         x=str(relust.text)
         y=str(myExcept)
         Trelust=x.replace('{','').replace('}','')####需要把括号去掉，否则字符串匹配会出错###
         TmyExcept=y.replace('{','').replace('}','')
         if Trelust is None or TmyExcept is None or TmyExcept=='':
            print("结果与预期不一致，测试失败")
            flag=False
            return flag
         else:
          if TmyExcept in Trelust:
            print("此条用例通过")
            flag=True
            return flag
          else:
             print("结果与预期不一致，测试失败")
             flag = False
             return flag