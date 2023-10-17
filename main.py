from selenium.webdriver.firefox.options import Options
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", '127.0.0.1')
profile.set_preference("network.proxy.socks_port", 9150)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.set_preference("network.proxy.socks_version", 5)
profile.update_preferences()

options = Options()
options.profile = profile

browser = webdriver.Firefox(options)

browser.get('https://check.torproject.org')