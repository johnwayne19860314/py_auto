elements = {
    'YunBao':{
        'homePage':"http://test.spb.riskeys.com",
        'MeiXing': {
            'test_Login':{
                'ele':['xpath',"//div[@class='right nav-box clearfix']/a[@data-toggle='modal']"],
                'account':['mxtest','123456'],
                'button':'channel-login-btn',
                'userId':['id','span-userName'],
            },
            'test_Addaccount': {
                'ele': ['xpath', ".//*[@id='sidebar']/ul/li[@data-href='user.html']"],
                #'account': ['mxtest', '123456'],
                'ele_validtor': ['xpath', ".//*[@id='dynamic-table']/tbody/tr"],
                #'userId': ['id', 'span-userName'],
            },
            'test_Policycreate': {
                'ele': {"form-product":3,"form-package":0, "form-address":2,"form-insure-day":7},
                # 'account': ['mxtest', '123456'],
                'ele_orderNo': ['id', "form-teamId",'ERMED1234'],
                'time_tuple': ['xpath', (".//*[@id='form-product-info']//div[@class='col-xs-4 time-group'][1]//span[@class='input-group-addon']",
                    "//th[@class='next']",
                    "//tr[1]/td[@class='day'][1]")],
                'link_check': ['id',('.//*[@id="link-tips"]',
                      './/*[@id="yb_ddhly_tips"]//button[@class="close"]',
                      './/*[@id="link-detail"]',
                      './/*[@id="modal-form-detail"]//button[@class="close" and @type="button"]')],
                'order_btn':['id','btn-order'],
                'ele_validator':['xpath',".//*[@id='profile-user-info']//span[@data-field='count']"],
                'eleList_val':["xpath",".//*[@id='table-userlist']/tbody/tr"],
                'order_val':['id','form-btn-order'],
                'order_print':["xpath",".//*[@id='anyi-modal-alert']//div[@class='modal-body']"],
                'policy_ele':["xpath",".//*[@id='anyi-modal-alert']//div[@class='modal-footer']/a"]
            },
            'addperson': {
                'ele': ['id', "btn-import"],
                'ele_1': ['id', "form-field-attach1"],
                'popClose': ['xpath', ".//*[@id='modal-form-upload']//div[@class='modal-content']//button[@class='btn btn-sm']"],
                # 'userId': ['id', 'span-userName'],
            },

        }
    }

}