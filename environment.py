from fixtures.driver import get_browser
import os 

def before_scenario(context,scenario):
    BASE_URL = context.config.userdata.get('BASE_URL')
    
    context.driver = get_browser()
    context.driver.get(BASE_URL)
    context.driver.implicitly_wait(15)

def after_scenario(context,scenario):
    os.makedirs('screenshots', exist_ok=True)
    scenario_name = scenario.name.replace(' ','_').replace(',','').replace('.','')
    context.driver.save_screenshot(f'./screenshots/{scenario_name}.png')
    context.driver.quit()