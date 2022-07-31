from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import smtplib
import imghdr
from email.message import EmailMessage
from selenium.webdriver.chrome.service import Service

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=750,600")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
s=Service('/usr/local/bin/chromedriver')
web = webdriver.Chrome(service = s, options = options)
web.get('https://form.jotform.com/201630197748459')
time.sleep(1)
print(web.title)
firstname = "1"
lastname = "3"
idstring = "1"
first = web.find_element("xpath", '//*[@id="first_9"]')
first.send_keys(firstname)
last = web.find_element("xpath", '//*[@id="last_9"]')
last.send_keys(lastname)
student = web.find_element("xpath", '//*[@id="label_input_10_0"]')
student.click()
findgrade = web.find_element("id",'input_16')
selectgrade = Select(findgrade)
selectgrade.select_by_value("11")
id = web.find_element("xpath", '//*[@id="input_17"]')
id.send_keys(idstring)
next = web.find_element("xpath", '//*[@id="form-pagebreak-next_31"]')
next.click()
opt1 = web.find_element("id", 'label_input_32_1')
opt2 = web.find_element("id", 'label_input_34_1')
opt3 = web.find_element("id", 'label_input_46_1')
opt4 = web.find_element("id", 'label_input_35_1')
opt5 = web.find_element("id", 'label_input_36_1')
time.sleep(0.5)
opt1.click()
opt2.click()
opt3.click()
opt4.click()
opt5.click()
submit = web.find_element("xpath", '//*[@id="input_2"]')
submit.click()
time.sleep(1)
web.get_screenshot_as_file("Screenshot.png")
msg = EmailMessage()
msg['Subject'] = 'Green Pass'
msg['From'] = 'bot19992003@gmail.com'
msg['To'] = 'focalxp7@gmail.com'

with open('Screenshot.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype = 'file_type',filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login('bot19992003@gmail.com', 'swxtuvzadjwudfdz')
    smtp.send_message(msg)
