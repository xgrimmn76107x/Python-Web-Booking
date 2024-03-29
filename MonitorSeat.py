from calendar import calendar
from pickle import FALSE
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError
from bs4 import BeautifulSoup
import time
from datetime import datetime
import schedule
import requests
import argparse



 
def login(account, password, page):
    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Click .wk-menu-btn >> nth=0
    page.locator(".wk-menu-btn").first.click()

    # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder="手機"]
    page.locator(
        "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").click()
    page.locator("text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").fill(
        account)

    # page.fill('div[class="desktop-header hidden-sm hidden-xs"]{span[id="user_id"]}', "0912345678")

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
    global wantDate
    if '/orderAPI/otGetPossible' in response.url and response.status == 200:
        seat = 0
        res = response.json()["res7"] #res2: 饗饗，res7: 開飯
        
        index1 = res[0]
        content = index1["content"]
        index2 = content[0]#大遠百店
        # 多座位
        calendar = index2["calendar"]
        # calendar["2022-07-16"] = wantSeat
        for date in wantDate:
            tmpSeat = calendar[date]
            # tmpSeat = wantSeat
            if (tmpSeat >= wantSeat):
                wantDate[date] = tmpSeat
            seat += tmpSeat
            print(date, "座位:", tmpSeat, datetime.now())
        # 單一座位
        # data = index2["data"]
        # seat = data["seat"]
        # print("座位:", seat, datetime.now())


def run(playwright: Playwright) -> None:
    global isHaveSeat
    global wantDate
    global seat
    global oldSeat
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    page.on('response', on_response)

    # Go to https://www.feastogether.com.tw/booking/7
    page.goto("https://www.feastogether.com.tw/booking/7")
    try:
        page.wait_for_load_state('networkidle')
        # time.sleep(2)

        # Click #modal-news >> text=我知道了
        page.locator("#modal-news >> text=我知道了").click()

        # ---------------------------------------------------------------------------------------------------------------------------------------
        # Click .wk-menu-btn >> nth=0
        page.locator(".wk-menu-btn").first.click()

        # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder="手機"]
        page.locator(
            "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").click()
        page.locator("text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> [placeholder=\"手機\"]").fill(
            phone)

        # page.fill('div[class="desktop-header hidden-sm hidden-xs"]{span[id="user_id"]}', "0912345678")

        # Click text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type="password"]
        page.locator(
            "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type=\"password\"]").click()
        page.locator(
            "text=帳戶 密碼 加入會員 | 忘記密碼 登入 會員登入 會員中心 登出 會員資料 訂位紀錄 線上支付 >> input[type=\"password\"]").fill(password)
        time.sleep(2)

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
        # 要訂台中的，所以多寫這個
        # Click #select_area
        page.locator("#select_area").click()

        # Click text=台中市 >> nth=1
        page.locator("text="+area).nth(1).click()
        #------------------------------------------------------------------------------------------------------------------------
        # Click input[type="number"]
        page.locator("input[type=\"number\"]").click()

        # Fill input[type="number"]
        page.locator("input[type=\"number\"]").fill("2")
        # Click [placeholder="隔日起 \~ 一個月內"]
        page.locator("[placeholder=\"隔日起 \\~ 一個月內\"]").click()

        
        time.sleep(1.5)
        # 下一頁
        # Click svg >> nth=1
        page.locator("svg").nth(1).click()

        # Click [aria-label="五月 03\, 2022"]
        page.locator(dataInfo).click()

        # Click text=晚餐
        time.sleep(1)
        page.locator(mealTime).first.click()

        # # Click #select_store
        # page.locator("#select_store").click()

        # # Click text=微風店 >> nth=1
        # page.locator("text=全部分店").nth(1).click()

        timeloop = 0
        while timeloop <= 3600:
            timeloop += 15
            d = []
            time.sleep(15)
            # Click text=晚餐
            page.locator(mealTime).first.click()
            headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/x-www-form-urlencoded"
            }   
            if (seat >= wantSeat and seat != oldSeat):
                oldSeat = seat
                tmpMessage = ""
                for date in wantDate:
                    if (wantDate[date] >= wantSeat):
                        msg = date + "尚有" + str(wantDate[date]) + "個座位\n"
                        d.append(date[-2:])
                        tmpMessage += msg
                params = {"message": tmpMessage}
        
                r = requests.post("https://notify-api.line.me/api/notify",
                                headers=headers, params=params)
                print(r.status_code)  #200

                print("Have Seat!!")
                # 訂位------------------------------------------------------------------------

                # 訂位可能不能用了

                # page.locator("[placeholder=\"隔日起 \\~ 一個月內\"]").click()
                
                # for i in d:
                #     time.sleep(1)
                #     haveSeatDateInfo = "[aria-label=\"一月 "+ i +"\\, 2023\"]"
                #     page.locator(haveSeatDateInfo).click()
                    
                #     # 舊的，訂饗饗只有信義微風店用的
                #     # page.locator("td:nth-child(4)").click()
                    
                #     # Click td:has-text("大遠百店午餐") >> nth=0
                #     page.locator("td:has-text(\"大遠百店晚餐\")").first.click()

                #     time.sleep(2)

                #     page.locator("text=時間 請選擇 11:30 12:00 >> select").select_option("11:30")

                #     # Click text=確認訂位
                #     page.locator("text=確認訂位").click()
                    
            
            
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

class Tools():
    @staticmethod
    def transform_month(month):
        if month == '01':
            return '一'
        elif month == '02':
            return '二'
        elif month == '03':
            return '三'
        elif month == '04':
            return '四'
        elif month == '05':
            return '五'
        elif month == '06':
            return '六'
        elif month == '07':
            return '七'
        elif month == '08':
            return '八'
        elif month == '09':
            return '九'
        elif month == '10':
            return '十'
        elif month == '11':
            return '十一'
        elif month == '12':
            return '十二'
        else:
            return ''
    def transform_time(time):
        if time == 'noon':
            return '午餐'
        elif time == 'tea':
            return '下午茶'
        elif time == 'dinner':
            return '晚餐'
        else:
            return ''
    
def parser_loader():
    parser = argparse.ArgumentParser(description = 'Monitor Seat')

    parser.add_argument('--phone', type=str, default = '')
    parser.add_argument('--password', type=str, default = '')
    parser.add_argument('--date', type=str, default = '2023-01-01')
    parser.add_argument('--count', type=int, default = 2)
    parser.add_argument('--time', type=str, default = 'dinner') # noon, tea, dinner
    parser.add_argument('--area', type=str, default = '台北市') 
    parser.add_argument('--branch', type=str, default = '信義店') 
    parser.add_argument('--lineToken', type=str, default = '') 
    
    return parser

# Start ----------------------------------------------------
parser = parser_loader()
args = vars(parser.parse_args())
print(args)

dateArr = args['date'].split("-")
year = dateArr[0]
month = Tools.transform_month(dateArr[1])
day = dateArr[2]

isHaveSeat = False
seat = 0
oldSeat = 0
phone = args['phone']
password = args['password']
dataInfo = "[aria-label=\"" + month + "月 " + day + "\\, " + year + "\"]" # "[aria-label=\"一月 14\\, 2023\"]"
mealTime = "text="+ Tools.transform_time(args['time'])
wantDate = {args['date']: 0}# {"2023-01-14": 0}
wantSeat = args['count']
area = args['area']
branch = args['branch']


token = args['token']



# with sync_playwright() as playwright:
#     while True:
#         run(playwright)
#         time.sleep(2)
    
        

    # schedule.every(10).seconds.do(run, playwright)

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
