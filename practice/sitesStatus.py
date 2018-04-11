from selenium import webdriver

def HomePage(sites):
    driver = webdriver.Firefox()
    driver.maximize_window()
   # self.driver = driver
    for k in sites:

    #打开浏览器，进入首页
        driver.get(sites[k][0])
    # 判断是否是首页内容
        try:
            assert sites[k][1] == driver.title
            #assertEquals(sites[k][1],driver.title)
        except AssertionError as e:
            print(u"找不到这个标题")
        #driver.close()

if __name__ == '__main__':
    sites = {'a':['http://test.spb.riskeys.com', '安逸云保-场景化保险专家'],
             'b':[],
             'c':[]
             }
    HomePage(sites)