def before_all(context):
    # Code to setup before running all tests (e.g., starting Appium server)
    pass

def after_all(context):
    # Code to teardown after all tests (e.g., quitting driver)
    context.driver.quit()
