import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    service_obj = Service()
    context.driver = webdriver.Chrome(service=service_obj)


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
    assert status is True



@then('close browser')
def closeBrowser(context):
    context.driver.close()

