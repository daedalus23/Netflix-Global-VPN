from WebDriver import Driver
import time

def main():

    url = "https://www.netflix.com/"
    driverPath = r"C:\Users\james\PycharmProjects\Netflix-Global-VPN\WebDriver\chromedriver.exe"

    driver = Driver(driverPath)
    driver.get(url)
    driver.open_cookie()

    # driver.click('//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a')
    # time.sleep(5)
    # driver.input_value('//*[@id="id_userLoginId"]', os.environ.get("Netflix_UserName"))
    # driver.input_value('//*[@id="id_password"]', os.environ.get("Netflix_Password"))
    # time.sleep(3)
    driver.click_css('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > div > ul > li:nth-child(1) > div > a')
    driver.click('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button')
    driver.input_value('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/input', selectedMovie.title)
    driver.save_cookie()


if __name__ == "__main__":
    main()
