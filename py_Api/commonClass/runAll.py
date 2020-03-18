import unittest
import parameterized
from py_Api.commonClass.readExcel import doExcel
from py_Api.commonClass.Http import http

data = doExcel.getData('666', 'listHomeworkDesc')

class MyTest(unittest.TestCase):

  def setUp(self):
      print('***********************本次接口测试开始***********************')

  @parameterized.parameterized.expand(data)
  def test1(self, caseName, db,sql, url, params, Except):
        res=http.testHttp( caseName, db,sql, url, params, Except)
        if  Except=="1":
            self.assertEquals(1,1)
            print("预期与结果相同，测试通过！")
        else:
            self.assertIn(Except,res.text,msg="预期与结果不一致，测试失败！")
  def tearDown(self):
      print('***********************本次接口测试结束***********************\n\n\n')

if __name__ == '__main__':
    unittest.main()

