from discuz.base_discuz import *
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack

class Discuz(BasePage):
    # input_user_loc=(By.NAME,'username')
    # input_mami_loc=(By.NAME,'password')
    input_user_loc=(By.ID,'ls_username')
    input_mami_loc=(By.ID,'ls_password')

    button_login_loc=(By.CSS_SELECTOR,'em')
    morenbankuai_loc=(By.LINK_TEXT,'默认版块')
    click_fatie_loc=(By.ID,"newspecial")
    input_fatie_biaoti_loc=(By.CSS_SELECTOR,'.z input')
    # iframe_loc=(By.ID,'e_iframe')
    input_fatie_zhuti_loc=(By.TAG_NAME,'body')
    button_fatie_loc=(By.ID,'postsubmit')
    huitie=(By.LINK_TEXT,'回复')
    huitiezhuti=(By.ID,'postmessage')
    button_huifu_loc=(By.CSS_SELECTOR,'.fastre')
    button_tuichu_loc=(By.CSS_SELECTOR,'.pipe')

    #2.
    sanchu_loc=(By.CSS_SELECTOR,'.o input')
    button_sanchu_loc=(By.LINK_TEXT,'删除')
    button_sanchu_queding_loc=(By.NAME,'modsubmit')
    glzx=(By.LINK_TEXT,'管理中心')
    mima=(By.NAME,'admin_password')
    tijiao1=(By.NAME,'submit')
    luntan = (By.LINK_TEXT, '论坛')
    tianjiabankuai=(By.LINK_TEXT,'添加新版块')
    tijiao2=(By.NAME,'editsubmit')
    tuichu1=(By.LINK_TEXT,'退出')
    tuichu2= (By.LINK_TEXT,'退出')
    xinmokuai=(By.LINK_TEXT,'新版块名称')

    #3.
    sousuo_loc=(By.ID,'scbar_txt')
    sousuo_click=(By.ID,'scbar_btn')
    click_sousuo=(By.LINK_TEXT,'title')

    #4.
    faqitoupiao=(By.LINK_TEXT,'发起投票')
    input_toupiao=(By.ID,'subject')
    input_toupiao1= (By.XPATH, '//div/p/input[1]')
    input_toupiao2 = (By.XPATH, '//div/p[2]/input[1]')
    toupiao_click=(By.ID,'postsubmit')
    toupiao_click2=(By.ID,'option_1')
    toupiao_tijiao=(By.ID,'pollsubmit')
    toupiao_zhuti=(By.ID,'thread_subject')
    toupiao_zhang=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[1]/td[1]/label')
    toupiao_zhang_bili=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[2]/td[2]')
    toupiao_die=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[3]/td[1]/label')
    toupiao_die_bili=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')

    def login(self,content1,content2):
        self.sendkeys(content1,*self.input_user_loc)
        self.sendkeys(content2,*self.input_mami_loc)
        self.click(*self.button_login_loc)
    def morenbankuai(self):
        # self.driver.switch_to.window(self.driver.window_handles[0])
        self.window()
        self.click(*self.morenbankuai_loc)
    def fatie(self,content1,content2):
        self.click(*self.click_fatie_loc)
        self.sendkeys(content1,*self.input_fatie_biaoti_loc)
        self.iframe('e_iframe')
        # self.iframe()
        self.sendkeys(content2,*self.input_fatie_zhuti_loc)
        self.fanhuiiframe()
        # self.close()
        self.click(*self.button_fatie_loc)
    def huifu(self,a):
        self.click(*self.huitie)
        self.sendkeys(a,*self.huitiezhuti)
        self.click(*self.button_huifu_loc)

    def xuanze(self):
        self.click(*self.sanchu_loc)
        self.click(*self.button_sanchu_loc)
        self.click(*self.button_sanchu_queding_loc)
    def bankuaiguanli(self,mima):
        self.click(*self.glzx)
        self.window_handles(2)
        self.sendkeys(mima,*self.mima)
        self.click(*self.tijiao1)
        self.click(*self.luntan)
        self.iframe('main')
        self.click(*self.tianjiabankuai)
        self.click(*self.tijiao2)
        self.fanhuiiframe()
        self.click(*self.tuichu1)
        self.click(*self.tuichu2)
        self.click(*self.xinmokuai)
    def sousuo(self,a):
        self.sendkeys(a,*self.sousuo_loc)
        self.click(*self.sousuo_click)
        self.window_handles(2)
        self.click(*self.click_sousuo)
        self.window_handles(3)
    # def yanzheng(self):
    #     assert 'title' in
    def toupiao(self,a,b,c):
        self.click(*self.click_fatie_loc)
        self.click(*self.faqitoupiao)
        self.sendkeys(a,*self.input_toupiao)
        self.sendkeys(b, *self.input_toupiao1)
        self.sendkeys(c, *self.input_toupiao2)
        self.click(*self.toupiao_click)
    def toupiao2(self):
        self.click(*self.toupiao_click2)
        self.click(*self.toupiao_tijiao)
        print('投票主题：%s'%self.get_text(*self.toupiao_zhuti))
        print(self.get_text(*self.toupiao_zhang),'比例：',self.get_text(*self.toupiao_zhang_bili))
        print(self.get_text(*self.toupiao_die), '比例：', self.get_text(*self.toupiao_die_bili))


    def tuichu(self):
        self.click(*self.button_tuichu_loc)

