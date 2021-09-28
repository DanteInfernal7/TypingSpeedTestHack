from selenium import webdriver
import pyautogui
driver=webdriver.Chrome('C:\\Users\\hwala\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.livechat.com/typing-speed-test/#/')

select = pyautogui.locateCenterOnScreen("image\\move.png")
pyautogui.moveTo(select)
pyautogui.click()
while True:
    for elem1 in driver.find_elements_by_xpath('.//span[@class = "u-pl-0 u-pr-2xs"]'):
            pyautogui.write(elem1.text)
            pyautogui.keyDown("Space")