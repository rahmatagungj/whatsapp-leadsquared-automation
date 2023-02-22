# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

# Config
login_time = 20     # Time for login (in seconds)
new_msg_time = 24    # Time for a new message (in seconds)
send_msg_time = 6   # Time for sending a message (in seconds)
country_code = 62   # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
with open('message.txt', 'r', encoding='utf8') as file:
    msg = file.read()

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    print("Preparing")

    all_content = file.readlines()
    all_content = [x.strip() for x in all_content]

    for count, n in enumerate(all_content):
        with_number = n.find('62')
        if (len(n) == 0) or with_number != 1:
            continue
        num = all_content[count].replace('+62-', '')
        name =  all_content[count - 1]

        print(f'Sending message to {name}(0{num})', end = ' ')
        message_to_send = msg.replace("|name|", name)
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={quote(message_to_send)}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print("-> DONE")
        time.sleep(send_msg_time)

# Quit the driver
print("Task Clear")
driver.quit()


