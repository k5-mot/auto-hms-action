import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep
import datetime

def main(argv = sys.argv):
    # USERNAME
    username = argv[1]
    # PASSWORD
    password = argv[2]

    # Selemium を起動する
    print('Run Selenium')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.implicitly_wait(10)

    # ログインフォームへ移動
    url = "https://hms.hc.nagasaki-u.ac.jp/menulogin.php"
    driver.get(url)

    # ログインフォームに入力
    print('Enter into Login form')
    elem_username = driver.find_element(By.NAME, 'UID')
    elem_username.send_keys(username)
    elem_password = driver.find_element(By.NAME, 'PW')
    elem_password.send_keys(password)

    # ログインフォームの Login ボタンを押下
    elem_loginbtn = driver.find_element(By.XPATH, '//div[@class="box_login_btn"]/button')
    elem_loginbtn.click()
    sleep(5)

    # メニュー画面の「過去報告確認」をクリック
    print('Select menu')
    elem_menubtn = driver.find_elements(By.XPATH, '//div[@class="outbox_menu"]/div[@class="box_btn_style5"]/button')
    elem_menubtn[1].click()
    sleep(5)

    # 最新日の「備考」を表示
    jst_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    elem_infocel = driver.find_element(By.XPATH, '//table[@class="tbl_hcHistory"]/tbody/tr[' + str(jst_time.day + 1) + ']/td[@class="note"]/span[@id="note"]')
    print('Latest Check: ' + elem_infocel.text)

    # 最新日の行をスクリーンショット
    elem_infotab = driver.find_element(By.XPATH, '//table[@class="tbl_hcHistory"]/tbody/tr[' + str(jst_time.day + 1) + ']')
    info_image = driver.elem_infotab.screenshot_as_png
    with open("./screenshot.png", "wb") as f:
        f.write(png)
    sleep(5)

    # 終了
    driver.close()


if __name__ == '__main__':
    main(sys.argv)

