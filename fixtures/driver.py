from selenium.webdriver import Chrome,Remote
from selenium.webdriver import ChromeOptions

def get_browser():
    browser_option = ChromeOptions()
    browser_option.page_load_strategy = 'eager'
    
    
    browser_option.add_argument("--log-level=3")
    # browser_option.add_argument("--headless=new")
    try:
        browser_option.page_load_strategy = 'eager'
        browser_option.set_capability('browserName','chrome')
        browser_option.set_capability('platformName','LINUX')
        driver = Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=browser_option
            )
        driver.set_window_size(1920,1080) #fullHD
        driver.maximize_window()
    except:   
        driver = Chrome(options=browser_option)  
        driver.set_window_size(2560,1440) #quadHD
        driver.maximize_window()
    finally:
        return driver