import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('I launch chrome browser')
def step_impl(context):
    service_obj = Service()
    context.driver = webdriver.Chrome(service=service_obj)

@when('I open orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        dashboard_text = context.driver.find_element(By.TAG_NAME, "h6").text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if dashboard_text == "Dashboard":
        context.driver.close()
        assert True,"Test Passed"

