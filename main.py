from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import email, password

# Set the path to the Edge WebDriver executable
edge_driver_path = 'C:\\Users\\kjain53\\Downloads\\edgedriver_win64\\msedgedriver.exe'
# Create an Edge browser instance with incorrect usage causing the error
driver = webdriver.Edge(executable_path=edge_driver_path)

# Maximize the browser window
driver.maximize_window()

# Navigate to the ServiceNow tool's URL
driver.get('https://uid.dxc.com/app/dxcprod_dxcservicenowbpcommercialproduction_1/exk65avoeQar4K7vM5d6/sso/saml?SAMLRequest=jVLLbtswEPwVgXe9LdkiLAOqjaJGk1SNnR56CWhynRCVSJVLKc7fl5JdJD3UyInE7nBmdpZLZG2TdLTq7bO6h989oPVObaOQnjsl6Y2imqFEqlgLSC2nu%2Br2hiZBRDujrea6IV6FCMZKrdZaYd%2BC2YEZJIeH%2B5uSPFvbIQ1DjjzAc91X%2BiXgug0VGzr2BIHQxNs4danYSPP2qJciECc%2BgVnXhe7uZMWjOy9cjurQubZT5ZI1Y7fnI8ljHMLpV56xQcN3ZmZf58NtJvIQUYfjeMT7rA2HafiSHFmDQLztpiS7uzUUyfxYHIukOCyKNIvjdJZHScYyyKM5z%2BcOiDVDlAO8PUXsYavQMmVLkkRJ6kcLP5nt4xlNCxpFwSJPfxKvvsT2SSoh1dP1jA9nENIv%2B33t1992%2B4lgkALMnUN%2FPN4fYHCK1tGS1XJaMJ08m%2Fc7v26H%2FV00WV3RXYbv2S9aHR39bje1biR%2F9aqm0S9rA8y6GazpYVpHy%2Bz%2FDcRBPFWk8I8TlELLZFMJYQCRhKuL7r8fevUH&RelayState=https%3A%2F%2Fcsc.service-now.com%2Fnow%2Fnav%2Fui%2Fclassic%2Fparams%2Ftarget%2F%2524pa_dashboards_overview.do%253Fsysparm_border%253Dtrue')

# Find the email input field and enter your email
email_field = driver.find_element(By.ID, 'input27')
email_field.send_keys(email)
# Click the "Next" button after entering the email
email_field.send_keys(Keys.RETURN)

# Wait for the password field to appear
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'input52'))
)
password_field.send_keys(password)

# Click the "Verify" button after entering the password
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# Open a new tab
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.execute_script("window.open('about:blank', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

time.sleep(2)

# Navigate to a new URL in the new tab
driver.get('https://csc.service-now.com/now/nav/ui/classic/params/target/%24pa_dashboards_overview.do%3Fsysparm_border%3Dtrue')  # Replace with the URL of the new page
time.sleep(2)
driver.get('https://csc.service-now.com/login_locate_sso.do')  # Replace with the URL you want to navigate to
email_login_field = driver.find_element(By.ID, 'sso_selector_id') # Finds email field for login
email_login_field.send_keys(email) # Enters email in the field
email_login_field.send_keys(Keys.RETURN) # Click the "Submit" button after entering the email
time.sleep (15)

# After the previous sleep, navigate to a new URL in the same tab
new_url = 'https://csc.service-now.com/now/nav/ui/classic/params/target/incident_list.do%3Fsysparm_query%3Dassignment_group%253D8f3a2549db47ff089a8da5db0b96197d%255EORassignment_group%253Dfa3a2549db47ff089a8da5db0b961923%255Estate%253D1%255EORstate%253D2%26sysparm_first_row%3D1%26sysparm_view%3D'  # Replace with the URL you want to navigate to
driver.get(new_url)
time.sleep(5)

# Define the URL you want to navigate to
url_to_refresh = 'https://csc.service-now.com/now/nav/ui/classic/params/target/incident_list.do%3Fsysparm_query%3Dassignment_group%253D8f3a2549db47ff089a8da5db0b96197d%255EORassignment_group%253Dfa3a2549db47ff089a8da5db0b961923%255Estate%253D1%255EORstate%253D2%26sysparm_first_row%3D1%26sysparm_view%3D'  # Replace with the URL you want to navigate to

# Keep refreshing indefinitely
while True:
    # Navigate to the URL
    driver.get(url_to_refresh)
    
    # Wait for 60 seconds before refreshing again
    time.sleep(5) 
