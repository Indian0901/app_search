from appium import webdriver


def get_driver(pac,act):
    desired_caps = {}
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = ''
    desired_caps['deviceName'] = 'sanxing'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)