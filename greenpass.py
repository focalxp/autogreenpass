from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import smtplib
import imghdr
import numpy as np
from sklearn import utils
from email.message import EmailMessage
from selenium.webdriver.chrome.service import Service
from earlyvariables import earlyfirstname, earlylastname, earlygrade, earlyidstring, earlyemail
from latevariables import latefirstname, latelastname, lategrade, lateidstring, lateemail

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.87 Safari/537.36"
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

firstname  = np.concatenate((earlyfirstname, latefirstname))
lastname = np.concatenate((earlylastname, latelastname))
idstring = np.concatenate((earlyidstring, lateidstring))
grade = np.concatenate((earlygrade, lategrade))
email = np.concatenate((earlyemail, lateemail))



web = webdriver.Chrome(service = s, options = options)

for i in range(len(firstname)):
    web.get('https://form.jotform.com/201630197748459')
    time.sleep(1)
    #print(web.title)
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
    opt4 = web.find_element("id", 'label_input_36_1')
    time.sleep(0.5)
    opt1.click()
    opt2.click()
    opt3.click()
    opt4.click()
    submit = web.find_element("xpath", '//*[@id="input_2"]')
    submit.click()
    time.sleep(1)
    web.get_screenshot_as_file("Screenshot.png")
    # payment = EmailMessage()
    # payment['Subject'] = 'GREENPASS PAYMENT!'
    # payment['From'] = 'bot19992003@gmail.com'
    # payment['To'] = email[i]
    # payment.set_content('Greenpass payment required by the end of the week. If youve already paid or are exempted from payment its taken care of, but if you havent, please bring cash. I have change for 10,000 won bills. Contact edward__kang on Instagram for help or 010-6307-7705 .  (Failure of payment will result in termination of your service)')
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
        #smtp.send_message(payment)
    print("%s %d/%d" %(firstname[i], i + 1, len(firstname)))

#test length of arrays
# print(len(firstname))
# print(len(lastname))
# print(len(idstring))
# print(len(grade))
# print(len(email))

#test order of arrays
# for i in range (len(firstname)):
#     print(firstname[i] + " " + lastname[i] + " " + grade[i] + " " + idstring[i] + " " + email[i])


