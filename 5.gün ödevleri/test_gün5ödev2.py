from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from constants.globalConstants import *
from pathlib import Path
from datetime import date

class Test_source:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(URL)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
  
    def teardown_method(self, method):
        self.driver.quit()
    # username ve password boş geçildiğinde...
        
    def test_empty_username_and_password(self):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,login_id))
        
        login_btn = self.driver.find_element(By.ID,login_id)
        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        error_message = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")  
        
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-username-and-password.png")      
        assert error_message.text == error_empty_info
       
    # password boş geçildiğinde...
    @pytest.mark.parametrize("username",(["1"],["2"]))
    def test_empty_password(self,username):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,login_id))
        self.waitForElementVisible((By.ID,user_id))

        user_name = self.driver.find_element(By.ID,user_id)
        login_btn = self.driver.find_element(By.ID,login_id)
        
        user_name.send_keys(username)
        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        error = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password.png")
        assert error.text == error_empty_pw
    
    
    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    @pytest.mark.parametrize("username,pw",[("locked_out_user","secret_sauce")])
    def test_locked_out(self,username,pw):
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
        
        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        error = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out.png")
        assert error.text == error_locked_out

    
    
    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    def test_empty_input_write_x(self):
        self.driver.get(URL)
        self.waitForElementVisible((By.ID,login_id))
        login_btn = self.driver.find_element(By.ID,login_id)

        login_btn.click()
        
        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        error = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        
        self.waitForElementVisible((By.XPATH,"//div/*[@data-icon='times-circle']"))
        x_icon_active = self.driver.find_elements(By.XPATH, "//div/*[@data-icon='times-circle']")

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button"))
        error_exit_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
            
        error_exit_btn.click()
        
        x_icon_passive = self.driver.find_elements(By.XPATH, "//div/*[@data-icon='times-circle']")
        
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-input-write-x.png")
        assert len(x_icon_passive) == 0
    
    
    
    # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_inventor_html(self,username,pw):
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
        
        self.waitForElementVisible((By.CLASS_NAME,"app_logo"))
        new_url = self.driver.current_url
        
        self.driver.save_screenshot(f"{self.folderPath}/test-inventor-html.png")
        assert new_url == inventor_URL
        
    
    #Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_6_product(self,username,pw):
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
        
        self.waitForElementVisible((By.CLASS_NAME,"app_logo"))
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        
        self.driver.save_screenshot(f"{self.folderPath}/test-6-product.png")
        assert len(products) == 6
    
    # Ürünlerin isimlerinin doğruluğu
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_product_name(self,username,pw):
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
        
        self.waitForElementVisible((By.CLASS_NAME,"app_logo"))
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        control = True
        for i in range(len(products)):
            if products[i].text != products_name[i]:
                control = False
                break
        
        self.driver.save_screenshot(f"{self.folderPath}/test-product-name.png")
        assert control
        
    # add to card butonuna tıklayınca butonun remove dönüşme durumu
    @pytest.mark.parametrize("username,pw",[("standard_user","secret_sauce")])
    def test_write_add_remove(self,username,pw):
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
        
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        add_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add_text = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").text
        add_btn.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"))
        remove_text = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").text
        
        self.driver.save_screenshot(f"{self.folderPath}/test-write-add-remove.png")
        assert add_text == add and remove_text == remove
        
    # ürünü sepete ekleme durumu
    @pytest.mark.parametrize("username,pw,basket_list",[("standard_user","secret_sauce",products_name[:3])])
    def test_add_basket(self,username,pw,basket_list):
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
        
        self.waitForElementVisible((By.CLASS_NAME, "inventory_item"))
        add1_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add1_btn.click()
        
        add2_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        add2_btn.click()
        
        add3_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        add3_btn.click()
        
        basket_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]")
        basket_btn.click()
        
        self.waitForElementVisible((By.CLASS_NAME, "cart_item"))
        products_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        
        control = True
        for i in range(len(products_list)):
            if products_list[i].text != basket_list[i]:
                control = False
                break
                
        self.driver.save_screenshot(f"{self.folderPath}/test-add-basket.png")
        assert control
    
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator)) 
