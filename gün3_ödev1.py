from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_source:
    
    # username ve password boş geçildiğinde...
    def test_empty_username_and_password(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)

        login_btn.click()
        sleep(1)
        
        error = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        
        error_message = error.text == "Epic sadface: Username is required"
        return f"TEST SONUCU: {error_message}"
        
        
    # password boş geçildiğinde...
    def test_empty_password(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        user_name = driver.find_element(By.ID,"user-name")
        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)
        
        user_name.send_keys("21613213")
        sleep(1)

        login_btn.click()
        sleep(1)
        
        error = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        
        error_message = error.text == "Epic sadface: Password is required"
        return f"TEST SONUCU: {error_message}"
    
    
    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_locked_out(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        user_name = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)
        
        user_name.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(2)
        
        login_btn.click()
        sleep(1)
        
        error = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        
        error_message = error.text == "Epic sadface: Sorry, this user has been locked out."
        return f"TEST SONUCU: {error_message}"
    
    
    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    def test_empty_input_write_x(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)

        login_btn.click()
        sleep(1)
        
        error = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(1)
        
        if error.text != "Epic sadface: Username is required":
            return f"TEST SONUCU: {False}"
        
        x_icon_active = driver.find_elements(By.XPATH, "//div/*[@data-icon='times-circle']")
        sleep(1)

        # eğer çarpı butonlarının sayısı hata sayısı 0 dan farksızsa
        if len(x_icon_active) == 0:
            return f"TEST SONUCU: {False}"
            
        error_exit_btn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(1)
            
        error_exit_btn.click()
        sleep(1)
        
        x_icon_passive = driver.find_elements(By.XPATH, "//div/*[@data-icon='times-circle']")
        sleep(1)
        
        if len(x_icon_passive) == 0:
            return f"TEST SONUCU: {True}"
        else:
            return f"TEST SONUCU: {False}"
    
    
    # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    def test_inventor_html(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        user_name = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)
        
        user_name.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(2)
        
        login_btn.click()
        sleep(2)
        
        new_url = driver.current_url
        
        if new_url == "https://www.saucedemo.com/inventory.html":
            return f"TEST SONUCU: {True}" 
        else:
            return f"TEST SONUCU: {False}"
        
    
    #Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_6_product(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        user_name = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)
        
        user_name.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(2)
        
        login_btn.click()
        sleep(2)
        
        products = driver.find_elements(By.CLASS_NAME,"inventory_item")
        
        if len(products) == 6:
            return f"TEST SONUCU: {True}" 
        else:
            return f"TEST SONUCU: {False}"    
    


test_class = Test_source()

# print(test_class.test_empty_username_and_password())
# print(test_class.test_empty_password())
# print(test_class.test_locked_out())
# print(test_class.test_empty_input_write_x())
# print(test_class.test_inventor_html())
print(test_class.test_6_product())