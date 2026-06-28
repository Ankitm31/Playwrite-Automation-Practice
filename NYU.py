from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://qa.benefitcenter.com/login/v3/pub/logonlw.jsp?client=NYULangoneHealth')
    page.fill('#USERNAME', '911491061')
    page.fill('#password', 'Test@1234')
    page.click('#ContinueBtn')
    page.wait_for_timeout(2000)
    page.click('#Mobile')
    page.click('#ContinueBtn')
    page.wait_for_timeout(3000)
    page.fill('#seccode','64769644')
    page.click('#Device1')
    page.click('#ContinueBtn')
    page.click('#ContinueBtn')
   # page.wait_for_timeout(3000)
    page.locator("//span[normalize-space()='Accept Cookies']").click()
    page.wait_for_timeout(3000)
    page.locator('//*[@id="main-nav"]/ul/li[2]/a').click() #Overview
    page.wait_for_selector('//*[@id="TabContainer"]/ul/li[1]/a').click()
    page.wait_for_selector('//*[@id="pdfButton"]/span/button').click() #Model button
    page.locator('a[aria-label="Hamburger Menu"]').click() #Hamburger menu
    page.locator('//*[@id="header-wrapper"]/div/div/div[2]/ng-include/nav/ul/li[4]/div/ul/li/a[6]').click() #Log out link
    page.locator('//*[@id="cnf_modalLOGOUT_MODAL"]/div/div/div[3]/button[2]').click() #logout button

    #  page.wait_for_timeout(3000)
