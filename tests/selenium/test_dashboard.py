import os
import ssl
import time
import urllib.request
import urllib.error

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

TEST_URL = os.getenv("TEST_URL", "https://wazuh.example.com")


def test_https_reachable_and_login_form():
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(TEST_URL, context=ctx, timeout=30) as resp:
            assert resp.status in (200, 302, 401), f"Unexpected status: {resp.status}"
    except urllib.error.URLError as e:
        raise AssertionError(f"HTTPS not reachable at {TEST_URL}: {e}")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(options=options, service=ChromeService())
    try:
        driver.get(TEST_URL)
        time.sleep(3)

        assert "Wazuh" in driver.title or "Dashboard" in driver.title

      
        username = None
        password = None
        for selector in [
            'input[name="username"]',
            'input#username',
            'input[data-test-subj="userName"]',
        ]:
            elems = driver.find_elements(By.CSS_SELECTOR, selector)
            if elems:
                username = elems[0]
                break
        for selector in [
            'input[name="password"]',
            'input#password',
            'input[data-test-subj="password"]',
        ]:
            elems = driver.find_elements(By.CSS_SELECTOR, selector)
            if elems:
                password = elems[0]
                break

        assert username is not None, "Username input not found"
        assert password is not None, "Password input not found"

        # Login button presence (do not submit)
        login_btn = None
        for selector in [
            'button[type="submit"]',
            'button[data-test-subj="loginSubmit"]',
        ]:
            elems = driver.find_elements(By.CSS_SELECTOR, selector)
            if elems:
                login_btn = elems[0]
                break
        assert login_btn is not None, "Login button not found"

    finally:
        driver.quit()
