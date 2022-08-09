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
firstname = ["Sky",
"Raymond",
"Minwoo",
"Sean",
"Ethan",
"James",
"Jinho",
"Evan",
"Muhammad",
"Raphael",
"Jeffrey ",
"Royce",
"Lara",
"Dione",
"emily",
"Yuji",
"Janghyun",
"Ethan",
"Michael",
"Moses",
"Alex",
"Seojoon",
"Matthew",
"Seungmi",
"Jason",
"Young",
"Isaac",
"Amy",
"Andrew",]
lastname = ["Jeong",
"Kim",
"Kwon ",
"Kim",
"Hong",
"Lee",
"Won",
"Koh",
"Muhammad",
"Koo",
"Sun ",
"Lee",
"Mayda",
"Kim",
"kim",
"Fukuda",
"Lee",
"An",
"Shin",
"Yoon",
"Choi",
"Kwon",
"Lim",
"Hong",
"Lee",
"Kim",
"Kwon",
"Park",
"Kim",]
grade = ["12",
"10",
"12",
"12",
"12",
"12",
"11",
"10",
"12",
"11",
"11",
"12",
"12",
"11",
"11",
"12",
"12",
"9",
"12",
"12",
"12",
"12",
"12",
"12",
"10",
"12",
"12",
"11",
"9"]
idstring = ["sjeong23",
"rkim25",
"mkwon23",
"swkim23",
"eyhong23",
"jslee23",
"jwon24",
"hskoh25",
"mkhalil23",
"rkoo24",
"jsun24",
"rjlee23",
"lmayda23 ",
"dionekim24",
"egkim24",
"yfukuda23",
"jhlee23",
"ean26",
"dshin23",
"pyoon23",
"achoi23",
"skwon23",
"slim23",
"ehong23",
"jklee25",
"ykim23",
"jkwon23",
"jepark24",
"akim26"]
email = [
"sjeong23@student.kis.or.kr",
"rkim25@student.kis.or.kr",
"mkwon23@student.kis.or.kr",
"swkim23@student.kis.or.kr",
"eyhong23@student.kis.or.kr",
"jameslee4128@gmail.com",
"jwon24@student.kis.or.kr",
"hskoh25@student.kis.or.kr",
"mkhalil23@student.kis.or.kr",
"rkoo24@student.kis.or.kr",
"jsun24@student.kis.or.kr",
"rjlee23@student.kis.or.kr",
"lmayda23@student.kis.or.kr",
"dionekim24@student.kis.or.kr",
"egkim24@student.kis.or.kr",
"yfukuda23@student.kis.or.kr",
"jhlee23@student.kis.or.kr",
"ean26@student.kis.or.kr",
"dshin23@student.kis.or.kr",
"pyoon23@student.kis.or.kr",
"achoi23@student.kis.or.kr",
"skwon23@student.kis.or.kr",
"slim23@student.kis.or.kr",
"ehong23@student.kis.or.kr",
"jklee25@student.kis.or.kr",
"ykim23@student.kis.or.kr",
"jkwon23@student.kis.or.kr",
"jepark24@student.kis.or.kr",
"akim26@student.kis.or.kr"]
web = webdriver.Chrome(service = s, options = options)

for i in range(len(firstname)):
    web.get('https://form.jotform.com/201630197748459')
    time.sleep(1)
    print(web.title)
    first = web.find_element("xpath", '//*[@id="first_9"]')
    first.send_keys(firstname[i])
    last = web.find_element("xpath", '//*[@id="last_9"]')
    last.send_keys(lastname[i])
    student = web.find_element("xpath", '//*[@id="label_input_10_0"]')
    student.click()
    findgrade = web.find_element("id",'input_16')
    selectgrade = Select(findgrade)
    if(grade[i] == "9"):
        selectgrade.select_by_value("9")
    
    if(grade[i] == "10"):
        selectgrade.select_by_value("10")
    
    if(grade[i] == "11"):
        selectgrade.select_by_value("11")
    
    if(grade[i] == "12"):
        selectgrade.select_by_value("12")
    id = web.find_element("xpath", '//*[@id="input_17"]')
    id.send_keys(idstring[i])
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
    msg['To'] = email[i]

    with open('Screenshot.png', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype = 'file_type',filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('bot19992003@gmail.com', 'swxtuvzadjwudfdz')
        smtp.send_message(msg)
    print(firstname[i] + " Done")

