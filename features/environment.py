import behave_webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()

