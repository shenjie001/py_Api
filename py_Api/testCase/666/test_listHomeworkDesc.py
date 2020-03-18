from commonClass.readExcel import doExcel
from commonClass.readConfig import readConfig
from commonClass.Http import http
##################################直接运行这个文件就可以了#######################################################


print('***********************接口测试结束***********************\n\n\n')
x=doExcel.readExcel('666', 'listHomeworkDesc')
http.HttpTest(x)
print('***********************接口测试结束***********************\n')