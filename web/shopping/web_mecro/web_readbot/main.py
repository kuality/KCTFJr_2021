from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
options.add_argument('window-size=900x1080')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
options.add_argument("lang=ko_KR")

# 실제브라우져와 동일하게 작동하는 세션루틴실행
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 지정경로에 세션정보를 디스크에 저장하고 실행시마다 재사용함
options.add_argument('--user-data-dir=' + '/home/kctf/')


URL = 'http://ctf.kuality.kr:12310'
#URL = 'http://192.168.0.3:9000'
driver = webdriver.Chrome(options=options, executable_path="/home/kctf/chromedriver")

def read_article():
    board_id = 1
    while True:  # 특정 시간동안 반복해서 게시글 읽기
        driver.get(URL + "/board/article/" + str(board_id) + "/")  # 게시글 페이지로 이동
        try:
            board_alert = Alert(driver)
            board_alert.accept()
        except:
            pass
        if "404 Not Found" in driver.title:  # 만약 게시글이 없을 때 동작
            print("no more article!")
            sleep(5)

        elif "KCTFjr Shopping" in driver.title:  # 회원가입에 성공해서 main 페이지로 redirect 됐을 때
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Somebody Success The Attack!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            board_id += 1
            sleep(5)
        elif "KCTFjr" in driver.title:  # 아이디 또는 이메일 중복이나 db 에러로 rollback() 됐을 때
            print("---------article : " + str(board_id) + "-----------")
            print("중복 아이디 또는 이메일로 공격이 시도되어 내용은 필터링 되었습니다.")
            print("--------------END--------------")
            board_id += 1
            sleep(5)
        else:  # 게시글이 존재할 때 동작
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            print("---------article : " + str(board_id) + "-----------")
            print(soup.h1)
            print(soup.div)
            print("--------------END--------------")
            board_id += 1
            sleep(5)

driver.implicitly_wait(3)
driver.get(URL)

driver.find_element_by_id('userid').send_keys('5up3rU53r')  # 슈퍼 계정 로그인
driver.find_element_by_id('password').send_keys('Bruta@@5205')
driver.find_element_by_xpath("//button[@type='submit']").click()

login_alert = Alert(driver)  # alert 값 받기
if "존재하지 않는 아이디입니다!" == login_alert.text:  # 슈퍼계정이 존재하지 않을 때
    login_alert.accept()
    driver.get(URL+"/register")
    driver.find_element_by_id('userid').send_keys('5up3rU53r')  # 슈퍼 계정 회원가입
    driver.find_element_by_id('email').send_keys('5up3rU53r@@hacker.kr')
    driver.find_element_by_id('password').send_keys('Bruta@@5205')
    driver.find_element_by_id('repassword').send_keys('Bruta@@5205')
    driver.find_element_by_xpath("//button[@type='submit']").click()
    print("슈퍼계정 가입 성공!!")
    register_alert = Alert(driver)
    register_alert.accept()
    sleep(3)
    driver.get(URL)
    driver.find_element_by_id('userid').send_keys('5up3rU53r')  # 슈퍼 계정 로그인
    driver.find_element_by_id('password').send_keys('Bruta@@5205')
    driver.find_element_by_xpath("//button[@type='submit']").click()
    a_login_alert = Alert(driver)  # 환영 alert 처리
    a_login_alert.accept()
    print("슈퍼계정으로 로그인했습니다")
    read_article()
elif "5up3rU53r님 환영합니다!" == login_alert.text:  # 슈퍼계정이 존재할 시
    print("슈퍼계정으로 로그인했습니다")
    login_alert.accept()
    read_article()



