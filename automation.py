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
    print('Move Login form: ', end='')
    url = "https://hms.hc.nagasaki-u.ac.jp/menulogin.php"
    driver.get(url)
    title = driver.find_element(By.CLASS_NAME, 'box_cont_title')
    #print(title.text)
    if title.text == "ログイン（Login）":
        print('OK')
    else:
        print('Failed')
        sys.exit()

    # ログインフォームに入力
    print('Enter into Login form')
    elem_username = driver.find_element(By.NAME, 'UID')
    elem_username.send_keys(username)
    elem_password = driver.find_element(By.NAME, 'PW')
    elem_password.send_keys(password)

    # ログインフォームの Login ボタンを押下
    print('Press Login button: ', end='')
    elem_sendbtn = driver.find_element(By.CLASS_NAME, 'btn_style1')
    #print(elem_sendbtn.text)
    if elem_sendbtn.text == "Login":
        print('OK')
    else:
        print('Failed')
        sys.exit()
    elem_sendbtn.click()
    sleep(5)

    # メニュー画面の「健康管理情報入力」をクリック
    print('Select menu: ', end='')
    elem_inbtn = driver.find_element(By.CLASS_NAME, 'btn_style3')
    #print(elem_inbtn.text)
    if elem_inbtn.text == "健康管理情報 入力（Register health data）":
        print('OK')
    else:
        print('Failed')
        sys.exit()
    elem_inbtn.click()
    sleep(5)

    # 備考に時間を追記
    jst_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    elem_note = driver.find_element(By.ID, 'note')
    elem_note.clear()
    elem_note.send_keys(jst_time.strftime('%Y/%m/%d(%a) %H:%M:%S JST'))
    sleep(5)

    # 「健康管理情報 入力」画面の「登録」をクリック
    print('Register health info: ', end='')
    elem_regbtn = driver.find_element(By.CLASS_NAME, 'btn_style1')
    # print(elem_regbtn.text)
    if elem_regbtn.text == "登録（Register）":
        print('OK')
    else:
        print('Failed')
        sys.exit()
    elem_regbtn.click()

    # ポップアップウィンドウ1のOKをクリック
    print('Avoid popup1')
    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.alert_is_present())   # Javascriptのアラートがでてくるまで待つ
        Alert(driver).accept()         # アラート受け入れる(OKを押す)
        sleep(5)       # 1秒まつ
    except Exception as e:
        print("アラートの処理でエラー")

    # ポップアップウィンドウ2のOKをクリック
    print('Avoid popup2')
    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.alert_is_present())   # Javascriptのアラートがでてくるまで待つ
        Alert(driver).accept()         # アラート受け入れる(OKを押す)
        sleep(5)       # 1秒まつ
    except Exception as e:
        print("アラートの処理でエラー")

    # 画面が遷移したかチェック
    print('Last check: ', end='')
    elem_outbtn = driver.find_element(By.CLASS_NAME, 'btn_style1')
    #print(elem_outbtn.text)
    if elem_outbtn.text == "登録（Register）":
        print('OK')
    else:
        print('Failed')
        sys.exit()
    #elem_outbtn[0].click()

if __name__ == '__main__':
    main(sys.argv)
