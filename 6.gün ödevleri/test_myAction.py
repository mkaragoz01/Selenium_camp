from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from constants.globalConstants import *


class Test_source:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(URL)
  
    def teardown_method(self, method):
        self.driver.quit()
        
    #ürünleri sıralama seçenekleri doğru çalışıyor mu?
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_product_short_contanier(self,username,pw):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,user_id))
        self.waitForElementVisible((By.ID,password_id))
        self.waitForElementVisible((By.ID,login_id))
        
        user_name = self.driver.find_element(By.ID,user_id)
        password = self.driver.find_element(By.ID,password_id)
        login_btn = self.driver.find_element(By.ID,login_id)
        
        user_name.send_keys(username)
        password.send_keys(pw)
        
        login_btn.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select"))
        
        contanier = self.driver.find_elements(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select")
        
        for i in range(1,len(contanier)+1):
            container_option = self.driver.find_element(By.XPATH,f"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[{i}]")
            container_option.click()
            
            first = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
            assert first.text==first_product[i-1]
            
    #sepette bulunan continue shopping butonu doğru çalışıyor mu?
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_continue_shopping(self,username,pw):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,user_id))
        self.waitForElementVisible((By.ID,password_id))
        self.waitForElementVisible((By.ID,login_id))
        
        user_name = self.driver.find_element(By.ID,user_id)
        password = self.driver.find_element(By.ID,password_id)
        login_btn = self.driver.find_element(By.ID,login_id)
        
        user_name.send_keys(username)
        password.send_keys(pw)
        
        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"))
        
        basket_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        basket_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/button[1]"))
        continue_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/button[1]")
        continue_btn.click()
        
        self.waitForElementVisible((By.CLASS_NAME,"app_logo"))
        new_url = self.driver.current_url
        
        assert new_url==inventor_URL            

    #ürünleri satın alma kısmında istenen tüm bilgileri boş bırakırsak almak istediğimiz hata...
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_pay_info_null_all(self,username,pw):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,user_id))
        self.waitForElementVisible((By.ID,password_id))
        self.waitForElementVisible((By.ID,login_id))
        
        user_name = self.driver.find_element(By.ID,user_id)
        password = self.driver.find_element(By.ID,password_id)
        login_btn = self.driver.find_element(By.ID,login_id)
        
        user_name.send_keys(username)
        password.send_keys(pw)
        
        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"))
        add_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add_btn.click()
        
        basket_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        basket_btn.click()
        
        checkout_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/button[2]")
        checkout_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input"))
        continue_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input")
        continue_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3"))
        error = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        error_txt = error.text
        
        assert error_txt==pay_null_fname_error
    
    #ürünleri satın alma kısmında istenen firstname hariç tüm bilgileri eksik bırakınca almak istediğimiz hata...
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_pay_info_null_lastname(self,username,pw):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,user_id))
        self.waitForElementVisible((By.ID,password_id))
        self.waitForElementVisible((By.ID,login_id))
        
        user_name = self.driver.find_element(By.ID,user_id)
        password = self.driver.find_element(By.ID,password_id)
        login_btn = self.driver.find_element(By.ID,login_id)
        
        user_name.send_keys(username)
        password.send_keys(pw)
        
        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"))
        add_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add_btn.click()
        
        basket_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        basket_btn.click()
        
        checkout_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/button[2]")
        checkout_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input"))
        fname_input = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
        fname_input.send_keys("1")
        
        continue_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input")
        continue_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3"))
        error = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3")
        error_txt = error.text
        
        assert error_txt==pay_null_lname_error
        
    #ürünleri satın alma kısmında istenen postal code eksik bırakınca almak istediğimiz hata...
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_pay_info_null_postalcode(self,username,pw):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,user_id))
        self.waitForElementVisible((By.ID,password_id))
        self.waitForElementVisible((By.ID,login_id))
        
        user_name = self.driver.find_element(By.ID,user_id)
        password = self.driver.find_element(By.ID,password_id)
        login_btn = self.driver.find_element(By.ID,login_id)
        
        user_name.send_keys(username)
        password.send_keys(pw)
        
        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"))
        add_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add_btn.click()
        
        basket_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        basket_btn.click()
        
        checkout_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/button[2]")
        checkout_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input"))
        fname_input = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
        fname_input.send_keys("1")
        
        lname_input = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
        lname_input.send_keys("1")
        
        continue_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input")
        continue_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3"))
        error = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3")
        error_txt = error.text
        
        assert error_txt==pay_null_postalCode_error
        
        
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator)) 
