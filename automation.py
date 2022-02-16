# original code from https://qiita.com/ftoyoda/items/fe3e2fe9e962e01ac421
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
    # elem_loginbtn = driver.find_element(By.CLASS_NAME, 'btn_style1')
    elem_loginbtn.click()
    sleep(5)

    # メニュー画面の「健康管理情報入力」をクリック
    print('Select menu')
    elem_menubtn = driver.find_element(By.CLASS_NAME, 'btn_style3')
    elem_menubtn.click()
    sleep(5)

    # 備考に時間を追記
    jst_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    elem_note = driver.find_element(By.ID, 'note')
    elem_note.clear()
    elem_note.send_keys(jst_time.strftime('%Y/%m/%d(%a) %H:%M:%S JST'))
    sleep(5)

    # 「健康管理情報 入力」画面の「登録」をクリック
    print('Register health info')
    elem_regbtn = driver.find_element(By.CLASS_NAME, 'btn_style1')
    elem_regbtn.click()

    # 「更新を行いますがよろしいですか?」ポップアップの「OK」を押下
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    Alert(driver).accept()
    sleep(5)

    # 「登録しました!」ポップアップの「OK」を押下
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    Alert(driver).accept()
    sleep(5)

    # 画面が遷移したかチェック
    print('Updated: ', end='')
    elem_regbtn = driver.find_element(By.CLASS_NAME, 'btn_style1')
    if elem_regbtn.text == "登録（Register）":
        print('Success')
    else:
        print('Failure')
        sys.exit(-1)


if __name__ == '__main__':
    main(sys.argv)
