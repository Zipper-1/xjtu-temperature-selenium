netid = "" #NetID
password = "" #密码
temperature = "36.0" #体温

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('http://jkrb.xjtu.edu.cn/EIP/user/index.htm')
driver.maximize_window()
if driver.current_url == "http://org.xjtu.edu.cn/openplatform/login.html":
  driver.implicitly_wait(10)
  driver.find_element_by_name("username").send_keys(netid)
  driver.implicitly_wait(10)
  driver.find_element_by_name("pwd").send_keys(password)
  driver.implicitly_wait(10)
  driver.find_element_by_id("account_login").click()

element = WebDriverWait(driver, 10, 0.5).until(EC.url_contains("jkrb.xjtu.edu.cn"))
driver.get('http://jkrb.xjtu.edu.cn/EIP/weixin/weui/home.html')
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[text()='本科生每日健康状况填报']")))
driver.find_element_by_xpath("//p[text()='本科生每日健康状况填报']").click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[text()='每日健康填报']")))
driver.find_elements_by_xpath("//h3[text()='每日健康填报']/following-sibling::a[1]")[0].click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请准确填写体温，格式如:36.5']")))
driver.find_elements_by_xpath("//p[text()='绿色']/../..")[0].click()
driver.find_elements_by_xpath("//input[@placeholder='请准确填写体温，格式如:36.5']")[0].send_keys(temperature)
driver.find_elements_by_xpath("//a[text()='下一步(流程)']")[0].click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请准确填写体温，格式如:36.5']")))
driver.find_elements_by_xpath("//a[text()='提交']")[0].click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='确定']")))
driver.find_elements_by_xpath("//a[text()='确定']")[0].click()
driver.quit()
