import os

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)


class creatTest():

    def mkdir(testFileName,pyName):
        path=parent_path+'\\'+'testCase'+'\\'+testFileName
        folder = os.path.exists(path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("------  正在创建新文件...  ------")
            print("------  目录创建成功  ------")

        else:
            print("---  文件夹已存在!  ---")


        print('**************神奇的分割线************************')


        pyPATH=path+'\\'+"test_"+pyName+".py"
        folder1=os.path.exists(pyPATH)
        if not folder1:
          f=open(pyPATH,"w")
          f.close()
          print("-------   正在创建py文件  -------")
          print("-------   py文件创建成功  -------")
        else:
            print("----  文件已存在  -----")

        fd=open(pyPATH,'w',encoding='utf-8')
        header='from commonClass.readExcel import doExcel\nfrom commonClass.readConfig import readConfig\nfrom commonClass.Http import http\n'
        fd.write(header)
        url="##################################直接运行这个文件就可以了#######################################################\n\n\nprint('***********************接口测试结束***********************\\n\\n\\n')\nx=doExcel.readExcel('"+testFileName+"', '"+pyName+"')\n"
        fd.write(url)
        str="http.HttpTest(x)\nprint('***********************接口测试结束***********************\\n')"
        fd.write(str)
        fd.close()


if __name__ == '__main__':
    creatTest.mkdir('666','listHomeworkDesc')



