from calendar import calendar
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError
from bs4 import BeautifulSoup
import time
from datetime import datetime
import schedule
import requests

# Line Notify Token: QGuub3Vwntxa0RJbnzRlldcRGbaskNT85sS24V2bN4O


 
def login(account, password, page):
    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Click .wk-menu-btn >> nth=0
    page.locator(".wk-menu-btn").first.click()

    # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder="手機"]
    page.locator(
        "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").click()
    page.locator("text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").fill(
        account)

    # page.fill('div[class="desktop-header hidden-sm hidden-xs"]{span[id="user_id"]}', "0970230723")

    # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type="password"]
    page.locator(
        "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type=\"password\"]").click()
    page.locator(
        "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type=\"password\"]").fill(password)

    # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> button[name="form-login"]
    # page.once("dialog", lambda dialog: dialog.dismiss())
    page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: print(dialog.message))
    page.locator(
        "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> button[name=\"form-login\"]").click()
    # page.on("dialog", lambda dialog: dialog.accept())
    # page.on("dialog", lambda dialog: print(dialog.message))
    # page.click("OK")
    # ---------------------------------------------------------------------------------------------------------------------------------------

def on_response(response):
    global seat
    if '/orderAPI/otGetPossible' in response.url and response.status == 200:
        res = response.json()["res2"]
        index1 = res[0]
        content = index1["content"]
        index2 = content[0]
        data = index2["data"]
        seat = data["seat"]
        print("座位:", seat, datetime.now())


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    page.on('response', on_response)

    # Go to https://www.feastogether.com.tw/booking/2
    page.goto("https://www.feastogether.com.tw/booking/2")
    try:
        page.wait_for_load_state('networkidle')
        # time.sleep(2)

        # Click #modal-news >> text=我知道了
        page.locator("#modal-news >> text=我知道了").click()

        # ---------------------------------------------------------------------------------------------------------------------------------------
        # # Click .wk-menu-btn >> nth=0
        # page.locator(".wk-menu-btn").first.click()

        # # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder="手機"]
        # page.locator(
        #     "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").click()
        # page.locator("text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").fill(
        #     "0970230723")

        # # page.fill('div[class="desktop-header hidden-sm hidden-xs"]{span[id="user_id"]}', "0970230723")

        # # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type="password"]
        # page.locator(
        #     "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type=\"password\"]").click()
        # page.locator(
        #     "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type=\"password\"]").fill("pkrve27m")
        # time.sleep(2)

        # # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> button[name="form-login"]
        # # page.once("dialog", lambda dialog: dialog.dismiss())
        # page.on("dialog", lambda dialog: dialog.accept())
        # page.on("dialog", lambda dialog: print(dialog.message))
        # page.locator(
        #     "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> button[name=\"form-login\"]").click()
        # # page.on("dialog", lambda dialog: dialog.accept())
        # # page.on("dialog", lambda dialog: print(dialog.message))
        # # page.click("OK")
        # ---------------------------------------------------------------------------------------------------------------------------------------

        # Click input[type="number"]
        page.locator("input[type=\"number\"]").click()

        # Fill input[type="number"]
        page.locator("input[type=\"number\"]").fill("2")
        # Click [placeholder="隔日起 \~ 一個月內"]
        page.locator("[placeholder=\"隔日起 \\~ 一個月內\"]").click()

        # Click [aria-label="五月 03\, 2022"]
        page.locator(dataInfo).click()

        # Click text=晚餐
        page.locator(mealTime).first.click()

        # Click #select_store
        page.locator("#select_store").click()

        # Click text=微風店 >> nth=1
        page.locator("text=全部分店").nth(1).click()
    except TimeoutError as timeoutError:
        print("有time error錯誤:", timeoutError)
    except:
        print("有錯誤!!!!")


    time.sleep(5)
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

    # # Click text=午餐 >> nth=0
    # page.locator("text=午餐").first.click()

    # # Click td:nth-child(4)
    # page.locator("td:nth-child(4)").click()
    # # expect(page).to_have_url("https://www.feastogether.com.tw/booking-check")

    # # Select 11:30
    # page.locator("text=時間 請選擇 11:30 12:00 >> select").select_option("11:30")


isHaveSeat = False
seat = 0
dataInfo = "[aria-label=\"五月 29\\, 2022\"]"
mealTime = "text=午餐"
token = "QGuub3Vwntxa0RJbnzRlldcRGbaskNT85sS24V2bN4O"

with sync_playwright() as playwright:
    while seat <= 0:
        run(playwright)
        time.sleep(1)
    else:
        headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
        params = {"message": "尚有"+ str(seat) +"個座位"}
    
        r = requests.post("https://notify-api.line.me/api/notify",
                        headers=headers, params=params)
        print(r.status_code)  #200

        print("Have Seat!!")

    # schedule.every(10).seconds.do(run, playwright)

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
